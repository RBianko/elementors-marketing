#!/usr/bin/env python3
"""Build Palmier scale/position keyframes that follow a Godot cursor track.

usage: zoom_keys.py <cursor.json> [--trim <source frames cut from clip start>] [--canvas 1080x1920]
Prints two JSON arrays of clip-relative rows: scale and position, for set_keyframes.
"""
import argparse
import json


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cursor")
    ap.add_argument("--canvas", default="1080x1920")
    ap.add_argument("--trim", type=int, default=0, help="source frames cut from the clip start")
    ap.add_argument("--follow-zoom", type=float, default=1.45)
    ap.add_argument("--impact-zoom", type=float, default=1.95)
    ap.add_argument("--rest-zoom", type=float, default=1.45)
    args = ap.parse_args()

    cw, ch = (int(v) for v in args.canvas.split("x"))
    d = json.load(open(args.cursor))
    W, H = d["width"], d["height"]
    frames = {f["f"]: (f["x"], f["y"]) for f in d["frames"]}
    markers = {}
    for m in d["markers"]:
        markers.setdefault(m["name"].split(":")[0], m["f"])
    last = max(frames)
    ar = (W / H) / (cw / ch)

    def tl(src):
        return src - args.trim

    def key(src, s, cx, cy, interp):
        vh = H / s
        vw = cw * (H / ch) / s
        cx = min(max(cx, vw / 2), W - vw / 2)
        cy = min(max(cy, vh / 2), H - vh / 2)
        return (tl(src), round(ar * s, 3), round(s, 3), round(0.5 - cx / W * ar * s, 4), round(0.5 - cy / H * s, 4), interp)

    drag = markers["drag_start"]
    drop = markers["drop"]
    impact = markers["impact"]
    end = markers.get("cascade_end", last)
    slot = frames[drop]
    x0, y0 = frames[args.trim]
    first_move = next((f for f in sorted(frames) if f > args.trim and abs(frames[f][0] - x0) + abs(frames[f][1] - y0) > 15), drag)
    base_cx = (frames[args.trim][0] + slot[0]) / 2
    keys = [key(args.trim, 1.0, base_cx, H / 2, "smooth"), key(first_move, 1.0, base_cx, H / 2, "smooth")]
    for f in range(first_move + 40, drop + 12, 10):
        x, y = frames[min(f, last)]
        keys.append(key(f, args.follow_zoom, x, y, "linear"))
    keys.append(key(impact - 8, args.follow_zoom, *slot, "smooth"))
    keys.append(key(impact, args.impact_zoom, *slot, "smooth"))
    keys.append(key(impact + 36, args.impact_zoom, *slot, "smooth"))
    keys.append(key(impact + 80, args.rest_zoom, slot[0], slot[1] + 30, "smooth"))
    ex, ey = frames[min(end, last)]
    keys.append(key(last, args.rest_zoom - 0.05, (slot[0] + ex) / 2, (slot[1] + ey) / 2 + 40, "smooth"))

    print(json.dumps([[k[0], k[1], k[2], k[5]] for k in keys]))
    print(json.dumps([[k[0], k[3], k[4], k[5]] for k in keys]))


if __name__ == "__main__":
    main()
