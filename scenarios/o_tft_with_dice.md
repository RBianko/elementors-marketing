---
name: o_tft_with_dice
voice: none
hook: contrarian
angle: it plays like TFT until the third copy lands and nothing merges; the missing piece is an element, and the element comes from a die
mood: recognition -> doubt -> suspense -> payoff
promise: the player rerolls, buys the third reptile like in any autobattler, nothing merges because it is bare, one die is thrown, fire lands, and the fire drop merges the three into a 2★ fire reptile
button: "TFT WITH DICE"
render: seed
seed: 8
round: 4
level: 3
gold: 10
roll: false
dice: ["fire", "fire", "fire", "fire", "fire", "fire", "fire", "fire", "ice", "wind", "water", "venom"]
board: [{"slot": 0, "unit": "reptile", "element": "fire", "stars": 1}, {"slot": 1, "unit": "reptile", "element": "fire", "stars": 1}]
bench: []
stash: []
cursor_start: [700, 300]
---
1. hover node:%RerollButton 0.3; click node:%RerollButton; wait 0.8 {focus: shop}
2. hover shop:0 0.5; click shop:0; wait 0.6 {focus: shop:0}
3. drag bench:0 -> board:2; wait 1.4 {focus: board}
4. hover node:%RollButton 0.4; click node:%RollButton; mark name=throw focus=dice; wait 2.6 {at: throw, punch, focus: dice}
5. hover stash:0 0.3; drag stash:0 -> board:2; wait 1.6 {at: star_up, punch, focus: board:2, zoom: 1.8}
6. drift 40,-30; wander 2.4 r10; idle 0.6 {focus: board, zoom: 1.0}

## Brief
- Angle: the comparison template (PACS) turned into a silent mechanic cut in the e mould, per the first results. The first three beats are the autobattler every viewer knows: reroll, buy the third copy, put it on the board. In TFT that is a merge; here nothing happens, because the new reptile is bare and the two on the board are fire. The die is the missing piece: one throw, fire on top, the drop, and the three merge into a 2★ fire reptile. The difference from TFT is shown, not said.
- Hook: contrarian, silent (the comparison template). 0:00 JUST TFT, RIGHT? over the reroll: the recognition as a doubt, the stake is whether the third copy merges the way it does in TFT; the "with dice" half is held back for the turn at the throw. The backlog line "This is just TFT with dice, chat." is a streamer line; as copy it would read as a tagline, so the cut splits it into a setup caption and a payoff caption.
- Emotion arc: recognition, doubt (no merge), suspense on the throw, payoff on the merge.
- Proof frame: beat 4 punches the `throw` mark on the dice table; beat 5 punches `star_up` on board:2 (2★ sparkle, medium edge glow), zoom 1.8. The no-merge moment in beat 3 is a hold of 1.4 s on three reptiles that stay apart.
- Captions (silent, music under, y 0.72, no trailing periods): JUST TFT, RIGHT? (0:00, beat 1) · REROLL (on the click) · THIRD ONE... (beat 2) · NO MERGE? (beat 3, held up to the throw) · FROM A DIE (beat 4, over the throw) · FIRE (in the fire colour #FF6A2B, on the landing) · STAR UP (beat 5, on `star_up`) · TFT WITH DICE (beat 6) · WHICH ELEMENT NEXT? held to the end (silent cuts end on the held question).
- Button: TFT WITH DICE, the comparison closed only once the dice did the merge; then the held question.
- Voice: none. Silent cut only, the shape that broke out (e silent, 2026-10-18). A voiced cut on the same render later if wanted: "Okay. Reroll... reptile. That's three." · "Wait, no merge?" · "Oh, it needs fire." · "Come on, fire..." · "FIRE. Two star." · "It's just TFT with dice, chat."
- Alt hook (curiosity, silent): same beats and captions, the 0:00 caption becomes BUY. MERGE? over the reroll (REROLL on the click stays), and the button NOT TFT, DICE replaces TFT WITH DICE before the held WHICH ELEMENT NEXT?
- Render: seed route. Seed 8 (seed 2 threw water, no merge), round 4, level 3 (two shop slots, field cap 3): the setup shop is plant, slime; the first reroll gives a bare reptile in shop:0 and an insect, no bonus card in either (`tools/shop_scan.gd`, rounds 4, level 3, seeds 1-300; other seeds with a reptile in shop:0 on the first reroll: 8, 12, 19, 24, 27, 29, 48, 64).
- Dice: a fire-heavy die like the Burning Aggression preset, eight chosen fire faces plus four others (ice, wind, water, venom), so the cut stays a legal build. Round 4 throws one die, the first roll of the round is free. The face is physics, seeded from `seed:`: two in three it lands fire.
- Assumptions: gold 10 covers the reroll (2) and the reptile (4). The buy lands on bench:0 and does not merge: the board reptiles carry fire, the bought one is bare. The fire 1★ face lands in stash:0 and applies on the bare 1★ on board:2; the three fire 1★ reptiles merge into a 2★ that stays on board:2 (the merge lands on the apply target). Three fire reptiles light Fire 3 in the synergy rail, a bonus on screen.
- Critic (round 1, REVISE): hook THIS IS TFT was a claim with no stake, now JUST TFT, RIGHT?; BUY THE THIRD became THIRD ONE...; IT NEEDS FIRE cut, it gave the turn away before the throw; alt captions fixed. Round 2: SHIP.
- Watch for: the face. If `apply:fire` is missing and another element landed, the drop still applies (any element takes a bare unit) but there is no merge and no `star_up`; rerender on the next seed from the list (8, 12, 19...) until the throw shows fire, and keep the shop check, since the seed changes both. Last resort: `dice: ["fire"]`, every face fire (not a legal die, eight chosen plus four random, but it reads the same on screen). If the dice still tumble when beat 5 starts, raise the wait in beat 4.
- Render result 2026-10-20 (pwn-zz main): seed 8 throws fire; markers throw 726, apply:fire 991, star_up 1057, cascade_end 1117 (source frames). Shop: plant, insect at setup, reptile and beast after the reroll.
- Build result 2026-10-20: timeline `o_tft_with_dice 9x16`, 1153 frames (19.2 s), no music yet; the last clip runs to the end of the render (2 s of wander) so the end captions hold: STAR UP 70 frames, TFT WITH DICE 110, WHICH ELEMENT NEXT? 133. Audio (user call 2026-10-20: the game's own background music jumped at every cut): game audio at -10 dB with no fades at the cuts, Action 3 Loop at -2 dB as one continuous clip under the whole cut, 60-frame fade-out. Two ripple cuts after the build: the reptile tooltip hover (65 frames) and the die resting before the drag (80 frames); star_up lands at 14.0 s. The camera on the fire shot is set by hand: stash:0 with the fire face, then a pan to board:2 by the drop. FIRE caption in #FF6A2B. Captions: JUST TFT, RIGHT? · REROLL · THIRD ONE... · NO MERGE? · FROM A DIE · FIRE · STAR UP · TFT WITH DICE · WHICH ELEMENT NEXT?. A rerun of align.py or palmier_build.py drops the cuts and the hand camera.
- Exported 2026-10-20: `exports/o_tft_with_dice.mp4`, 1080x1920, 19.2 s, game audio only, no music.
