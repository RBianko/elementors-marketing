#!/usr/bin/env python3
"""Build a 9:16 timeline in Palmier Pro from an edit plan, over the MCP HTTP endpoint.

usage: palmier_build.py <plan.json> [--project palmier/ELEMS.palmier] [--timeline "<name>"] [--export out.mp4]

Palmier must be running (MCP at 127.0.0.1:19789).
"""
import argparse
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MCP = "http://127.0.0.1:19789/mcp"

CAPTION_STYLE = {
    "fontName": "Poppins-Bold", "fontSize": 60, "fontCase": "uppercase", "color": "#FFFFFF", "alignment": "center", "tracking": 1,
    "outline": {"enabled": True, "color": "#000000", "width": 8},
    "shadow": {"enabled": True, "color": "#000000", "opacity": 0.6, "blur": 6, "offset": {"x": 0, "y": 4}},
}
CAPTION_Y = 0.72
HIGHLIGHT = "#FFE600"


class Palmier:
    def __init__(self):
        self.sid = None
        self.next_id = 1
        r, headers = self._post({"jsonrpc": "2.0", "id": 0, "method": "initialize",
                                 "params": {"protocolVersion": "2025-03-26", "capabilities": {}, "clientInfo": {"name": "short", "version": "1"}}})
        self.sid = headers.get("MCP-Session-Id") or headers.get("mcp-session-id")
        self._post({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def _post(self, body):
        headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
        if self.sid:
            headers["Mcp-Session-Id"] = self.sid
        req = urllib.request.Request(MCP, data=json.dumps(body).encode(), headers=headers)
        with urllib.request.urlopen(req, timeout=600) as r:
            raw = r.read().decode()
            hdrs = {k: v for k, v in r.headers.items()}
        result = None
        for line in raw.splitlines():
            if line.startswith("data: {"):
                result = json.loads(line[6:])
        return result, hdrs

    def call(self, tool, **args):
        self.next_id += 1
        r, _ = self._post({"jsonrpc": "2.0", "id": self.next_id, "method": "tools/call", "params": {"name": tool, "arguments": args}})
        if r is None:
            return None
        if "error" in r:
            raise RuntimeError(f"{tool}: {r['error']}")
        content = r["result"].get("content", [])
        text = next((c["text"] for c in content if c.get("type") == "text"), "{}")
        if r["result"].get("isError"):
            raise RuntimeError(f"{tool}: {text[:400]}")
        try:
            return json.loads(text)
        except ValueError:
            return {"text": text}


def unique_timeline_name(p, base):
    names = {t["name"] for t in p.call("get_media").get("timelines", [])}
    name, i = base, 2
    while name in names:
        name = f"{base} v{i}"
        i += 1
    return name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--project", default=os.path.join(ROOT, "palmier", "ELEMS.palmier"))
    ap.add_argument("--timeline")
    ap.add_argument("--export")
    args = ap.parse_args()
    plan = json.load(open(args.plan))
    fps = plan["fps"]
    cw, ch = plan["canvas"]
    p = Palmier()

    p.call("manage_project", action="open", path=os.path.abspath(args.project))
    tl_name = unique_timeline_name(p, args.timeline or f"{plan['name']} 9x16")
    tl = p.call("create_timeline", name=tl_name)
    print(f"timeline {tl['timelineId']} '{tl_name}'")
    if p.call("get_timeline").get("fps") != fps:
        p.call("set_project_settings", fps=fps)

    folder = f"shorts/{plan['name']}"
    video = p.call("import_media", source={"path": plan["video"]["path"]}, folder=folder, name=f"{plan['name']} render")["mediaRef"]
    clips = p.call("add_clips", entries=[{"mediaRef": video, "startFrame": plan["video"]["startFrame"], "source": plan["video"]["source"]}])
    vclip = clips["clips"][0]["id"]
    p.call("set_project_settings", aspectRatio=f"{cw}:{ch}" if (cw, ch) != (1080, 1920) else "9:16", quality="1080p")
    p.call("set_keyframes", clipId=vclip, property="scale", keyframes=plan["keyframes"]["scale"])
    p.call("set_keyframes", clipId=vclip, property="position", keyframes=plan["keyframes"]["position"])

    if plan.get("mirror"):
        heights = {k[0]: k[2] for k in plan["keyframes"]["scale"]}
        mirrors = []
        for side in (-1, 1):
            m = p.call("add_clips", entries=[{"mediaRef": video, "startFrame": plan["video"]["startFrame"], "source": plan["video"]["source"],
                                              "includeAudio": False}])["clips"][0]["id"]
            pos = [[k[0], k[1], round(k[2] + side * heights[k[0]], 4), k[3]] for k in plan["keyframes"]["position"]]
            p.call("set_keyframes", clipId=m, property="scale", keyframes=plan["keyframes"]["scale"])
            p.call("set_keyframes", clipId=m, property="position", keyframes=pos)
            mirrors.append(m)
        p.call("set_clip_properties", clipIds=mirrors, transform={"flipVertical": True}, volumeDb=-60)
        p.call("apply_color", clipIds=mirrors, exposure=-1.6, saturation=0.6)
        p.call("apply_effect", clipIds=mirrors, effects=[{"type": "blur.gaussian", "params": {"radius": 6}}])
        main_track = next(t["trackId"] for t in p.call("get_timeline")["tracks"] if any(c.get("id") == vclip for c in t.get("clips", [])))
        p.call("manage_tracks", reorder=[{"trackId": main_track, "to": 0}])

    if plan.get("hold"):
        still = p.call("import_media", source={"path": plan["hold"]["png"]}, folder=folder, name=f"{plan['name']} hold")["mediaRef"]
        s = p.call("add_clips", entries=[{"mediaRef": still, "startFrame": plan["hold"]["frames"][0], "endFrame": plan["hold"]["frames"][1], "trackIndex": 0}])
        p.call("set_clip_properties", clipIds=[s["clips"][0]["id"]], transform=plan["hold"]["transform"])

    if plan["vo"]:
        entries = []
        for v in plan["vo"]:
            ref = p.call("import_media", source={"path": v["path"]}, folder=f"{folder}/vo", name=f"beat {v['beat']}")["mediaRef"]
            entries.append({"mediaRef": ref, "startFrame": v["startFrame"]})
        p.call("add_clips", entries=entries)

    if plan["captions"]:
        texts = [{"startFrame": c["start"], "endFrame": c["end"], "content": c["text"], "animation": "highlightPop", "highlightColor": HIGHLIGHT,
                  "style": CAPTION_STYLE, "transform": {"x": 0.5, "y": CAPTION_Y}} for c in plan["captions"] if c["end"] > c["start"]]
        p.call("add_texts", entries=texts)

    tracks = p.call("get_timeline")["tracks"]
    names = []
    vi, ai = 0, 0
    for t in tracks:
        if t["type"] == "video":
            names.append({"trackId": t["trackId"], "name": ["Captions", "Gameplay", "Mirror"][min(vi, 2)] if plan["captions"] else "Gameplay"})
            vi += 1
        else:
            names.append({"trackId": t["trackId"], "name": ["Game", "VO"][min(ai, 1)]})
            ai += 1
    p.call("manage_tracks", set=names)
    print(f"built {plan['totalFrames']} frames ({plan['totalFrames'] / fps:.1f}s), {len(plan['vo'])} voice clips, {len(plan['captions'])} captions")

    if args.export:
        job = p.call("export_project", mode="video", outputPath=os.path.abspath(args.export), resolution="Match Timeline")
        jid = job.get("jobId")
        print(f"export {jid} -> {args.export}")
        while True:
            time.sleep(3)
            lst = p.call("manage_exports", action="list")
            j = next((x for x in lst.get("exports", []) if x.get("jobId") == jid), None)
            if not j:
                continue
            st = j.get("status")
            if st in ("completed", "failed", "cancelled"):
                print(f"export {st}: {j.get('path', '')} {j.get('error', '')}")
                break


if __name__ == "__main__":
    main()
