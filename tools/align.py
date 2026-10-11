#!/usr/bin/env python3
"""Turn a render + per-beat voice files into an edit plan for Palmier.

usage: align.py <scenario.md> [--canvas 1080x1920] [--out renders/<name>/plan.json]

Reads renders/<name>/<name>.cursor.json and vo/<name>/beat_<n>.words.json.
Frames in the plan are timeline frames unless the key says clip-relative.
"""
import argparse
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenario  # noqa: E402

FOLLOW_ZOOM = 1.45
PUNCH_ZOOM = 1.95
REST_ZOOM = 1.4
PUNCH_HOLD = 36
VO_GAP_BEFORE = 5
VO_LEAD_AFTER_PUNCH = 12
MAX_CAPTION_WORDS = 3


def marker_frame(markers, name):
    for m in markers:
        if m["name"] == name or m["name"].split(":")[0] == name:
            return m
    return None


def chunk_words(words):
    chunks, cur = [], []
    for w in words:
        cur.append(w)
        if len(cur) >= MAX_CAPTION_WORDS or w[0][-1] in ".?!,":
            chunks.append(cur)
            cur = []
    if cur:
        chunks.append(cur)
    return chunks


class Camera:
    def __init__(self, W, H, cw, ch):
        self.W, self.H = W, H
        self.ar = (W / H) / (cw / ch)
        self.cw, self.ch = cw, ch
        self.scale, self.pos = [], []

    def key(self, f, s, cx, cy, interp="smooth"):
        vh = self.H / s
        vw = self.cw * (self.H / self.ch) / s
        cx = min(max(cx, vw / 2), self.W - vw / 2)
        cy = min(max(cy, vh / 2), self.H - vh / 2)
        self.scale.append([f, round(self.ar * s, 3), round(s, 3), interp])
        self.pos.append([f, round(0.5 - cx / self.W * self.ar * s, 4), round(0.5 - cy / self.H * s, 4), interp])


def build_camera(frames, markers, beats, trim, last, cam):
    def at(src):
        x, y = frames[min(max(src, 0), last)][:2]
        return x, y

    def rel(src):
        return src - trim

    def cursor_driven(b):
        return any(a["do"] in ("drag", "hover", "click", "drift", "wander") for a in b.get("actions", []))

    def fit(b):
        fx, fy, fw, fh = b["focus_rect"]
        zoom = b.get("zoom")
        if not zoom:
            vis_w = cam.cw * (cam.H / cam.ch)
            zoom = min(vis_w / (fw * 1.3), cam.H / (fh * 1.3))
            zoom = min(max(zoom, 1.0), 2.6)
        vw = cam.cw * (cam.H / cam.ch) / zoom
        align = b.get("align", "center")
        cx = fx + fw / 2 if align == "center" else (fx + vw * 0.45 if align == "left" else fx + fw - vw * 0.45)
        return zoom, cx, fy + fh / 2

    x0, y0 = at(trim)
    first_move = next((f for f in range(trim, last + 1) if abs(frames[f][0] - x0) + abs(frames[f][1] - y0) > 15), trim + 1)
    first_target = next((b["focus_xy"] for b in beats if b.get("focus_xy")), None) or at(last)
    base_c = ((x0 + first_target[0]) / 2, cam.H / 2)
    cam.key(0, 1.0, *base_c)
    if first_move > trim + 1:
        cam.key(rel(first_move), 1.0, *base_c)

    battle = marker_frame(markers, "battle_start"), marker_frame(markers, "battle_end")
    ordered = sorted(beats, key=lambda b: b["frame"])
    cursor = max(first_move + 40, trim + 1)
    for i, b in enumerate(ordered):
        seg_start = max(b["frame"], trim)
        seg_end = ordered[i + 1]["frame"] if i + 1 < len(ordered) else last
        if b.get("punch"):
            if b.get("focus_rect"):
                zoom, px, py = fit(b)
                zoom = b.get("zoom") or PUNCH_ZOOM
            else:
                px, py = at(seg_start)
                zoom = b.get("zoom") or PUNCH_ZOOM
            cam.key(rel(seg_start) - 8, FOLLOW_ZOOM, px, py)
            cam.key(rel(seg_start), zoom, px, py)
            cam.key(rel(seg_start) + PUNCH_HOLD, zoom, px, py)
            if b.get("focus_rect") and b.get("zoom"):
                cam.key(rel(seg_end), zoom, px, py)
            else:
                cam.key(rel(seg_start) + PUNCH_HOLD + 44, FOLLOW_ZOOM, px, py + 30)
            cursor = seg_end
            continue
        if battle[0] and seg_start <= battle[0]["f"] < seg_end:
            cam.key(rel(max(seg_start, cursor)), FOLLOW_ZOOM, *at(seg_start), interp="linear")
            cam.key(rel(battle[0]["f"]) + 20, 1.0, cam.W / 2, cam.H / 2)
            end = battle[1]["f"] if battle[1] else seg_end
            cam.key(rel(end), 1.0, cam.W / 2, cam.H / 2)
            cursor = end
            continue
        if cursor_driven(b):
            s = max(seg_start, cursor)
            for f in range(s, seg_end, 10):
                cam.key(rel(f), FOLLOW_ZOOM, *at(f), interp="linear")
            cam.key(rel(seg_end) - 1, FOLLOW_ZOOM, *at(seg_end - 1), interp="linear")
            cursor = seg_end
        elif b.get("focus_rect"):
            zoom, cx, cy = fit(b)
            cam.key(rel(seg_start) + 15, zoom, cx, cy)
            cam.key(rel(seg_end) - 1, zoom, cx, cy)
            cursor = seg_end
    if not any(k[0] >= rel(last) - 1 for k in cam.scale):
        lx, ly = cam.pos[-1][1], cam.pos[-1][2]
        ex, ey = at(last)
        cam.key(rel(last), REST_ZOOM, ex, ey + 40)


def beats_focus(beats, frame):
    for b in beats:
        if b.get("frame") == frame and b.get("focus_xy"):
            return b["focus_xy"]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario")
    ap.add_argument("--canvas", default="1080x1920")
    ap.add_argument("--out")
    args = ap.parse_args()
    sc = scenario.parse(args.scenario)
    name = sc["meta"]["name"]
    rdir = os.path.join(ROOT, "renders", name)
    cur = json.load(open(os.path.join(rdir, f"{name}.cursor.json")))
    fps, W, H = cur["fps"], cur["width"], cur["height"]
    cw, ch = (int(v) for v in args.canvas.split("x"))
    frames = {f["f"]: (f["x"], f["y"], f["down"]) for f in cur["frames"]}
    last = max(frames)
    markers = cur["markers"]
    wm = marker_frame(markers, "warmup")
    trim = wm["f"] if wm else 0

    beats = []
    for b in sc["beats"]:
        m = marker_frame(markers, str(b["at"]))
        if m is None:
            if b["vo"] or b.get("punch"):
                sys.exit(f"beat {b['n']}: marker '{b['at']}' not in render; available: {sorted({x['name'] for x in markers})}")
            print(f"beat {b['n']}: no marker '{b['at']}', skipped (no voice, no punch)", file=sys.stderr)
            continue
        fb = dict(b)
        fb["frame"] = m["f"]
        explicit_focus = b.get("focus") or str(b["at"]) != f"beat:{b['n']}"
        if m.get("focus") and explicit_focus:
            fo = m["focus"]
            fb["focus_rect"] = (fo["x"], fo["y"], fo["w"], fo["h"])
            fb["focus_xy"] = (fo["x"] + fo["w"] / 2, fo["y"] + fo["h"] / 2)
        if b["vo"]:
            wp = os.path.join(ROOT, "vo", name, f"beat_{b['n']}.words.json")
            mp3 = os.path.join(ROOT, "vo", name, f"beat_{b['n']}.mp3")
            if not os.path.exists(mp3):
                sys.exit(f"beat {b['n']}: no voice file {mp3}; run tts.py or drop the file there")
            if os.path.exists(wp):
                fb["words"] = json.load(open(wp))
            else:
                import tts
                dur = tts.duration_of(mp3)
                fb["words"] = {"duration": dur, "words": tts.words_proportional(b["vo"], dur)}
                print(f"beat {b['n']}: no word timings, using proportional timing", file=sys.stderr)
            fb["mp3"] = mp3
        beats.append(fb)

    def rel(src):
        return src - trim

    vo = []
    for i, b in enumerate(beats):
        if not b.get("vo"):
            continue
        dur = round(b["words"]["duration"] * fps)
        nxt = beats[i + 1] if i + 1 < len(beats) else None
        gap = (nxt["frame"] - b["frame"]) if nxt else None
        anchor = b.get("anchor") or ("end" if (nxt and nxt.get("punch") and not b.get("punch") and gap < dur + 2 * fps) else "start")
        lead = int(b.get("lead", VO_LEAD_AFTER_PUNCH if b.get("punch") else 0))
        if anchor == "end" and nxt:
            start = rel(nxt["frame"]) - VO_GAP_BEFORE - dur
        else:
            start = rel(b["frame"]) + lead
        if vo and not b.get("punch"):
            prev_end = vo[-1]["start_clip"] + vo[-1]["dur"]
            if start < prev_end + 6:
                print(f"beat {b['n']}: voice pushed {prev_end + 6 - start} frames late, previous line overruns the beat (add idle time in the scenario)", file=sys.stderr)
                start = prev_end + 6
        elif vo and vo[-1]["start_clip"] + vo[-1]["dur"] > start:
            print(f"beat {b['n']}: previous voice line overlaps this punch line, shorten it or add idle time", file=sys.stderr)
        vo.append({"beat": b["n"], "start_clip": start, "dur": dur, "mp3": b["mp3"], "words": b["words"]["words"]})

    offset = max([0] + [-v["start_clip"] for v in vo])
    clip_len = last - trim + 1
    last_vo_end = max([0] + [v["start_clip"] + v["dur"] for v in vo])
    last_marker = max(b["frame"] for b in beats)
    end_clip = min(clip_len, max(last_vo_end + fps, rel(last_marker) + int(1.5 * fps)))

    cam = Camera(W, H, cw, ch)
    build_camera(frames, markers, beats, trim, trim + end_clip - 1, cam)

    captions = []
    for v in vo:
        for chunk in chunk_words(v["words"]):
            s = offset + v["start_clip"] + round(chunk[0][1] * fps)
            e = offset + v["start_clip"] + round(chunk[-1][2] * fps) + 6
            captions.append({"start": s, "end": e, "text": " ".join(w[0] for w in chunk)})
    for a, b in zip(captions, captions[1:]):
        if a["end"] > b["start"]:
            a["end"] = b["start"]

    hold = None
    if offset > 0:
        png = os.path.join(rdir, "hold_first.png")
        src_png = os.path.join(rdir, "frames", f"frame{trim:08d}.png")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src_png, "-vf", f"scale={W}:{H}:flags=neighbor", png], check=True)
        hold = {"png": png, "frames": [0, offset], "transform": {"centerX": round(cam.pos[0][1] + cam.scale[0][1] / 2, 4), "centerY": 0.5,
                                                                "width": cam.scale[0][1], "height": 1.0}}

    plan = {
        "name": name,
        "source_build": cur.get("source_build"),
        "fps": fps,
        "canvas": [cw, ch],
        "video": {"path": os.path.join(rdir, f"{name}.mp4"), "source": [round(trim / fps, 4), round((trim + end_clip) / fps, 4)],
                  "startFrame": offset, "trim": trim},
        "hold": hold,
        "keyframes": {"scale": cam.scale, "position": cam.pos},
        "vo": [{"beat": v["beat"], "path": v["mp3"], "startFrame": offset + v["start_clip"]} for v in vo],
        "captions": captions,
        "beats": [{"n": b["n"], "frame": offset + rel(b["frame"]), "punch": bool(b.get("punch")), "at": b["at"]} for b in beats],
        "totalFrames": offset + end_clip,
    }
    out = args.out or os.path.join(rdir, "plan.json")
    json.dump(plan, open(out, "w"), indent=1)
    print(f"plan: {out}")
    print(f"  clip src {plan['video']['source']} at frame {offset}, total {plan['totalFrames']} frames ({plan['totalFrames'] / fps:.1f}s)")
    for b in plan["beats"]:
        print(f"  beat {b['n']}: frame {b['frame']} ({b['at']}){' PUNCH' if b['punch'] else ''}")
    for v in plan["vo"]:
        print(f"  vo beat {v['beat']}: frame {v['startFrame']}")
    if any(v["startFrame"] < 0 for v in plan["vo"]):
        print("  WARNING: a voice line starts before the timeline", file=sys.stderr)


if __name__ == "__main__":
    main()
