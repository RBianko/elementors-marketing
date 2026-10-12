#!/usr/bin/env python3
"""Parse a short scenario (markdown) into beats, or emit the harness scenario JSON.

usage: scenario.py <scenario.md> [--harness] [--beats]

Scenario format:

    ---
    name: dps_shock
    voice: ninja
    board: [{"slot": 2, "unit": "reptile", "element": "bare", "stars": 1}]
    stash: [{"element": "fire", "stars": 1}]
    ---
    1. hover stash:0 0.45 {at: warmup} — "Okay wait, what happens if I put fire on a lizard?"
    2. drag stash:0 -> board:2 {at: impact, punch} — "OH. Okay okay okay."
    3. wait 0.5; wander 1.2 r10

Beat line: `N. <actions> {options} — "voice line"`. Actions are `;`-separated, the
braces and the voice line are optional. Options: `at: <marker>` (defaults to
`beat:N`), `punch`, `focus: <name>`, `lead: <frames>`, `anchor: start|end`, `zoom: <factor>`,
`align: left|center|right` (which end of a wide focus rect to frame).
Everything in the frontmatter except name/voice/vo/music is passed through to
the harness scenario (seed, round, level, gold, dice, board, bench, stash,
cursor_start, ...). JSON values are allowed on a single line.
"""
import argparse
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

BEAT_RE = re.compile(r"^\s*(\d+)\.\s*(.*?)\s*$")
VO_RE = re.compile(r"\s(?:—|--)\s*[\"“](.*)[\"”]\s*$")
OPTS_RE = re.compile(r"\{([^}]*)\}")
EDIT_KEYS = {"name", "voice", "vo", "music", "model", "base", "hook", "angle", "mood", "promise", "button", "render", "camera"}


def parse_value(v):
    v = v.strip()
    if v[:1] in "[{":
        return json.loads(v)
    if v in ("true", "false"):
        return v == "true"
    if re.fullmatch(r"-?\d+", v):
        return int(v)
    if re.fullmatch(r"-?\d+\.\d+", v):
        return float(v)
    return v


def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.index("\n---", 3)
    meta = {}
    for line in text[3:end].strip().splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = parse_value(v)
    return meta, text[end + 4:]


def parse_action(token):
    words = token.split()
    if not words:
        return None
    do, args = words[0], words[1:]
    act = {"do": do}
    if do == "wander":
        for a in args:
            if a.startswith("r"):
                act["radius"] = float(a[1:])
            else:
                act["s"] = float(a)
    elif do == "hover":
        act["target"] = args[0]
        if len(args) > 1:
            act["hold"] = float(args[1])
    elif do == "drag":
        src, _, dst, *rest = args
        act.update({"from": src, "to": dst})
        if rest:
            act["hold"] = float(rest[0])
    elif do in ("wait", "idle"):
        act["s"] = float(args[0])
    elif do == "click":
        act["target"] = args[0]
    elif do == "drift":
        dx, dy = args[0].split(",")
        act["by"] = [float(dx), float(dy)]
    else:
        for a in args:
            if "=" in a:
                k, v = a.split("=", 1)
                act[k] = parse_value(v)
            else:
                act.setdefault("args", []).append(a)
    return act


def parse_beat(n, body):
    beat = {"n": n, "actions": [], "at": f"beat:{n}", "punch": False, "vo": None}
    m = VO_RE.search(body)
    if m:
        beat["vo"] = m.group(1).strip()
        body = body[: m.start()]
    m = OPTS_RE.search(body)
    if m:
        for opt in m.group(1).split(","):
            opt = opt.strip()
            if not opt:
                continue
            if ":" in opt:
                k, v = opt.split(":", 1)
                beat[k.strip()] = parse_value(v)
            else:
                beat[opt] = True
        body = body[: m.start()] + body[m.end():]
    for token in body.split(";"):
        act = parse_action(token.strip())
        if act:
            beat["actions"].append(act)
    return beat


def parse(path):
    text = open(path, encoding="utf-8").read()
    meta, body = parse_frontmatter(text)
    beats = []
    for line in body.splitlines():
        m = BEAT_RE.match(line)
        if m:
            beats.append(parse_beat(int(m.group(1)), m.group(2)))
    if "name" not in meta:
        meta["name"] = re.sub(r"\.md$", "", path.rsplit("/", 1)[-1])
    return {"meta": meta, "beats": beats}


def harness_json(sc):
    out = {k: v for k, v in sc["meta"].items() if k not in EDIT_KEYS}
    if isinstance(out.get("save"), str) and not out["save"].startswith("/"):
        out["save"] = str((REPO / out["save"]).resolve())
    out["name"] = sc["meta"]["name"]
    actions = []
    for b in sc["beats"]:
        mark = {"do": "mark", "name": f"beat:{b['n']}"}
        if b.get("focus"):
            mark["focus"] = b["focus"]
        actions.append(mark)
        actions.extend(b["actions"])
    out["actions"] = actions
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario")
    ap.add_argument("--harness", action="store_true", help="print the harness scenario JSON")
    ap.add_argument("--beats", action="store_true", help="print parsed beats")
    args = ap.parse_args()
    sc = parse(args.scenario)
    if args.harness:
        print(json.dumps(harness_json(sc), indent=2))
    else:
        print(json.dumps(sc if args.beats else sc["meta"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
