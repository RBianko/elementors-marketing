---
name: n_apply_loop
voice: none
hook: mechanic-as-hook
angle: dragging an element onto a creature is the core verb of the game; six 2★ applies back to back, each played to the end of its animation, loop forever
mood: curiosity -> rhythm -> trance
promise: a 2★ element flies onto a bare 2★ creature, gets sucked in, flashes and the creature turns elemental, six times in a row, and the last one cuts into the first drag with no seam
button: "ANY CREATURE."
render: plain
seed: 11
round: 8
level: 9
gold: 10
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "reptile", "element": "bare", "stars": 2}, {"slot": 1, "unit": "slime", "element": "bare", "stars": 2}, {"slot": 2, "unit": "insect", "element": "bare", "stars": 2}, {"slot": 3, "unit": "plant", "element": "bare", "stars": 2}, {"slot": 4, "unit": "ghost", "element": "bare", "stars": 2}, {"slot": 5, "unit": "dragon", "element": "bare", "stars": 2}]
bench: []
stash: [{"element": "fire", "stars": 2}, {"element": "ice", "stars": 2}, {"element": "wind", "stars": 2}, {"element": "water", "stars": 2}, {"element": "light", "stars": 2}, {"element": "venom", "stars": 2}]
cursor_start: [760, 520]
---
1. wander 0.5 r10; hover stash:0 0.5 {focus: board}
2. drag stash:0 -> board:0; wait 2.4 {at: impact:fire, punch, focus: board:0}
3. drag stash:1 -> board:1; wait 2.4 {at: impact:ice, punch, focus: board:1}
4. drag stash:2 -> board:2; wait 2.4 {at: impact:wind, punch, focus: board:2}
5. drag stash:3 -> board:5; wait 2.4 {at: impact:water, punch, focus: board:5}
6. drag stash:4 -> board:4; wait 2.4 {at: impact:light, punch, focus: board:4}
7. drag stash:5 -> board:3; wait 2.4 {at: impact:venom, punch, focus: board:3}
8. idle 0.6 {focus: board}

## Brief
- Angle: the apply as a satisfying loop. One verb, six elements, six 2★ creatures. Each shot runs from the element in flight through the suction, the impact flash and the creature settling into its elemental form, then cuts to the next element in flight; the venom shot cuts into the fire shot the same way, so the seam is invisible and the short replays.
- Hook: mechanic as hook, silent, the template of e. The first caption sits at 0:00 over the first element in flight. The caption sentence wraps around the seam and reads from any point.
- Emotion arc: curiosity, rhythm, trance.
- Proof frame: six `impact:<element>` markers, one per shot; the camera is tight on the target unit from the moment the element reaches it.
- Shot list: set after the render from the markers. Each shot is the source window [drag_start + about 0.4 s, end of the apply animation], zoom about 1.7; the camera opens on the element in flight (cursor track) and pans to the unit centre by the drop, then holds on the unit through the impact and the settle. The animation is never cut: a shot ends only once the creature stands still in its new form. Shot lengths rounded to whole beats of Action 3 Loop (150 BPM, 24 frames a beat) where the animation allows.
- Captions (silent, music under, y 0.72, the Poppins highlightPop style of `palmier_build.py`; one sentence that explains the mechanic and wraps around the seam): ROLL AN ELEMENT, (0-96, the die) · DROP IT ON / ANY CREATURE. (96-960, one caption on two lines; user call 2026-10-18: half a sentence held for seven seconds read wrong, so the 3-word rule gives way here). Over each apply shot the element's name sits at y 0.22 in its colour, popIn, the whole shot (user call 2026-10-18): WATER #4FB3FF · LIGHT #FFE36B · VENOM #8EE04A · FIRE #FF6A2B · ICE #A8E8FF · WIND #9FF0C8, Poppins-Bold 84, black outline 10; at 0.30 they covered the heads of the 2★ sprites.
- Button: ANY CREATURE. closes the sentence on the last settle; the loop restarts on the die throw and ROLL AN ELEMENT,.
- Audio: game audio at -4 dB, the whoosh, the suction and the impacts are the rhythm; Action 3 Loop under it at -2 dB, no fades (a fade breaks the loop).
- Render: plain, a new render on the current build (user call 2026-10-17: the e render showed old frames, the cut chopped the animation, and the loop should show 2★ units). Six different bare 2★ types so no three are identical (setup units merge), six 2★ elements in the stash (only a bare unit of the same star takes an element). `wait 2.4` after each drop leaves the full animation on tape; the drop lands about 1.1 s into the drag and the impact 0.48 s after the drop.
- Pairs (user call 2026-10-17): fire reptile, ice slime, wind insect, water dragon, light ghost, venom plant.
- Voice: none, the voice pass skipped (no lines).
- Alt hook (number, silent): ONE DRAG. · SIX ELEMENTS. · ANY CREATURE.; it swaps the first two captions, since the sentence is one unit.
- Length: 14.4 s with the full animations, longer than the 7-9 s of the backlog row; the user asked for the animation uncut.
- Critic (first version, edit-only from e): REVISE then SHIP after the pan from the element to the unit replaced a fixed tight crop and the hook labels were fixed. This rerender keeps both.
- Assumptions: reptile, slime, insect, plant, ghost and dragon have 2★ art for every demo element (they do at 1★, used in e). Level 9 gives the six field slots. Round 8 is a shop round with nothing scripted around it.
- Watch for: a refused drop (no `apply:<el>` marker before an `impact:`) means the star did not match; if a 2★ art is static or missing for one pair, swap the type with another for that element. If the animation still runs at the next drag_start, raise the `wait`.
- Render result 2026-10-17: all six drops applied (impacts fire 13.07, ice 17.25, wind 22.82, water 27.93, light 32.32, venom 37.25); the animation (flash, sparks, the unit settling elemental) runs about 1.2 s after the impact.
- Build result 2026-10-17: timeline `n_apply_loop 9x16` in `shorts/n_apply_loop/`, 960 frames (16.0 s, 10 bars, the music loops on a bar line). Opens on one die (user call: an element dice roll first, from an existing cut): `l_dice_decide` 6.0-7.6, the throw, the camera pushes from 1.6 to 2.7 on the left die, which lands water up (3080, 930). Then the six applies in the order water dragon, light ghost, venom plant, fire reptile, ice slime, wind insect, so the rolled water is the first element dropped. Each apply shot is 144 frames, from the element in flight (camera on the element, the cursor track, at the unit in 6-9 frames) to impact + 1.25 s when the sparks are gone. A second die part (the face flying into the stash) was tried and dropped: the face does not visibly travel and the stash sat under the caption. Not exported.
- Outro (user call 2026-10-18): from frame 936, in the wind shot's settle, a black layer fades to 70% over 30 frames, the Elementors logo from 951, the Steam icon and WISHLIST ON STEAM (Poppins-Bold 50, one line) from 981, all fade out over the last 30 frames while the black goes to 100% at 1116. The wind shot runs on under it (source to about 26.1 s). Captions end at 950. The music runs to 1116 with a 90-frame fade-out. The end card breaks the seamless loop and the no-plate rule of hooks.md on purpose, as in m. Total 1116 frames (18.6 s).
- Exported 2026-10-18: `exports/n_apply_loop.mp4`, 1080x1920, 18.6 s.
