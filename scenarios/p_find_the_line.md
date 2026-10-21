---
name: p_find_the_line
voice: none
camera: wide
hook: challenge
angle: a mid-game board held still as a puzzle: one drag of the right element onto the right bare unit chains two merges into a 3★, and the viewer gets three seconds to find it
mood: challenge -> suspense -> payoff -> smug
promise: the board holds still for three seconds, then the fire goes onto the bare reptile, the three fire reptiles merge into a 2★ and the three 2★ merge into a 3★ on the spot
button: "GOT IT?"
render: plain
seed: 11
round: 9
level: 7
gold: 6
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 1, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 2, "unit": "slime", "element": "ice", "stars": 2}, {"slot": 3, "unit": "insect", "element": "bare", "stars": 1}, {"slot": 4, "unit": "reptile", "element": "bare", "stars": 1}]
bench: [{"unit": "reptile", "element": "fire", "stars": 1}, {"unit": "reptile", "element": "fire", "stars": 1}]
stash: [{"element": "fire", "stars": 1}, {"element": "ice", "stars": 1}, {"element": "wind", "stars": 1}]
cursor_start: [1180, 640]
---
1. idle 3.2 {focus: board, zoom: 0.5}
2. hover stash:1 0.5; hover stash:2 0.4; hover stash:0 0.5 {focus: stash, zoom: 1.4}
3. drag stash:0 -> board:4; wait 1.6 {at: star_up, punch, focus: board:4, zoom: 1.8}
4. wander 1.4 r6 {at: cascade_end, punch, focus: board:4, zoom: 2.0}
5. drift -60,40; wander 2.4 r10 {focus: board:4, zoom: 1.4}

## Brief
- Angle: the challenge template ("find the line here, I'll wait") as a silent cut. The board is a real-looking round 9: two fire reptile 2★, an ice slime, a bare insect and a bare reptile on the field, two fire reptile 1★ on the bench, fire, ice and wind in the stash. Only one drag makes a 3★: fire onto the bare reptile, which completes the 1★ fire trio (bench pair) into a 2★, which completes the 2★ trio (board pair) into a 3★, both in one pass. The cut gives the viewer three seconds, hesitates over the stash (ice, wind, then fire) and pays off.
- Hook: challenge, silent. 0:00 FIND THE 3★ over the still board in the wide frame, then 3 · 2 · 1 counting down over the hold. The still is the hook: the viewer's own search is the retention.
- Emotion arc: challenge, suspense (the cursor weighing the three elements), payoff on the cascade, smug.
- Proof frame: beat 3 punches the first `star_up` on board:4; beat 4 punches `cascade_end` with the 3★ badge, strong edge glow and shake, zoom 2.0.
- No fake drop: the harness `drag` always releases on its target (`_drag` in `tests/shot_movie.gd` has no waypoint), so a feint over the insect would really apply the fire there and kill the cascade. The hesitation lives in the stash hover instead.
- Captions (silent, music under, y 0.72, no trailing periods): FIND THE 3★ (0:00) · 3 · 2 · 1 (one per second over the hold) · ICE? · WIND? · FIRE (beat 2, over each hover, FIRE in its colour) · BARE ONE (beat 3, the drop) · 2★ (first star_up) · 3★ (cascade_end) · GOT IT? held to the end over the 3★ (beat 5 stays on board:4).
- Button: GOT IT? held over the 3★, the silent-cut ending and a reply invite ("I got it in one").
- Voice: none. Silent cut only.
- Alt hook (number, silent): 0:00 ONE DRAG. 3★ over the still; the button WHAT'S THE DRAG? swaps for GOT IT?
- Render: plain, no shop, no seed hunt, no dice throw (`roll: true` rolls at setup and `stash:` replaces the faces). `camera: wide` so the still shows the board, the bench and the stash in one frame; zoom per beat in wide units. Gold 6 so nothing on screen suggests a buy.
- Assumptions: the merge lands on the unit the element is applied to (c, 2026-10-14), so the 3★ ends on board:4. Setup units do not merge: the two fire 1★ reptiles are two, the fire 2★ reptiles are two, the bare 1★ reptile does not match the fire ones. Level 7 gives five field slots. The bare insect is a decoy only on screen; nothing is dropped on it.
- Critic (round 1, REVISE): ON THE BARE ONE was four words and an explanation, now BARE ONE; beat 5 stays on the 3★ at zoom 1.4 instead of pulling back wide. Round 2: SHIP; check at render that the star badges read in the zoom 0.5 still, otherwise there is no puzzle.
- Watch for: a missing second `star_up` or `cascade_end` means a merge did not chain; check that the bench pair and the board pair are both fire. A "Bestiary unlocked" toast is off by default.
- Render result 2026-10-21 (pwn-zz main): fire on board:4, both `star_up` on the same frame (the cascade in one pass), `cascade_end` 1 s later; the 3★ ends on board:4.
- Build result 2026-10-21: timeline `p_find_the_line 9x16`, 803 frames (13.4 s), no cuts. The wide still (zoom 0.5) was unreadable as the critic feared, so the camera over the still is set by hand as a tour: the board with the fire 2★ pair and the bare 1★ (0-70, scale 3.16) → the bench fire 1★ pair (95-140, zoom 1.4, framed low with the backdrop under it) → the stash (172 on). The drag is followed by hand from the stash to board:4. Countdown 3 · 2 · 1 at y 0.4 so it does not cover the units. Audio: game audio only; with no cuts its round music runs without seams. A rerun of align.py or palmier_build.py drops the hand camera.
- Exported 2026-10-21: `exports/p_find_the_line.mp4`, 1080x1920, 13.4 s, game audio.
