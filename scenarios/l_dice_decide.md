---
name: l_dice_decide
voice: none
hook: contrarian
angle: the dice are the build: you compose your d12 from elements, the throw is luck, and where you put what fell is the skill
mood: curiosity -> suspense -> payoff -> smug
promise: the shop shows two bare cards, the player throws three dice, the faces fly into the stash, and each one goes onto a bare creature with its impact
button: "BUILD. ROLL. MERGE."
render: plain
seed: 12
round: 11
level: 8
gold: 10
roll: false
dice: ["fire", "ice", "wind", "water", "light", "venom"]
board: [{"slot": 0, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 1, "unit": "ghost", "element": "ice", "stars": 2}, {"slot": 2, "unit": "dragon", "element": "bare", "stars": 1}, {"slot": 3, "unit": "insect", "element": "bare", "stars": 1}, {"slot": 4, "unit": "plant", "element": "bare", "stars": 1}]
bench: []
stash: []
cursor_start: [475, 85]
---
1. hover shop:0 0.7; hover node:%RollButton 0.3 {focus: shop}
2. wander 1.6 r4 {focus: tooltip}
3. click node:%RollButton; mark name=throw focus=dice; wait 3.0 {at: throw, punch, focus: dice}
4. hover stash:0 0.4; hover stash:2 0.4 {focus: stash}
5. drag stash:0 -> board:bare; wait 0.45; mark name=hit1; wait 0.8 {at: hit1, punch}
6. drag stash:1 -> board:bare; wait 0.45; mark name=hit2; wait 0.8 {at: hit2}
7. drag stash:2 -> board:bare; wait 0.45; mark name=hit3; wait 1.4 {at: hit3, punch}
8. wander 2.6 r12; idle 0.6 {focus: board, zoom: 1.0}

## Brief
- Angle: the dice are the build. Round 11: a fire reptile and an ice ghost on the board, three bare 1★ creatures next to them (dragon, insect, plant). The shop shows only bare cards; the d12 build panel shows where the elements come from. The ROLL button throws three dice (luck), the faces fly into the stash, and the player places each one (skill). Nothing is planned around the faces: the cut uses whatever falls.
- Hook: contrarian, silent. SHOP: NO ELEMENTS. over the bare shop cards breaks the autobattler habit of buying the finished unit; YOUR DICE. · YOUR BUILD. over the "Your d12 build" panel (hovering ROLL opens it in the left rail) names where the elements come from. User call 2026-10-16: the dice are the build, the throw is luck, the mix is the player's skill; the cut ends on that.
- Emotion arc: curiosity, suspense while the dice spin, payoff on each impact, smug.
- Proof frame: beat 2 frames the d12 build panel (`focus: tooltip`, the cursor parked on ROLL from the end of beat 1). Beat 3 punches on the throw (the `throw` mark carries `focus=dice`; a mark's focus wins over the beat's). Beats 5-7 land on `hit1..3`, custom marks placed 0.45 s after each drop, close to the impact (0.48 s); the camera punches on the first and the last. The marks keep the beats independent of the faces; two equal faces would make `impact:<el>` match only the first.
- Button: BUILD. ROLL. MERGE. One caption, the whole loop in three verbs over the wander across the finished board: you build the die, the roll is luck, the merge is the player. User pick 2026-10-16 over LUCK ROLLS. · YOU MIX. and BUILD. ROLL. MIX.
- Captions (silent cut, music under, no VO): SHOP: NO ELEMENTS. (beat 1) · YOUR DICE. · YOUR BUILD. (beat 2, over the d12 panel) · nothing over the throw and the landing · {A} ON DRAGON. (hit1) · {B} ON INSECT. (hit2) · {C} ON PLANT. or the synergy it lights, e.g. VENOM TWO. (hit3) · BUILD. ROLL. MERGE. (beat 8). The ON captions show placement as the player's choice. Fill {A}{B}{C} from the `apply:<element>` markers in the cursor json, in order.
- Render result 2026-10-16: faces water, venom, venom on dragon, insect, plant (the same in all four renders on seed 12); the second venom lights Venom 2. Timeline `l_dice_decide 9x16`, 23.3 s, throw at 5.0 s. Captions SHOP: NO ELEMENTS. · YOUR DICE. · YOUR BUILD. · WATER ON DRAGON. · VENOM ON INSECT. · VENOM TWO. · BUILD. ROLL. MERGE. Music still to lay. The tail and the caption times are set by hand in plan.json (align ends 1.5 s after the last marker); a rerun of align.py drops them.
- Voice: none. Silent cut only, by the user's call (2026-10-16). A voiced cut can be added later on the same render.
- Critic (round 1, REVISE): proof captions, button and alt rewritten as suggested. The hook rewrite ("NEED THREE ELEMENTS." / "ROLL. PLEASE.") was refused: the backlog line is the anchor of the design-rule template, as in e. The hook type moved from design-rule to contrarian. Round 2: beat 1 shortened so DICE DO. and the ROLL click land inside 3 s; everything else PASS. User revision 2026-10-16: OKAY OKAY OKAY. cut as filler; the button moved from DIDN'T PICK THEM. · DICE DID. to the build / luck / skill split.
- Alt hook (curiosity gap, silent): 0:00 SHOP'S ALL BARE? over the shop; every other caption is unchanged. Alt button: SAME DICE. NEW BOARD.
- Render: plain, `roll: false`, one live throw in beat 2 (first roll of the round, free; three dice from round 11). Seed 12: the setup shop shows a bare slime and a bare insect, no bonus card (checked with `tools/shop_scan.gd`, round 11, level 8). A bonus card with an element would contradict the first caption.
- Assumptions: the faces are decided by the throw physics (`begin_throw` / `land_die`), not by `RunRNG.dice_rng`. The throw impulses use the global `randf`, which the harness seeds with `seed:`, so a rerender of the same scenario repeats the faces (verified 2026-10-16: two renders, water, venom, venom, identical marker frames). The die is the six demo elements twice each, so every face is a playable element. Faces bank into stash 0, 1, 2 in die order. `board:bare` picks the lowest bare 1★ slot, so the drags fill dragon, insect and plant in that order. Reptile/fire, ghost/ice, dragon, insect and plant have animated art for every demo element (used in e).
- Watch for: three equal faces (1 in 36) merge into one 2★ element in stash:0; it is refused on a bare 1★ and stash:1-2 are empty. Then change `seed:` and rerender (and rescan the shop for the new seed). Two equal faces are fine. If the dice are still flying when beat 3 starts, raise the `wait` in beat 2. A missing `hit1..3` frame is impossible (marks always fire); check that each has an `apply:` marker right before it, otherwise that drop was refused.
