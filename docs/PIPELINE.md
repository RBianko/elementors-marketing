# Elementors shorts pipeline

How a 9:16 short is produced from a written scenario. Two halves, two repos.

## Capture (lives in `/Users/a1/DEV/pwn-zz`)

- Harness: `tests/shot_movie.tscn` + `tools/shot_movie.sh`, driven by a scenario JSON in `tools/scenarios/shots/`. Run from the game repo:

  ```
  SHOT_MOVIE_ROOT=/Users/a1/DEV/elementors-marketing/renders tools/shot_movie.sh <scenario>
  ```
- Renders through Godot `--write-movie --fixed-fps 60`, deterministic. Viewport 1280x720, nearest-upscaled 3x to 3840x2160, H.264 CRF 10 + AAC.
- Warm-up: every element's ImpactFx/ElementFx plays under a black matte before the `warmup` marker. Everything before that marker is discarded in the edit.
- Fake cursor drives the real drag-and-drop: Bezier path, overshoot and settle, sub-pixel jitter, hover before pick-up and drop, wander/drift after the impact. DEBUG button hidden.
- Output per scenario in `renders/<scenario>/`:
  - `<scenario>.mp4`
  - `<scenario>.cursor.json`: `{fps, width, height, scale, frames:[{f,x,y,down}], markers:[{f,name}]}` in output pixels.
  - `frames/`: raw 1280x720 PNGs + `frame.wav`.
- Marker names: `warmup`, `drag_start:<element>`, `drop:<element>`, `apply:<element>`, `impact:<element>` (apply + suction, the big beat), `star_up`, `cascade_end`.
- Planned: board state from real player builds (Supabase, `tools/builds_*.py`) converted to a save for `SHOT_LOAD_SAVE`, random mid-game build + random slot + random element per short so no two shorts look alike.

## Edit (this repo)

- Editor: Palmier Pro via MCP (`palmier-pro`, http://127.0.0.1:19789/mcp). The app must be running before the Claude session starts, otherwise `/mcp` reconnect.
- Project: `palmier/ELEMS.palmier`, 60 fps. One timeline per short, 1080x1920. Media referenced by absolute path, so moving files breaks links.
- Tracks: Text (captions) on top, Gameplay, VO, Game (linked game audio).

### Timing rule

The impact lands right after the last word of the pre-impact VO phrase. Place the gameplay clip so that `impact` marker frame = end of VO part A + ~5 frames; VO part B starts ~12 frames after impact. Trim the clip start at the `warmup` marker; if the VO needs lead-in before the first clean frame, hold a nearest-upscaled still of that frame (`ffmpeg -vf scale=3840:2160:flags=neighbor`).

### Zoom

`tools/zoom_keys.py <cursor.json> --trim <warmup frame>` prints clip-relative `scale` and `position` rows for `set_keyframes`:

- base framing at 1.0 (height fill, centered between cursor start and target slot),
- follow the cursor at 1.45 from 40 frames after the first move until the drop (linear keys every 10 frames),
- punch to 1.95 on the impact, hold 36 frames, ease back to 1.45, slow drift to the end.

Keyframe frames are clip-relative in Palmier (0 = first frame of the clip). Position rows are the top-left corner in canvas units.

### Voiceover

ElevenLabs "Ninja - Engaging Sports Commentator" voice. The script contains an `(impact)` beat, which ElevenLabs renders as a knock. Find it on a spectrogram (broadband transient, no harmonics; local transcription mislabels it as a stretched word) and cut the file into part A (before) and part B (after):

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

a early fire on reptile (done, two cuts) · b synergy tier pop · c 1->2->3 star cascade · d wrong element then right one · e one reptile, all 13 elements, for a music-only cut · combat before/after · "pick the element" poll format.
