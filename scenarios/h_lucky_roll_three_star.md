---
name: h_lucky_roll_three_star
voice: ninja
hook: need-first
angle: the one card you were missing shows up in the bonus slot at round 14
mood: want -> disbelief -> hype -> smug
promise: a 2★ fire reptile lands in the lucky slot on a reroll and the board goes 3★ on the spot
button: "This board is INSANE man."
render: offer
seed: 83
round: 14
level: 7
gold: 24
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 1, "unit": "slime", "element": "ice", "stars": 2}, {"slot": 2, "unit": "insect", "element": "fire", "stars": 2}, {"slot": 3, "unit": "plant", "element": "wind", "stars": 1}, {"slot": 4, "unit": "beast", "element": "ice", "stars": 1}]
bench: [{"unit": "reptile", "element": "fire", "stars": 2}]
stash: []
offer: {"kind": "echo_2star", "unit": "reptile", "element": "fire", "stars": 2}
cursor_start: [700, 520]
---
1. idle 0.6; hover board:0 0.8; idle 0.6 {focus: board:0} — "I need one more fire reptile."
2. hover node:%RerollButton 0.4; click node:%RerollButton; wait 0.7 {focus: shop} — "Two gold. Come on."
3. hover shop:4 0.1; wander 2.0 r40; idle 0.2 {punch, focus: shop:4, zoom: 2.0} — "...wait."
4. click shop:4; wait 0.5; idle 0.8 {at: star_up, punch, focus: board:0} — "YESSSS."
5. hover board:0 0.2; wander 0.5 r8 {focus: board:0} — "Three star. THREE."
6. wander 2.2 r6 {focus: tooltip, zoom: 1.4} — "Look at those stats."
7. drift 30,20; hover board:2 0.4; idle 2.2 {focus: board} — "This board is INSANE man."

## Brief
- Angle: late game, the player is one copy short of a 3★ carry and the lucky slot hands it over on a two-gold reroll.
- Hook: need-first. The first line names the one missing piece, the shop answers it inside 7 s. "Round fourteen" was cut: the label is on screen and the line overran the beat.
- Emotion arc: want, disbelief, hype, smug.
- Proof frame: two punches. Beat 3 on the rainbow reveal in shop:4, beat 4 on the `star_up` marker with the 3★ sparkle and edge glow on board:0. Beat 6 holds the cursor on the 3★ so the left-rail tooltip stays open and frames it: name, 3★, HP, ATK, the passive.
- Cursor: on the shop card and on the 3★ the cursor wanders (r12 / r8) instead of freezing on a hover hold; a frozen cursor read as a screenshot in the 2026-10-11 cut.
- Button: "This board is INSANE man." The flex, said over the whole board.
- Captions: ONE MORE · COME ON · WAIT · YESSSS · THREE · THOSE STATS · INSANE
- Alt hook (contrarian): "Chat said sell the second reptile. Chat." 0:00 caption: SELL IT, CHAT. Alt button: "Sell it, they said."
- Alt hook (number): "Twenty percent. That's the odds on this slot." 0:00 caption: TWENTY PERCENT. Alt button: "Twenty percent. Sure."
- Render: offer route. `offer:` arms the bonus slot, the reroll click in beat 2 places the card with the full reveal FX. No save file, no seed hunt.
- Verified on the 2026-10-11 render: the echo offer costs 17 gold, the reroll 2, gold 24 leaves 5; the buy merges board:0 + bench:0 + the card and the 3★ lands on board:0 (board-first, lowest slot). Beast is ice, not fire, because beast/fire has static art.
- Watch for: the shop-odds tooltip opens while the cursor sits on the reroll button and closes on the move to shop:4; a "Bestiary unlocked" toast covers the top of the shop for a moment after the 3★, keep the camera on the board there.
- Revision 2026-10-11 (user): wandering cursor on the shop card and the 3★, a tooltip beat after the 3★, button changed from "One more reptile. My best board so far." to "This board is INSANE man."
