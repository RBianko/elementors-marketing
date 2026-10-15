# Elementors shorts pipeline

How a 9:16 short is produced from a written scenario. Two halves, two repos.

## Capture (lives in `/Users/a1/DEV/pwn-zz`)

- Harness: `tests/shot_movie.tscn` + `tools/shot_movie.sh`, driven by a scenario JSON in `tools/scenarios/shots/`. Run from the game repo:

  ```
  SHOT_MOVIE_ROOT=/Users/a1/DEV/elementors-marketing/renders tools/shot_movie.sh <scenario>
  ```
- Renders through Godot `--write-movie --fixed-fps 60`, deterministic. Viewport 1280x720, nearest-upscaled 3x to 3840x2160, H.264 CRF 10 + AAC.
- Run renders under `caffeinate -dimsu` (before `tools/shot_movie.sh`): a render that ran while the Mac slept came out with 5194 frozen frames (2026-10-15).
- A regular shop card (not the bonus slot) cannot be armed; find a seed instead. `tools/shop_scan.gd` replays the harness setup per seed and prints the setup shop and each reroll, matching the render (checked on seeds 29 and 34):

  ```
  cd /Users/a1/DEV/pwn-zz && SCAN_FROM=1 SCAN_TO=500 SCAN_ROUND=9 SCAN_LEVEL=8 SCAN_REROLLS=3 \
    /Applications/Godot.app/Contents/MacOS/Godot --headless --path . -s /Users/a1/DEV/elementors-marketing/tools/shop_scan.gd
  ```

  The shop depends only on seed, round, level and the reroll count, not on the board. Check the setup shop (`s0`) too: it is rolled before the level is raised and may carry a bonus card.
- The merge result lands on the unit the element was applied to, so the apply target decides where a cascade ends (bench or board).
- After a merge under a parked cursor the tooltip does not open: move the cursor off and back (`drift`, then `hover`).
- The focus rect of a beat is written into its `beat:N` marker at render time; a `focus:` change needs a rerender, a `zoom:` or `align:` change does not.
- A render whose window stops redrawing (occluded, another Godot run on the machine) keeps writing PNGs while `Engine.get_frames_drawn()` stands still: the cursor track repeats one `f` for hundreds of entries, the mp4 holds a frozen frame for seconds and every marker after the stall is off by that many frames. Check `len(frames) == max(f) + 1` in the cursor json before aligning; if not, rerender (c_one_buy_three_star, 2026-10-14: 631 copies of frame 791, clean on the second run).
- Warm-up: every element's ImpactFx/ElementFx plays under a black matte before the `warmup` marker. Everything before that marker is discarded in the edit.
- Fake cursor drives the real drag-and-drop: Bezier path, overshoot and settle, sub-pixel jitter, hover before pick-up and drop, wander/drift after the impact. DEBUG button hidden. Injected mouse events carry device id 77; every other mouse event (the OS mouse crossing the render window) is marked handled before the GUI sees it, so moving the real mouse during a render no longer turns cards or swaps hover. Code that polls the cursor (shop card turn, drag card, drag trail, floating tooltip, forest parallax, round gold drift, scout card) reads it through `ui/components/pointer.gd` in pwn-zz: `Viewport.get_mouse_position()` returns the OS cursor and ignores injected motion, so without the seam a hovered shop card froze at its first-hover tilt. The harness sets `Pointer.override` every frame.
- Output per scenario in `renders/<scenario>/`:
  - `<scenario>.mp4`
  - `<scenario>.cursor.json`: `{fps, width, height, scale, frames:[{f,x,y,down}], markers:[{f,name}]}` in output pixels.
  - `frames/`: raw 1280x720 PNGs + `frame.wav`.
- Marker names: `warmup`, `beat:N` (one per scenario beat, from `mark` actions), `drag_start:<element>`, `drop:<element>`, `apply:<element>`, `impact:<element>` (apply + suction, the big beat), `star_up`, `cascade_end`, `battle_start`, `battle_open_end`, `battle_end`, `summary`, `summary:damage`, `summary:synergies`, `summary:unit:N`, `summary:dps:N`, `summary:kills:N`, `summary:focus`. Every marker except `warmup` carries `focus: {x, y, w, h}` in output pixels.
- Actions: `wander`, `hover`, `click`, `drag`, `wait`, `idle`, `drift`, `mark`, `battle` (clicks BATTLE for real, `speed` sets the fight's time scale, `open=N` keeps the first N s at speed 1), `summary` (opens the recap, marks every row).
- Shop card override: `"offer": {"kind": "echo_2star", "unit": "reptile", "element": "fire", "stars": 2}` → `RunState.debug_next_offer`, consumed by the next refresh.
- Real player boards: `"board": "supabase"` with `stage`, `pick`, `require_bare`, `min_units`, `exclude`; snapshots cached in `pwn-zz/build/player_snapshots.json` (5016 demo boards, stages 1–3, refetched 2026-10-11). `SHOT_BUILD=<id>` reproduces a short; `source_build` is written into cursor.json.

## Edit (this repo)

- Editor: Palmier Pro via MCP (`palmier-pro`, http://127.0.0.1:19789/mcp). The app must be running before the Claude session starts, otherwise `/mcp` reconnect.
- Project: `palmier/ELEMS.palmier`, 60 fps. One timeline per short, 1080x1920. Media referenced by absolute path, so moving files breaks links.
- Tracks: Text (captions) on top, Gameplay, VO, Game (linked game audio).
- When the `palmier-pro` MCP server did not connect in the session, `tools/palmier_build.py`'s `Palmier` class drives the same endpoint over HTTP from a script (`p.call(tool, **args)`, raw images from `inspect_timeline` through `p._post`), so verification and small fixes do not need `/mcp`.
- Silent cut: `create_timeline` with `from` set to the voiced timeline and the name `<name> silent 9x16`, `manage_tracks` remove the VO track, `remove_clips` on every text clip, `add_texts` with the brief's silent captions on the marker frames (style, highlight and y from `palmier_build.py`), `manage_tracks` set the caption track's name back to Captions. The copy keeps the gameplay clip, its keyframes and the linked game audio.

### Timing rule

The impact lands right after the last word of the pre-impact VO phrase. Place the gameplay clip so that `impact` marker frame = end of VO part A + ~5 frames; VO part B starts ~60 frames (1 s) after impact, so the reaction follows the event instead of firing with it. Trim the clip start at the `warmup` marker; if the VO needs lead-in before the first clean frame, hold a nearest-upscaled still of that frame (`ffmpeg -vf scale=3840:2160:flags=neighbor`).

### Writing (`/scenario` skill)

- Turns a raw moment ("late game, lucky roll, merge to 3★") into `scenarios/<name>.md`: hook type, beats the harness can film, streamer voice lines, captions, a `## Brief` block with the angle, emotion arc, proof frame, button, alt hook, render route and assumptions. References: `.claude/skills/scenario/references/game.md` (mechanics, harness limits) and `hooks.md` (hook taxonomy, structure, voice, captions), sources in `docs/SHORTS_RESEARCH.md`.
- Frontmatter keys `hook`, `angle`, `mood`, `promise`, `button`, `render` are edit-side and never reach the harness. `save:` is resolved to an absolute path for the harness.
- `tools/scenario_lint.py` — pre-render estimate: voice length vs action time per beat, first punch second, total length, target and option validity. Opening line may lead in on a hold still; a line may run over the silent beats after it.
- Shop cards: `offer: {kind, unit, element, stars}` arms `RunState.debug_next_offer` in the game; the next refresh the scenario triggers (a reroll click) places exactly that card in the bonus slot with the reveal FX. The same override sits in the game's debug menu ("Next offer / Arm"). Fallbacks: `save:` with a hand-written save, or a seed search.
- A/B variants: `scenarios/<name>__<hooktype>.md` with `base: <name>`, same beats, different first line, 0:00 caption and button. `align.py` reads the base render and writes the variant's own `renders/<variant>/plan.json`; `/short` never renders a variant. The lint refuses a variant whose beats drift from the base.
- Voice pass: after the lint, the `streamer-voice` agent (`.claude/agents/streamer-voice.md`) proposes two or three streamer readings per line (repeats, restarts, stops, fillers, chat address, hedged flexes, the autobattler lexicon) with a pick, ElevenLabs tags and caption chunks, inside the beat's time budget; `/scenario` applies the picks. Reference `.claude/skills/scenario/references/voice.md`, evidence `docs/VOICE_REFERENCE_CLIPS.md`. `/scenario voice <name>` reruns only this pass.
- Then `/scenario` runs the `shorts-critic` agent (`.claude/agents/shorts-critic.md`): seven PASS/FAIL checks and up to three rewrites, two rounds at most.

### Tools (`/short` skill)

- `tools/scenario.py` — parses `scenarios/<name>.md` (frontmatter + numbered beats) and emits the harness JSON.
- `tools/tts.py` — one ElevenLabs file per beat with word timings (`vo/<name>/beat_<n>.mp3` + `.words.json`), voice cache in `voices.json`, key from `.env`. Library voices over the API need a paid plan; premade voices work on free.
- `tools/align.py` — render markers + voice durations → `renders/<name>/plan.json`: clip trim at `warmup`, voice placement (line before a punch ends 5 frames before it, a punch line starts 60 frames (1 s) after), hold still when the first line needs lead-in, camera keyframes (follow cursor 1.45x, punch 1.95x, rest 1.4x; a beat with only `wander` and a `focus:` frames that region instead of following, e.g. `focus: tooltip` while the cursor wanders on a board unit; the segment before a punch ends 20 frames early so the camera glides to the punch target in one move; after a punch the camera holds the punch frame until the cursor has moved and settled, then follows, so a cursor parked on the shop after the buy does not drag the camera up and back), captions in ≤3-word chunks.
- `tools/palmier_build.py` — builds the timeline in Palmier over the MCP HTTP endpoint and can export.

Keyframe frames are clip-relative in Palmier (0 = first frame of the clip). Position rows are the top-left corner in canvas units; scale rows are the clip's normalized width/height, 1.0 = canvas axis.

### Voiceover

ElevenLabs "Ninja - Engaging Sports Commentator" voice (library voice, paid plan over the API; `liam` is the premade fallback). eleven_v3 reads an all-caps word as an acronym, so `tts.py` sends "THREE" as "Three" and keeps the caps only in the caption words. v3 audio tags (`[laughs]`, `[happy gasp]`, the list in `voice.md`) go first in a line; `tts.py` sends them to the voice and drops them from the caption words, the lint adds 0.4 s per tag and flags tags outside the list. The script contains an `(impact)` beat, which ElevenLabs renders as a knock. Find it on a spectrogram (broadband transient, no harmonics; local transcription mislabels it as a stretched word) and cut the file into part A (before) and part B (after):

```
ffmpeg -i in.mp3 -af "atrim=start=S:end=E,asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st=(E-S-0.03):d=0.03" out.wav
```

`atrim` + `asetpts` is mandatory: with `-ss` after `-i` the fade-out start is measured from the original file and the clip comes out silent.

### Captions

TikTok style: Poppins-Bold, 60 pt, uppercase, white, black outline 8, soft shadow, `highlightPop` with `#FFE600`, centered at y 0.72, max 3 words per caption. Palmier's local transcription handles sentences but misses interjections ("OH. Okay okay okay."), add those as text clips by hand from the VO envelope.

### Style decisions

- Shorts should read as stream clips: no end card, no "free demo" plate, no AI streamer webcam.
- Hook is creature x element apply; the impact must happen inside the first 2.5-4.5 s.
- Two VO variants per clip are cheap (same timeline duplicated), use them for A/B.

## Scenario ideas

The ranked backlog with the evidence behind it is `docs/SCENARIO_BACKLOG.md`. The original list: a early fire on reptile (done, two cuts) · b synergy tier pop · c 1->2->3 star cascade · d wrong element then right one · e one reptile, all 13 elements, for a music-only cut · f battle recap number · g real player board · h lucky roll into 3★ via `offer:` and a reroll · combat before/after · "pick the element" poll format.
