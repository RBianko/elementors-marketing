---
name: m_flip_round_fifteen
voice: none
hook: number
angle: one still of a real round-15 board, rendered once per board for the flip in m_round_one_round_fifteen
mood: awe
promise: a real round-15 board, held still, framed on the board and the synergy tags
render: multi
seed: 12
round: 15
level: 7
refill_shop: true
gold: 24
roll: false
board: supabase
pick: 1785909172-ccd1ca98
stage: [3, 3]
min_units: 4
bench: []
stash: []
cursor_start: [475, 85]
---
1. idle 2.6 {focus: board, zoom: 0.9}

## Brief
- Template for the flip in `m_round_one_round_fifteen`; the board list, order and cut lengths live in that brief. Render once per id with `SHOT_BUILD=<id>`, which overrides `pick:`.
- Captions: none here; the base timeline carries them.
- Voice: none.
- Render: multi, `board: supabase`, the cursor parked at `cursor_start` for the whole beat so nothing moves but the idle animations.
- Level matches the board: 5 units render at level 7, 4 units at level 5, so the field cap equals the unit count. A higher level shows a red "5 / 6 placed" under the board (first render 2026-10-16); the render loop rewrites `level` in the harness JSON per id.
- Watch for: "field cap refused" in the log means `level:` is too low for that board.
