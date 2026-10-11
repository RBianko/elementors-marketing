# elementors-marketing

Short-form video pipeline for Elementors. A short is written as a markdown scenario, rendered from the game by a deterministic Godot harness, voiced per beat with ElevenLabs, and assembled into a 9:16 timeline in Palmier Pro by the `/short` Claude Code skill.

## Layout

| Path | What |
|---|---|
| `scenarios/*.md` | Scenario per short: board setup in the frontmatter, numbered beats with actions and voice lines |
| `renders/<name>/` | Harness output: `<name>.mp4`, `<name>.cursor.json` (cursor track, markers with focus rects, fight track, source build), `plan.json` (edit plan) |
| `vo/<name>/` | One voice file per beat plus word timings |
| `palmier/` | Palmier Pro projects; `ELEMS.palmier` holds the shorts timelines |
| `tools/` | `scenario.py`, `tts.py`, `align.py`, `palmier_build.py` |
| `docs/PIPELINE.md` | The full contract between the harness and the edit, timing and camera rules |
| `.claude/skills/short/` | The `/short` skill |
| `voices.json` | ElevenLabs voice cache, maintained by `tts.py` |

Media, renders, voice files and Palmier media caches are not committed.

## Requirements

- Game repo at `/Users/a1/DEV/pwn-zz` with the capture harness (`tools/shot_movie.sh`).
- Palmier Pro running (MCP on `127.0.0.1:19789`).
- `ELEVENLABS_API_KEY` in `.env` (see `.env.example`). Library voices need a paid ElevenLabs plan over the API; premade voices work on the free plan.
- `ffmpeg`, Python 3.

## Usage

In Claude Code, from this directory:

```
/short a_early_fire_reptile          # build the short for scenarios/a_early_fire_reptile.md
/short rerender f_battle_summary     # force a new Godot render first
/short voices                        # list the account's ElevenLabs voices
```

By hand, the same steps:

```
python3 -I tools/scenario.py scenarios/<name>.md --harness > /Users/a1/DEV/pwn-zz/tools/scenarios/shots/<name>.json
(cd /Users/a1/DEV/pwn-zz && SHOT_MOVIE_ROOT=$PWD/renders tools/shot_movie.sh <name>)
python3 -I tools/tts.py scenarios/<name>.md
python3 -I tools/align.py scenarios/<name>.md
python3 -I tools/palmier_build.py renders/<name>/plan.json [--export exports/<name>.mp4]
```

## Scenario example

```md
---
name: g_player_board_apply
voice: ninja
board: supabase
stage: [2, 3]
pick: random
require_bare: true
stash: [{"element": "fire", "stars": 1}]
---
1. idle 2.2 {focus: board} — "Random board from a real player."
2. hover stash:0 0.5 — "Fire goes... here."
3. drag stash:0 -> board:bare; wait 0.5; idle 0.8 {at: impact, punch} — "Oh that's nasty."
4. hover board:best 1.2 {focus: board:best} — "Still not the best thing on this board though."
```

Beat options and actions are listed in `.claude/skills/short/SKILL.md`; the harness side is described in `docs/PIPELINE.md`.
