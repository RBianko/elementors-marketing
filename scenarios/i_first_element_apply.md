---
name: i_first_element_apply
voice: ninja
hook: curiosity
angle: the player knows elements go on creatures but has never done it; fire on a healing plant turns the heal into burn
mood: anticipation -> surprise -> delight -> greed
promise: fire dropped on a bare plant turns it into a fire plant, unlocks a bestiary entry and makes its regen pulse burn the enemy
button: "Okay. What does ice do. Somebody tell me."
render: plain
seed: 11
round: 3
level: 3
gold: 6
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "insect", "element": "bare", "stars": 1}, {"slot": 2, "unit": "plant", "element": "bare", "stars": 1}]
bench: []
stash: [{"element": "fire", "stars": 1}, {"element": "ice", "stars": 1}]
cursor_start: [960, 470]
---
1. wander 0.3 r10; hover stash:0 0.5 {focus: stash, anchor: start} — "So I rolled fire. Let's see."
2. drag stash:0 -> board:2; wait 0.5; idle 1.6 {at: impact, punch, focus: board:2} — "Ohhh. That's sick."
3. drift 40,150; wander 1.6 r10; hover board:2 0.5 {focus: board} — "Look. It's on fire."
4. wander 2.8 r6 {focus: tooltip, zoom: 1.3} — "Hold on. It still heals?"
5. wander 2.2 r6 {punch, focus: tooltip, zoom: 1.45} — "And the heal BURNS them??"
6. drift 20,10; hover board:0 0.4; wander 0.6 r8; hover stash:1 0.4; idle 1.4 {focus: stash} — "Okay. What does ice do. Somebody tell me."

## Brief
- Angle: round 3, the player knows elements merge into creatures but has never applied one. They rolled fire, drop it on the bare plant, and the element rewrites the plant's skill: a bestiary unlock and an orange bonus box under Vital Roots.
- Hook: curiosity. "So I rolled fire. Let's see." The player does not say where it goes; the cursor carries the die to the plant and the drop answers inside 3 s.
- Promise: fire on a bare plant, impact FX, "BESTIARY UNLOCKED · Fire Plant" toast, the tooltip shows the heal skill plus the new fire line.
- Emotion arc: anticipation, surprise, delight, greed.
- Proof frame: beat 2 on `impact:fire` on board:2 (about 2.5 s in, cold open). Beat 4 opens the tooltip on the skill box ("Same-line allies regen +1% HP/s"), beat 5 punches the bonus box: "Each regen pulse applies 100% of its amount as burn stacks to the primary enemy".
- Button: "Okay. What does ice do. Somebody tell me." The only chat address in the short; the cursor ends on the ice die, so the reply writes itself.
- Captions: ROLLED FIRE · SICK · ON FIRE · STILL HEALS · HEAL BURNS · WHAT DOES ICE
- Alt hook (reaction-first): "WAIT. Rewind. Watch the plant." 0:00 caption: WATCH THE PLANT. Alt button: "Every plant gets fire now."
- Alt hook (confession): "Three runs and I never put an element on anything." 0:00 caption: THREE RUNS. NEVER. Alt button: "Three runs. Wasted."
- Render: plain. Board, stash and the drag are all setup keys and harness actions; no offer, no save, no seed hunt.
- Assumptions: the harness clears the bestiary before the run (`_seed_run`), so the apply fires the unlock toast on every render; setup units do not go through the buy signal, so the toast fires only on the apply. The tooltip opens in the left rail on hover of a board unit, as in h_lucky_roll_three_star beat 6. Plant/fire has animated art (`plant_fire_1_sprite`). `regen_burn_pct=1.00` and the two tooltip strings were read from pwn-zz on 2026-10-11.
- Watch for: the toast sits at the top over the shop while beats 3-4 play, keep the camera on the board and the left rail; if the tooltip has no orange bonus box, the drop was refused (wrong star or the unit was not bare).
