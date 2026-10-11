#!/usr/bin/env python3
"""Generate one voice file per beat with ElevenLabs, with word timings.

usage: tts.py <scenario.md> [--force] [--model eleven_v3]
       tts.py --voices

Writes vo/<name>/beat_<n>.mp3 and beat_<n>.words.json ({text, duration,
words: [[word, start, end], ...]}). Reads ELEVENLABS_API_KEY from .env at the
repo root. Voice names are resolved against voices.json, then against the
account's voice library by name (case-insensitive prefix), and cached.
"""
import argparse
import base64
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import scenario  # noqa: E402

API = "https://api.elevenlabs.io/v1"


def load_env():
    path = os.path.join(ROOT, ".env")
    if os.path.exists(path):
        for line in open(path):
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k, v)
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY missing: put it in .env")
    return key


def request(key, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, headers={"xi-api-key": key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"{path}: {e.code} {e.read().decode()[:400]}") from None


def list_voices(key):
    return request(key, "/voices")["voices"]


def resolve_voice(key, name):
    reg_path = os.path.join(ROOT, "voices.json")
    reg = json.load(open(reg_path)) if os.path.exists(reg_path) else {}
    if name in reg:
        return reg[name]["voice_id"]
    if re.fullmatch(r"[A-Za-z0-9]{20}", name):
        return name
    needle = name.lower()
    for v in list_voices(key):
        short = re.split(r"\s+[-–]\s+", v["name"])[0].strip().lower()
        if short == needle or v["name"].lower().startswith(needle):
            reg[needle] = {"voice_id": v["voice_id"], "name": v["name"]}
            json.dump(reg, open(reg_path, "w"), indent=2)
            return v["voice_id"]
    sys.exit(f"voice '{name}' not found; run tts.py --voices")


def words_from_alignment(al):
    chars, starts, ends = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    words, cur, s = [], "", None
    for c, st, en in zip(chars, starts, ends):
        if c.isspace():
            if cur:
                words.append([cur, s, prev_end])
                cur, s = "", None
            continue
        if s is None:
            s = st
        cur += c
        prev_end = en
    if cur:
        words.append([cur, s, prev_end])
    return words


def words_proportional(text, duration):
    toks = text.split()
    weights = [len(re.sub(r"[^\w]", "", t)) + 1 for t in toks]
    total = sum(weights)
    t, out = 0.0, []
    for tok, w in zip(toks, weights):
        d = duration * w / total
        out.append([tok, round(t, 3), round(t + d, 3)])
        t += d
    return out


def duration_of(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(out.stdout.strip())


def synth(key, voice_id, model, text, prev, nxt):
    body = {"text": text, "model_id": model}
    if "v3" not in model and "v4" not in model:
        if prev:
            body["previous_text"] = prev
        if nxt:
            body["next_text"] = nxt
    try:
        r = request(key, f"/text-to-speech/{voice_id}/with-timestamps?output_format=mp3_44100_128", body)
        return base64.b64decode(r["audio_base64"]), words_from_alignment(r["alignment"])
    except RuntimeError as e:
        print(f"  with-timestamps failed ({str(e)[:120]}), falling back to plain tts", file=sys.stderr)
    req = urllib.request.Request(f"{API}/text-to-speech/{voice_id}?output_format=mp3_44100_128", data=json.dumps(body).encode(),
                                 headers={"xi-api-key": key, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read(), None
    except urllib.error.HTTPError as e:
        sys.exit(f"tts failed: {e.code} {e.read().decode()[:400]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario", nargs="?")
    ap.add_argument("--voices", action="store_true")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--model", default=None)
    ap.add_argument("--voice", default=None, help="override the scenario voice")
    args = ap.parse_args()
    key = load_env()
    if args.voices:
        for v in list_voices(key):
            labels = v.get("labels") or {}
            print(f"{v['voice_id']}  {v['name']}  [{v.get('category')}] {labels.get('use_case', '')}")
        return
    if not args.scenario:
        ap.error("scenario required")
    sc = scenario.parse(args.scenario)
    meta = sc["meta"]
    voice_id = resolve_voice(key, str(args.voice or meta.get("voice", "ninja")))
    model = args.model or meta.get("model") or os.environ.get("ELEVENLABS_MODEL", "eleven_v3")
    out_dir = os.path.join(ROOT, "vo", meta["name"])
    os.makedirs(out_dir, exist_ok=True)
    spoken = [b for b in sc["beats"] if b["vo"]]
    for i, b in enumerate(spoken):
        mp3 = os.path.join(out_dir, f"beat_{b['n']}.mp3")
        meta_path = os.path.join(out_dir, f"beat_{b['n']}.words.json")
        digest = hashlib.sha1(f"{voice_id}|{model}|{b['vo']}".encode()).hexdigest()
        if not args.force and os.path.exists(meta_path) and json.load(open(meta_path)).get("digest") == digest:
            print(f"beat {b['n']}: cached")
            continue
        prev = spoken[i - 1]["vo"] if i > 0 else None
        nxt = spoken[i + 1]["vo"] if i + 1 < len(spoken) else None
        print(f"beat {b['n']}: {b['vo']}")
        audio, words = synth(key, voice_id, model, b["vo"], prev, nxt)
        open(mp3, "wb").write(audio)
        dur = duration_of(mp3)
        if words is None:
            words = words_proportional(b["vo"], dur)
        json.dump({"text": b["vo"], "duration": dur, "words": words, "digest": digest, "voice_id": voice_id, "model": model},
                  open(meta_path, "w"), indent=1, ensure_ascii=False)
        print(f"  -> {mp3} ({dur:.2f}s, {len(words)} words)")


if __name__ == "__main__":
    main()
