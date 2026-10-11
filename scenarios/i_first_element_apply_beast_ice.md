---
name: i_first_element_apply_beast_ice
voice: ninja
hook: fail-to-win
angle: the first element ever goes on the wrong unit and bounces off; the fallback target turns out to be the real play
mood: confidence -> shrug -> delight
promise: an ice die slides off a bare 2★ slime, lands on a lone 1★ beast instead and makes its crits freeze
button: "Slime didn't deserve it anyway."
render: plain
seed: 11
round: 3
level: 3
gold: 6
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "beast", "element": "bare", "stars": 1}, {"slot": 2, "unit": "slime", "element": "bare", "stars": 2}]
bench: []
stash: [{"element": "ice", "stars": 1}]
cursor_start: [960, 470]
---
1. wander 0.3 r10; hover stash:0 0.4; drag stash:0 -> board:2; wait 0.4 {focus: board:2, anchor: start} — "Ice on the big slime. Easy."
2. idle 0.5; hover board:2 0.6; wander 2.4 r8 {punch, focus: tooltip, zoom: 1.3} — "Oh. It needs two stars, like the slime."
3. hover stash:0 0.3 {focus: stash} — "Okay. Ice beast then."
4. drag stash:0 -> board:0; wait 0.5; idle 1.0; drift 30,140; hover board:0 0.6 {at: impact, punch, focus: board:0} — "Oh. He's COLD."
5. wander 2.4 r6 {punch, focus: tooltip, zoom: 1.45} — "Crits FREEZE them?"
6. drift 20,10; hover board:2 0.4; idle 1.8 {focus: board} — "Slime didn't deserve it anyway."

## Brief
- Angle: round 3, the player's first element. They aim it at the biggest unit, a bare 2★ slime, and it slides back to the stash: a 1★ element only goes on a 1★ body. The fallback, a lone bare beast up front, turns out better: Lone Hunter plus "crits freeze the target".
- Hook: fail-to-win. "Ice on the big slime. Easy." is said over a drag the viewer already sees going somewhere it will not stay.
- Promise: refused drop (red refused cursor, the die snaps back), then ice on the beast, impact FX, the tooltip shows "+30% phys damage when no ally in front" plus "Crits freeze the target for 1s".
- Emotion arc: confidence, a quick shrug, delight.
- Proof frame: three beats the camera works on. Beat 2 opens the slime's tooltip so the 2★ is on screen while the player reads the rule off it (no marker for a refused drop, lands on `beat:2`), beat 4 on `impact:ice` on board:0, beat 5 punches the freeze line in the tooltip.
- Button: "Slime didn't deserve it anyway." Smug cope, a callback to the bounce.
- Captions: BIG SLIME. EASY · NEEDS TWO STARS · ICE BEAST · HE'S COLD · CRITS FREEZE · DIDN'T DESERVE IT
- Alt hook (curiosity): "My first ice did something weird." 0:00 caption: FIRST ICE. WEIRD. Alt button: "Read the stars, kids."
- Render: plain. The refused drop is a harness drag onto an invalid target; no save, no seed hunt.
- Assumptions: application needs a star match (documentation.md v0.25), so 1★ ice on the bare 2★ slime is refused and the die returns to stash:0; the harness draws the refused cursor while the drag hovers an invalid target (`CursorSkin.is_refusing`). Beast at board:0 is front line with nothing in front, so Lone Hunter is live. Beast/ice has animated art (`beast_ice_1_frames.tres`); beast/fire is static, which is why the die is ice. Strings and `freeze_on_crit_duration=1.0` read from pwn-zz on 2026-10-11.
- Watch for: if the refused drop leaves the die anywhere but stash:0, beat 4 drags nothing; check the frame after beat 1. If an `impact:ice` marker appears in beat 1, the star rule changed and the slime took it.
