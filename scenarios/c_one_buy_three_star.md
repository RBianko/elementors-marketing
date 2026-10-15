---
name: c_one_buy_three_star
voice: ninja
hook: curiosity
angle: a plain bare reptile from the shop, one fire on it, and the whole reptile line collapses: the 1★ pair on the bench goes 2★ and the 2★ pair on the board goes 3★ in one drop
mood: tease -> want -> doubt -> disbelief -> hype -> smug
promise: the player buys a bare 1★ reptile, drops fire on it on the bench, and both merges fire in the same instant, ending on a 3★ fire reptile on the board
button: "One unit. One fire, and he's three star, man."
render: seed
seed: 34
round: 9
level: 8
gold: 14
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 1, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 2, "unit": "slime", "element": "ice", "stars": 2}, {"slot": 3, "unit": "plant", "element": "wind", "stars": 1}, {"slot": 4, "unit": "beast", "element": "ice", "stars": 1}]
bench: [{"unit": "reptile", "element": "fire", "stars": 1}, {"unit": "reptile", "element": "fire", "stars": 1}]
stash: [{"element": "fire", "stars": 1}]
cursor_start: [700, 520]
---
1. hover bench:0 0.4; hover bench:1 0.5 {focus: bench} — "One more, One more let's go."
2. hover node:%RerollButton 0.1; click node:%RerollButton; click node:%RerollButton; click node:%RerollButton; wait 0.2 {focus: shop} — "two gold. give me."
3. hover shop:0 0.1; wander 2.4 r12 {punch, lead: 25, focus: shop:0, zoom: 1.6} — "yeees, here we go, now watch."
4. click shop:0; drag bench:2 -> board:5 {focus: board:5} — "I have it, I have fire, watch"
5. drag stash:0 -> board:5; wait 1.3 {at: star_up, punch, lead: 20, focus: board:5, zoom: 1.6} — "Wait wait wait."
6. drift 60,-50; hover board:5 0.1; wander 3.4 r8 {at: cascade_end, punch, lead: 20, focus: board:5, zoom: 1.8} — "ohhhh Three? He's... he's three? right"
7. wander 1.9 r6 {focus: tooltip, zoom: 1.4} — "That's a boy. huuge stats."
8. wander 6.3 r10 {focus: board, align: left, zoom: 1.0} — "[laughs] One unit. One fire, and he's three star, man."

## Brief
- Angle: mid game, two 1★ fire reptiles on the bench and two 2★ on the board. The shop gives a plain bare reptile, the player buys it, moves it to the empty board slot 5, drops the one fire from the stash on it, and the fire 1★ completes the trio with the bench pair, whose 2★ completes the trio with the board pair; both promotions land on board:5. Revision 2026-10-14 (user): a bare buy plus a fire apply instead of the COPY card.
- Voice: lines rewritten by the user 2026-10-14 for a live read and recorded by hand in ElevenLabs (Lewis Moore), cut per beat from one file; they are anchors, no voice pass over them. Only fix: a space after the comma in line 1. Beats 6 and 8 got longer wanders for the longer reads (3.7 s and 5.8 s with the laugh).
- Pace: revision 2026-10-15 (user: "too slow"). Every beat is cut to its recorded line: three reroll clicks back to back, the buy and the move to the board under one line, reactions 0.3-0.4 s after the event (`lead: 20-25`) instead of 1 s. 38.5 s became 30.5 s; the recorded reads are about 20 s of it.
- Hook: curiosity gap with the stake first. "One more. Watch the bench." One more copy is wanted, the bench is where it happens.
- Emotion arc: tease, want, doubt (a bare one, no fire), disbelief, hype, smug.
- Proof frame: beat 2 is three quick rerolls under one line, two misses; beat 3 is a light punch on the reptile in shop:0 at about 8 s, a slow build on purpose: the two dead shops are the tension. Beat 5 punches `star_up` on board:5 after the fire drop; beat 6 punches `cascade_end` on board:5 with the 3★ badge, strong edge glow and shake, `lead: 90` so the two reactions do not overlap. On the 2026-10-10 render of the same chain with a board apply, both `star_up` markers landed on the apply frame and `impact:fire` 0.47 s after them.
- Button: "One unit. One fire, and he's three star, man." Callback to "I have fire" in beat 4.
- Captions: ONE MORE, · ONE MORE LET'S GO. · TWO GOLD. · GIVE ME. · YEEES, · HERE WE GO, · NOW WATCH. · I HAVE IT, · I HAVE FIRE, · WATCH · WAIT WAIT WAIT. · OHHHH THREE? · HE'S... · HE'S THREE? RIGHT · THAT'S A BOY. · HUUGE STATS. · ONE UNIT. · ONE FIRE, · AND HE'S THREE · STAR, MAN.
- Silent cut: ONE MORE. · WATCH THE BENCH. at 0:00, BARE ONE. on the card, ADD FIRE. on the drag, TWO STAR. on the bench pop, THREE STAR. on board:0 from `cascade_end`, ONE FIRE. · THREE STAR. over beat 8. Music still to be laid under it.
- Alt hook (reaction-first): "No. No way. Okay, watch the bench." 0:00 caption: NO WAY. Alt button: "One fire. That was one fire, chat."
- Alt hook (number): "Four gold and one fire. Watch." 0:00 caption: FOUR GOLD. Alt button: "Told you. One fire."
- Render: seed route, no `offer:`. Seed 34 at round 9, level 8: the setup shop is insect, slime with no bonus card, the first reroll shows beast, plant, ghost, demon, the second plant, slime, slime, beast, the third reptile, insect, ghost, ghost; the bonus slot stays empty throughout. Seed 28 was dropped: its setup shop showed a TWO STAR! bonus card that the player rerolled away. The bare reptile is an ordinary roll in shop:0, so the short is plain gameplay. Found with a headless scan of seeds 1-500 (29 seeds qualify) that replays the harness setup and calls the reroll (`RunRNG.shop_rng(master_seed, round, shop_refresh_idx)`), checked against the seed 29 render. Revision 2026-10-14 (user): the reptile shows on the third reroll, not the first, and never in the bonus slot.
- Assumptions: gold 14 covers three rerolls (6) and the card (4); the buy lands on bench:2 and does not merge, because nothing else is a bare reptile; level 8 for the six-unit field cap, so board:5 takes it. The merge result lands on the unit the element was applied to: the first try applied on bench:2 and the 3★ ended on the bench at the bottom of the screen (2026-10-14), so the apply now happens on board:5. Both `star_up` markers land about 0.6 s after `impact:fire`.
- Camera: beat 8 is wander-only with `focus: board, align: left, zoom: 1.0`: the left half of the board in frame, the 3★ on board:5 whole. At zoom 1.25 the board region cut the 3★ at one edge or the other, centered or aligned (2026-10-15). The beat's focus rect is written into the `beat:N` marker at render time, so a focus change in the scenario needs a rerender; a zoom or align change does not.
- Material for k: beats 5-6 are the cascade punch for the "fifteen seconds" pitch cut.
- Watch for: the shop-odds tooltip on the reroll hover closes on the move to shop:0; a "Bestiary unlocked" toast may cover the shop after the 3★. If `star_up` is missing, the apply was refused on the bench or the buy merged early; check that board:5 holds the bare reptile after beat 4. Check the cursor json for frame stalls before aligning (`docs/PIPELINE.md`).
