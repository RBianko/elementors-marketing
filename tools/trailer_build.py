#!/usr/bin/env python3
"""Build the 16:9 Steam trailer timeline in Palmier Pro from the shot list in docs/STEAM_TRAILER.md.

usage: trailer_build.py [--timeline "steam_trailer 16x9"] [--export exports/steam_trailer_v5.mp4]

Palmier must be running with palmier/ELEMS.palmier open; every render is already imported there.
"""
import argparse
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from palmier_build import Palmier, unique_timeline_name  # noqa: E402

W, H = 3840, 2160
MEDIA = {
    "b": "6830A42E", "c": "E58A633F", "e": "2E01DE95", "h": "CD755912", "j": "5347C425", "l": "0BC3838C",
    "music": "532397A1", "black": "E676DBEF", "logo": "EECE59F7", "steam": "3DA85D21",
}
FLIPS = ["D4A467E8", "4EB6D8DD", "506A556B", "EEB02988", "BCE5E8E6", "D37FCFDF",
         "994CE660", "5E54F160", "D3EB6210", "DB62CDDD", "DC8704DC", "DD79FF55"]
PLATE_STYLE = {
    "fontName": "BoldPixels", "fontSize": 96, "fontCase": "uppercase", "color": "#FFFFFF", "alignment": "center", "tracking": 2,
    "outline": {"enabled": True, "color": "#000000", "width": 6},
    "shadow": {"enabled": True, "color": "#000000", "opacity": 0.8, "blur": 24, "offset": {"x": 0, "y": 0}},
}
PLATE_Y = 0.86


def impact(x, y):
    return (x + 180) / W, (y + 162) / H


BOARD = (0.5, 0.5)
FIGHT = (0.5, 0.55)
E_IMPACTS = [(14.30, 2190, 1038), (17.38, 2010, 795), (20.62, 1830, 1038), (24.00, 1650, 795), (27.25, 1470, 1038), (30.63, 1290, 795)]

SHOTS = [
    ("e", 16.88, 48, impact(2010, 795), 1.8),
    ("c", 18.30, 48, impact(1290, 795), 1.8),
    ("b", 23.00, 48, FIGHT, 1.3),
    ("j", 15.60, 48, (0.55, 0.55), 1.25),
    (None, 0, 96, None, 0),
    ("l", 5.60, 192, (0.88, 0.364), 1.5),
    ("l", 12.60, 144, impact(1830, 1038), 1.6),
    *[("e", t - 0.55, 72, impact(x, y), 1.7) for t, x, y in E_IMPACTS],
    ("c", 16.90, 216, impact(1290, 795), 1.6),
    ("h", 5.80, 96, (0.672, 0.11), 1.6),
    ("h", 10.60, 120, impact(2190, 1038), 1.6),
    ("b", 13.20, 144, impact(1470, 1038), 1.5),
    ("b", 25.00, 240, FIGHT, 1.1),
    ("j", 14.20, 240, (0.55, 0.55), 1.15),
]
FLIP_FRAMES = [48, 48, 36, 36, 24, 24, 24, 12, 12, 12, 12, 12]
OUTRO = 300
CYCLE = 6

PLATES = [
    (288, 480, "ROLL ELEMENT DICE"),
    (480, 624, "EVERY FACE IS AN ELEMENT"),
    (624, 840, "ANY ELEMENT ON ANY CREATURE"),
    (840, 1056, "6 ELEMENTS × 8 CREATURES"),
    (1056, 1272, "THREE OF A KIND MERGE UP"),
    (1272, 1488, "HUNT THE LUCKY ROLL"),
    (1488, 1632, "STACK SYNERGIES"),
    (1632, 1872, "FIGHT REAL PLAYERS' BOARDS"),
    (1872, 2112, "BEAT THE BOSSES"),
    (2112, 2412, "NO TWO RUNS THE SAME"),
]


def framing(center, z, frames):
    fx, fy = center
    rows_s, rows_p = [], []
    for f, zz in ((0, z), (frames - 1, z * 1.06)):
        x = min(0, max(1 - zz, 0.5 - fx * zz))
        y = min(0, max(1 - zz, 0.5 - fy * zz))
        rows_s.append([f, round(zz, 4), round(zz, 4), "linear"])
        rows_p.append([f, round(x, 4), round(y, 4), "linear"])
    return rows_s, rows_p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeline", default="steam_trailer 16x9")
    ap.add_argument("--export")
    args = ap.parse_args()
    p = Palmier()

    tl = p.call("create_timeline", name=unique_timeline_name(p, args.timeline))
    p.call("set_active_timeline", timelineId=tl["timelineId"])
    p.call("organize_media", moves=[{"into": "trailer", "items": [tl["timelineId"]]}])

    cuts, at = [], 0
    for key, src, frames, center, z in SHOTS:
        if key:
            cuts.append((MEDIA[key], src, frames, center, z, at))
        else:
            title = (at, at + frames)
        at += frames
    flips_at = at
    for ref, frames in zip(FLIPS, FLIP_FRAMES):
        cuts.append((ref, 1.4, frames, BOARD, 1.35, at))
        at += frames
    outro_at = at
    i = 0
    while at < outro_at + OUTRO:
        frames = min(CYCLE, outro_at + OUTRO - at)
        cuts.append((FLIPS[i % len(FLIPS)], 1.4 + (i // len(FLIPS)) * 0.1, frames, BOARD, 1.35, at))
        at += frames
        i += 1
    total = at

    entries = [{"mediaRef": ref, "startFrame": start, "source": [src, src + frames / 60 + 0.05], "includeAudio": ref not in FLIPS}
               for ref, src, frames, _, _, start in cuts]
    added = p.call("add_clips", entries=entries)["clips"]
    p.call("set_project_settings", aspectRatio="16:9", quality="1080p")
    ids = {c["id"] for c in added}
    gameplay = next(t for t in p.call("get_timeline")["tracks"] if t["type"] == "video" and any(c["id"] in ids for c in t.get("clips", [])))
    by_start = {c["frames"][0]: c for c in gameplay["clips"]}
    for ref, src, frames, center, z, start in cuts:
        c = by_start[start]
        if c["frames"][1] - c["frames"][0] != frames:
            p.call("set_clip_properties", clipIds=[c["id"]], durationFrames=frames)
        s, pos = framing(center, z, frames)
        p.call("set_keyframes", clipId=c["id"], property="scale", keyframes=s)
        p.call("set_keyframes", clipId=c["id"], property="position", keyframes=pos)

    lengths = {start: frames for _, _, frames, _, _, start in cuts}
    audio = []
    for c in next(t for t in p.call("get_timeline")["tracks"] if t["trackId"] == gameplay["trackId"])["clips"]:
        a = c.get("audio")
        if a:
            audio.append(a["id"])
            span = a.get("frames", c["frames"])
            if span[1] - span[0] != lengths[c["frames"][0]]:
                p.call("set_clip_properties", clipIds=[a["id"]], durationFrames=lengths[c["frames"][0]])
    p.call("set_clip_properties", clipIds=audio, volumeDb=-8)

    black = p.call("add_clips", entries=[{"mediaRef": MEDIA["black"], "startFrame": title[0], "endFrame": title[1]},
                                         {"mediaRef": MEDIA["black"], "startFrame": outro_at, "endFrame": total}])["clips"]
    full = {"centerX": 0.5, "centerY": 0.5, "width": 1, "height": 1}
    p.call("set_clip_properties", clipIds=[c["id"] for c in black], transform=full)
    p.call("set_keyframes", clipId=black[1]["id"], property="opacity", keyframes=[[0, 0], [30, 0.7], [OUTRO - 40, 0.7], [OUTRO - 1, 1]])

    logo = p.call("add_clips", entries=[{"mediaRef": MEDIA["logo"], "startFrame": title[0] + 6, "endFrame": title[1]},
                                        {"mediaRef": MEDIA["logo"], "startFrame": outro_at + 15, "endFrame": total - 40}])["clips"]
    p.call("set_clip_properties", clipIds=[logo[0]["id"]], transform={"centerX": 0.5, "centerY": 0.5, "width": 0.55, "height": 0.356},
           fadeInFrames=12, fadeOutFrames=8)
    p.call("set_clip_properties", clipIds=[logo[1]["id"]], transform={"centerX": 0.5, "centerY": 0.4, "width": 0.5, "height": 0.323},
           fadeInFrames=15, fadeOutFrames=20)
    steam = p.call("add_clips", entries=[{"mediaRef": MEDIA["steam"], "startFrame": outro_at + 45, "endFrame": total - 40}])["clips"]
    p.call("set_clip_properties", clipIds=[steam[0]["id"]], transform={"centerX": 0.5, "centerY": 0.62, "width": 0.05, "height": 0.089},
           fadeInFrames=10, fadeOutFrames=20)

    texts = [{"startFrame": a, "endFrame": b, "content": t, "animation": "slideUp", "style": PLATE_STYLE, "transform": {"x": 0.5, "y": PLATE_Y}}
             for a, b, t in PLATES]
    texts.append({"startFrame": outro_at + 45, "endFrame": total - 40, "content": "WISHLIST ON STEAM", "animation": "popIn",
                  "style": PLATE_STYLE, "transform": {"x": 0.5, "y": 0.76}})
    p.call("add_texts", entries=texts)

    music = p.call("add_clips", entries=[{"mediaRef": MEDIA["music"], "startFrame": 0, "source": [0.44, 0.44 + total / 60]}])["clips"]
    p.call("set_clip_properties", clipIds=[music[0]["id"]], fadeInFrames=6, fadeOutFrames=90, volumeDb=1)
    print(f"timeline {tl['timelineId']}: {total} frames ({total / 60:.1f}s), {len(cuts)} cuts, flips from {flips_at}, outro from {outro_at}")

    if args.export:
        job = p.call("export_project", mode="video", outputPath=os.path.abspath(args.export), resolution="Match Timeline")
        jid = job.get("jobId")
        while True:
            time.sleep(3)
            j = next((x for x in p.call("manage_exports", action="list").get("exports", []) if x.get("jobId") == jid), None)
            if j and j.get("status") in ("completed", "failed", "cancelled"):
                print(f"export {j['status']}: {j.get('path', '')} {j.get('error', '')}")
                break


if __name__ == "__main__":
    main()
