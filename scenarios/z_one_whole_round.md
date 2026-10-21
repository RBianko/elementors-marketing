---
name: z_one_whole_round
voice: none
hook: stakes-first
angle: the whole round 10 boss turn in one take, the way a player plays it: free throw, two drops, a reroll that hits the lucky slot, a 3★ on buy, the fire tag at four, the round 10 boss fight, the loot
mood: curiosity -> build-up -> hype -> tension -> relief
promise: nothing is cut between the first throw and the boss loot; every mechanic of the demo shows up once inside a single round and the boss goes down
button: "BOSS DOWN"
render: offer
seed: 61
round: 10
level: 6
gold: 24
roll: false
dice: ["fire", "fire", "fire", "fire", "fire", "fire", "fire", "fire", "ice", "wind", "water", "venom"]
board: [{"slot": 0, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 1, "unit": "plant", "element": "fire", "stars": 2}, {"slot": 2, "unit": "ghost", "element": "bare", "stars": 1}, {"slot": 3, "unit": "insect", "element": "bare", "stars": 1}, {"slot": 4, "unit": "slime", "element": "fire", "stars": 2}]
bench: [{"unit": "reptile", "element": "fire", "stars": 2}]
stash: []
offer: {"kind": "echo_2star", "unit": "reptile", "element": "fire", "stars": 2}
cursor_start: [700, 520]
---
1. wander 1.2 r10; hover board:2 0.6 {focus: board}
2. hover node:%RollButton 0.4; click node:%RollButton; mark name=throw focus=dice; wait 3.0 {at: throw, punch, focus: dice}
3. hover stash:0 0.4; hover stash:1 0.4 {focus: stash}
4. drag stash:0 -> board:bare; wait 0.45; mark name=hit1; wait 1.0 {at: hit1, punch}
5. drag stash:1 -> board:bare; wait 0.45; mark name=hit2; wait 1.0 {at: hit2, punch}
6. hover node:%RerollButton 0.4; click node:%RerollButton; wait 1.2 {focus: shop}
7. hover shop:4 1.0; idle 0.4 {punch, focus: shop:4, zoom: 1.8}
8. click shop:4; wait 0.5; idle 1.6 {at: star_up, punch, focus: board:0}
9. hover board:0 1.6 {focus: tooltip}
10. hover syn:fire 1.8 {focus: tooltip}
11. hover node:%EndRoundButton 0.4 {focus: node:%EndRoundButton, zoom: 1.3, anchor: end}
12. battle hold=0.4 open=8 speed=1.5 roam=true {at: battle_start, focus: battle}
13. idle 1.5 {at: battle_end, punch, focus: board}
14. hover loot:0 0.8; click loot:0; idle 0.5; hover loot:take 0.5; click loot:take {focus: board}
15. summary hold=3.0 {at: summary}

## Brief
- Angle: the long pure gameplay test from the backlog (M.I.N.S.K. 2 min), against the 15 s cut k. Round 10 is a boss round (the render met the 3★ Lava Lord, Stage 2 boss), so the round has a stake on its own: a lost boss round costs 10 HP. Every mechanic the shorts have shown one at a time (throw, apply, lucky roll, 3★, synergy, fight, loot) happens once, in order, in one take.
- Hook: stakes-first, silent. 0:00 BOSS ROUND, then NO CUTS inside 2 s over the moving board, LOSE = 10 HP on the ROLL click: the format is the promise, the boss is the stake.
- Emotion arc: curiosity, build-up (throw and drops), hype (lucky slot, 3★), tension (boss fight), relief (loot).
- Proof frame: beat 2 punches the `throw` mark on the dice table; beats 4 and 5 punch `hit1`/`hit2` on the two impacts; beat 7 the rainbow reveal of the COPY! card in shop:4; beat 8 `star_up` on board:0 (3★ sparkle, strong edge glow, shake); beat 13 `battle_end` on the Boss Loot pick.
- Captions (silent, music under, y 0.72, no trailing periods, the mechanic named, not reactions): BOSS ROUND (0:00) · NO CUTS (by 1.2 s) · LOSE = 10 HP (on the ROLL click) · TWO DICE (over the throw) · each face in its colour on its landing (filled after the render) · ANY CREATURE (beat 4) · TAKES IT (beat 5) · REROLL (beat 6) · LUCKY SLOT (beat 7) · COPY! · THREE STAR (beat 8, on `star_up`) · FIRE 4 (beat 10, only if the throw lit it; otherwise the tag the board shows) · GOLEM BOSS (battle start) · then one caption every 6-8 s across the fight, filled from the render, each naming a thing on screen: BURN STACKS (if Fire 4) · the 3★ unit when the roaming cursor opens its tooltip · BOSS HALF HP · ONE LEFT · BOSS DOWN (beat 13) · PICK LOOT (beat 14) · WHICH BUILD NEXT? held over the summary to the end.
- Button: BOSS DOWN, then the held WHICH BUILD NEXT? (silent cuts end on the held question).
- Voice: none. Silent cut only, the shape that broke out (e silent, 2026-10-18); a voiced read over 60+ s would turn into narration.
- Alt hook (number, silent): same beats, 0:00 becomes ONE ROUND · 69 SECONDS (set to the real length after the render), button WHOLE ROUND instead of BOSS DOWN.
- Edit: one continuous clip from `warmup` to the end of the summary hold, no ripple cuts, no speed change in the edit; the camera keyframes from `align.py` stay (they are framing, not cuts). Game audio under the music as in o.
- Render: offer route. `offer:` arms an echo_2star fire reptile; the reroll in beat 6 places it in shop:4 with the full reveal FX. The throw is physics seeded from `seed:`, two dice in round 10 (free first roll), the faces decide the two drops (`board:bare` targets ghost and insect, any element takes a bare 1★).
- Assumptions: gold 24 covers the reroll (2) and the echo card (about 17: 4 × 3 × 1.4); the buy merges board:0 + bench:0 + the card into a 3★ on board:0 (board-first). Fire on board before the throw: reptile, plant, slime = Fire 3; one fire face lights Fire 4 (burn stacks). Level 6 caps the field at 5, the board is full, so the drops never need a move. Fight: the first 8 s at speed 1 (the opening reads), then x1.5, about 29 s; the round lands around 65-70 s. Harness speed is not an edit cut.
- Critic (round 1, REVISE): the stake was only in the brief, now LOSE = 10 HP on the ROLL click and the hook relabelled stakes-first; the speed 1 fight left 20+ s with no change, now open=8 speed=1.5 roam=true plus a caption every 6-8 s. Round 2: SHIP.
- Watch for: render once and read the markers before captions. If the boss wins (defeat overlay instead of loot), try the next seed and re-check the throw. If the total runs past 90 s, `speed=2` on beat 12. If the two faces are identical they stay two 1★ in the stash (a stash merge needs three), fine. If `star_up` is missing, the echo card was refused (gold) or not armed.
- Render result 2026-10-21 (pwn-zz main 16c48575): seed 61 throws fire, fire; Fire 5 on the board; the echo card cost 17 (gold 24 → 22 → 5); 3★ fire reptile on the buy; victory over the 3★ Lava Lord (not the Golem: the round 10 boss in the current build), loot Awakening taken. Markers (source frames): throw 334, impact:fire 788 and 1033, star_up 1472, battle_start 2152, battle_open_end 2632, battle_end 3088, summary 3615; render 3797 frames (63.3 s). The fight is 15.6 s, shorter than the 29 s estimate.
- Build result 2026-10-21: timeline `z_one_whole_round 9x16`, 3725 frames (62.1 s), one continuous clip from `warmup` to the end of the render. Captions written into plan.json by hand: BOSS ROUND · NO CUTS · LOSE = -10 HP · TWO DICE · FIRE, FIRE (#FF6A2B) · ANY CREATURE · TAKES IT · REROLL · LUCKY SLOT · COPY! · THREE STAR · FROM ONE BUY · FIRE 5 · BURN STACKS · LAVA LORD · THREE STAR BOSS · BURN TICKS · BOSS DOWN · PICK LOOT · WHICH BUILD NEXT?. Fight camera set by hand in plan.json: a fixed wide frame (scale 1.538, x -0.2, y 0.257) from 2138 to 3002 so the allies and the boss are both in frame; the align.py fight follow kept the boss off the right edge. Audio: game -10 dB, Action 3 Loop -2 dB under the whole cut, 60-frame fade-out. A rerun of align.py drops the captions and the hand camera.
- Captions rewritten by the user in Palmier 2026-10-21, livelier than the mechanic labels: BOSS ROUND · NO CUTS · LOSE = -10 HP · ROLL DICE · FIRE AND FIRE · THAT'S FIRE BUILD · FIRE SYNERGY · REROLL FOR MORE · LUCKY ROLL! · COPY! · THREE STAR · FROM ONE BUY · FIRE 5 · BURN STACKS IS INSANE! · *LAVA LORD* · THREE STAR BOSS · BURN BURN BURN · OP BUILD · PICK LOOT · WHICH BUILD NEXT?. Exported `exports/z_one_whole_round.mp4`, 1080x1920, 62.1 s.
