---
name: h_lucky_roll_three_star__contrarian
base: h_lucky_roll_three_star
voice: ninja
hook: contrarian
angle: the one card you were missing shows up in the bonus slot at round 14
mood: want -> disbelief -> hype -> smug
promise: a 2★ fire reptile lands in the lucky slot on a reroll and the board goes 3★ on the spot
button: "Sell it, they said."
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
1. idle 0.6; hover board:0 0.8; idle 0.6 {focus: board:0} — "Chat said sell the second reptile."
2. hover node:%RerollButton 0.4; click node:%RerollButton; wait 0.7 {focus: shop} — "Two gold. Come on."
3. hover shop:4 0.1; wander 2.0 r40; idle 0.2 {punch, focus: shop:4, zoom: 2.0} — "...wait."
4. click shop:4; wait 0.5; idle 0.8 {at: star_up, punch, focus: board:0} — "YESSSS."
5. hover board:0 0.2; wander 0.5 r8 {focus: board:0} — "Three star. THREE."
6. wander 2.2 r6 {focus: tooltip, zoom: 1.4} — "Look at those stats."
7. drift 30,20; hover board:2 0.4; idle 2.2 {focus: board} — "Sell it, they said."

## Brief
- Variant of h_lucky_roll_three_star: same beats, same render. Changes only line 1, the 0:00 caption and the button.
- Hook: contrarian. Chat's advice is the stake, the lucky slot proves chat wrong.
- Captions: SELL IT, CHAT · COME ON · WAIT · YESSSS · THREE · THOSE STATS · THEY SAID
- Button: "Sell it, they said." Callback to the hook.
