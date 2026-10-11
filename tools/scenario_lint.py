#!/usr/bin/env python3
"""Pre-render check of a short scenario: timing of voice vs actions, hook placement, targets.

usage: scenario_lint.py <scenario.md> [--json]

Durations are estimates (no render, no voice file yet). They flag beats whose
line is longer than the actions under it, a first punch that lands too late,
and a total length outside the short-form window.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scenario import parse  # noqa: E402

SEC_PER_WORD = 0.38
SEC_PER_SENTENCE_PAUSE = 0.25
HOVER_MOVE = 0.55
DRAG_BASE = 1.25
CLICK_BASE = 0.85
DRIFT = 0.3
BATTLE_SEC = 39.0
SUMMARY_SETTLE = 1.0
PUNCH_DEADLINE = 5.5
REACTION_DELAY = 1.0
TOTAL_MIN, TOTAL_MAX = 10.0, 32.0
MAX_WORDS_PER_LINE = 16

MARKERS = {"warmup", "impact", "star_up", "cascade_end", "battle_start", "battle_end",
           "summary", "summary:focus", "summary:damage", "summary:synergies"}
MARKER_PREFIX = ("beat:", "drag_start", "drop", "apply", "impact:", "summary:dps:",
                 "summary:kills:", "summary:unit:")
REGIONS = {"shop", "board", "synergies", "bench", "stash", "dice", "battle", "roll",
           "gold", "level", "hp", "tooltip"}
TARGET_RE = re.compile(r"^(board:(\d+|bare|best|any|empty)|bench:\d+|stash:\d+|shop:\d+|recap:\d+|node:%\w+)$")
OPTIONS = {"at", "punch", "focus", "zoom", "align", "lead", "anchor", "n", "actions", "vo"}


def action_seconds(a):
    do = a["do"]
    if do in ("wait", "idle", "wander"):
        return float(a.get("s", 0.5))
    if do in ("hover", "move"):
        return HOVER_MOVE + float(a.get("hold", 0.3))
    if do == "drag":
        return DRAG_BASE + float(a.get("hold", 0.4))
    if do in ("click", "buy"):
        return CLICK_BASE + float(a.get("hold", 0.2))
    if do == "drift":
        return DRIFT
    if do == "battle":
        return BATTLE_SEC / float(a.get("speed", 1)) + float(a.get("hold", 0.5))
    if do == "summary":
        return SUMMARY_SETTLE + float(a.get("hold", 0.5))
    return 0.0


def speech_seconds(line):
    words = re.findall(r"[A-Za-z0-9'’]+", line)
    sentences = len(re.findall(r"[.!?…]+", line)) or 1
    return len(words) * SEC_PER_WORD + sentences * SEC_PER_SENTENCE_PAUSE, len(words)


def marker_ok(name):
    return name in MARKERS or name.startswith(MARKER_PREFIX)


def lint(path):
    sc = parse(path)
    meta, beats = sc["meta"], sc["beats"]
    problems, rows = [], []
    t = 0.0
    first_punch = None
    for i, b in enumerate(beats):
        n = b["n"]
        secs = sum(action_seconds(a) for a in b["actions"])
        vo_secs, words = speech_seconds(b["vo"]) if b["vo"] else (0.0, 0)
        rows.append({"beat": n, "start": round(t, 2), "actions_s": round(secs, 2),
                     "voice_s": round(vo_secs, 2), "words": words, "punch": b["punch"]})
        if b["punch"] and first_punch is None:
            first_punch = t
        # The line of a beat may run over the silent beats after it. A line right
        # before a punch beat (or with anchor: end) is placed to end at the punch
        # and may start before the clip on a hold still, so it is never short.
        budget = secs + sum(sum(action_seconds(a) for a in nb["actions"])
                            for nb in beats[i + 1:] if not nb["vo"])
        nxt = beats[i + 1] if i + 1 < len(beats) else None
        anchored_end = b.get("anchor") == "end" or (nxt is not None and nxt["punch"] and not b["punch"])
        # A reaction starts a beat after the event (align.py VO_LEAD_AFTER_PUNCH).
        need = vo_secs + (REACTION_DELAY if b["punch"] else 0.0)
        if b["vo"] and not anchored_end and need > budget + 0.4:
            problems.append(f"beat {n}: line needs ~{need:.1f}s with the reaction delay but the beat and the silent beats after it last ~{budget:.1f}s; add idle/wait or shorten the line")
        if words > MAX_WORDS_PER_LINE:
            problems.append(f"beat {n}: {words} words in one line; a streamer would say it in two beats")
        if b["vo"] and ("—" in b["vo"] or "–" in b["vo"]):
            problems.append(f"beat {n}: dash inside the voice line; use a period or an ellipsis")
        if not marker_ok(str(b["at"])):
            problems.append(f"beat {n}: unknown marker at: {b['at']}")
        for a in b["actions"]:
            for key in ("target", "from", "to"):
                v = a.get(key)
                if v and not TARGET_RE.match(v):
                    hint = " (regions work only in focus:)" if v in REGIONS else ""
                    problems.append(f"beat {n}: bad target {v}{hint}")
            if a["do"] not in ("wait", "idle", "wander", "drift", "hover", "move", "click", "buy", "drag", "battle", "summary", "mark", "set"):
                problems.append(f"beat {n}: unknown action {a['do']}")
        for k in b:
            if k not in OPTIONS:
                problems.append(f"beat {n}: unknown option {k}")
        if "focus" in b and isinstance(b["focus"], str):
            f = b["focus"]
            if f not in REGIONS and not TARGET_RE.match(f):
                problems.append(f"beat {n}: bad focus {f}")
        t += secs
    if first_punch is None:
        problems.append("no punch beat: the short has no impact moment")
    elif first_punch > PUNCH_DEADLINE:
        problems.append(f"first punch at ~{first_punch:.1f}s; fine only for a slow-build structure, a cold-open hook needs it inside {PUNCH_DEADLINE}s")
    if t < TOTAL_MIN or t > TOTAL_MAX:
        problems.append(f"estimated length {t:.1f}s; aim for {TOTAL_MIN:.0f}-{TOTAL_MAX:.0f}s")
    if not beats:
        problems.append("no beats parsed")
    if "voice" not in meta:
        problems.append("frontmatter has no voice:")
    if "base" in meta:
        base_md = Path(path).resolve().parent / f"{meta['base']}.md"
        if not base_md.exists():
            problems.append(f"base scenario {meta['base']} not found next to this file")
        else:
            bb = parse(str(base_md))["beats"]
            mine = [(b["n"], b["actions"], b["at"], b["punch"]) for b in beats]
            theirs = [(b["n"], b["actions"], b["at"], b["punch"]) for b in bb]
            if mine != theirs:
                problems.append("variant beats differ from the base in actions, markers or punch; a variant may change only the lines")
    if isinstance(meta.get("board"), str) and "stage" not in meta:
        problems.append("player board without stage:; the pool spans rounds 1-15")
    return {"name": meta.get("name"), "beats": rows, "total_s": round(t, 2),
            "first_punch_s": None if first_punch is None else round(first_punch, 2), "problems": problems}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    out = lint(args.scenario)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        for r in out["beats"]:
            mark = " PUNCH" if r["punch"] else ""
            print(f"beat {r['beat']:>2}  t={r['start']:5.1f}s  actions {r['actions_s']:4.1f}s  voice {r['voice_s']:4.1f}s ({r['words']} w){mark}")
        print(f"total ~{out['total_s']}s, first punch at {out['first_punch_s']}s")
        for p in out["problems"]:
            print("WARN", p)
    sys.exit(1 if out["problems"] else 0)


if __name__ == "__main__":
    main()
