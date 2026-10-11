---
name: h_lucky_roll_three_star
voice: ninja
hook: need-first
angle: the one card you were missing shows up in the bonus slot at round 14
mood: want -> disbelief -> hype -> smug
promise: a 2★ fire reptile lands in the lucky slot on a reroll and the board goes 3★ on the spot
button: "One more reptile. My best board so far."
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
3. hover shop:4 0.8; idle 0.3 {punch, focus: shop:4, zoom: 2.0} — "...wait."
4. click shop:4; wait 0.5; idle 1.2 {at: star_up, punch, focus: board:0} — "YESSSS."
5. hover board:0 1.2; idle 0.8 {focus: board:0} — "Three star. THREE."
6. drift 30,20; hover board:2 0.6; idle 2.0 {focus: board} — "One more reptile. My best board so far."

## Brief
- Angle: late game, the player is one copy short of a 3★ carry and the lucky slot hands it over on a two-gold reroll.
- Hook: need-first. The first line names the one missing piece, the shop answers it inside 7 s. "Round fourteen" was cut: the label is on screen and the line overran the beat.
- Emotion arc: want, disbelief, hype, smug.
- Proof frame: two punches. Beat 3 on the rainbow reveal in shop:4, beat 4 on the `star_up` marker with the 3★ sparkle and edge glow on board:0.
- Button: "One more reptile. My best board so far." Callback to the hook, then the flex the user asked for.
- Captions: ONE MORE · COME ON · WAIT · YESSSS · THREE · BEST BOARD
- Alt hook (contrarian): "Chat said sell the second reptile. Chat." 0:00 caption: SELL IT, CHAT. Alt button: "Sell it, they said."
- Alt hook (number): "Twenty percent. That's the odds on this slot." 0:00 caption: TWENTY PERCENT. Alt button: "Twenty percent. Sure."
- Render: offer route. `offer:` arms the bonus slot, the reroll click in beat 2 places the card with the full reveal FX. No save file, no seed hunt.
- Verified on the 2026-10-11 render: the echo offer costs 17 gold, the reroll 2, gold 24 leaves 5; the buy merges board:0 + bench:0 + the card and the 3★ lands on board:0 (board-first, lowest slot). Beast is ice, not fire, because beast/fire has static art.
- Watch for: the shop-odds tooltip opens while the cursor sits on the reroll button and closes on the move to shop:4; a "Bestiary unlocked" toast covers the top of the shop for a moment after the 3★, keep the camera on the board there.
- Critic: round 1 REVISE on proof line, button and alt captions; applied. The proposed button "One more reptile, I said. One." was refused because "my best board so far" is the user's anchor line; the callback was added in front of it instead.
