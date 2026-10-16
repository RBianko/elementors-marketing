---
name: m_round_one_round_fifteen
voice: none
hook: number
angle: round 1 is one bare creature like in every autobattler; by round 15 types times elements has turned into boards nobody else has
mood: calm -> recognition -> acceleration -> awe
promise: three real round-1 boards with one bare unit each, then twelve real round-15 boards flip past faster and faster and keep cycling to the end
button: "TYPES × ELEMENTS. WHICH ONE'S YOURS?"
render: multi
seed: 12
round: 1
level: 1
gold: 5
roll: false
board: supabase
pick: 1781454642-3f22a0ae
stage: [1, 1]
min_units: 1
bench: []
stash: []
cursor_start: [475, 85]
---
1. idle 2.6 {focus: board, zoom: 0.9}

## Brief
- Angle: early versus late without a fight. Round 1 is level 1, one field slot: a single bare 1★ plant, the opening of every autobattler (all 442 real round-1 boards are one bare unit, plant 186, slime 136, insect 103). Round 15 is the opposite: twelve real player boards from `player_snapshots.json`, each a different mix of types and elements, flipped Marvel-intro style, each shorter than the last, down to a few frames. The point is the matrix: 8 types × 6 elements × 3 stars on 4-5 slots; real round-15 boards almost never repeat.
- Hook: number, silent. ROUND 1. · VS ROUND 15? inside 2 s over the first round-1 board: the contrast is the stake and promises the cut. Then JUST... ONE UNIT. while the lone unit changes from plant to insect to slime; the viewer recognises the start of any autobattler before the cut.
- Emotion arc: calm, recognition, acceleration, awe.
- Proof frame: the whole short is one locked board framing (zoom 0.9). Round 1 swaps the single bare unit three times, the turn is the hard cut to ROUND 15. and the first full board; the flips themselves are the proof, real boards with the authors' units.
- Button: TYPES × ELEMENTS. · WHICH ONE'S YOURS? over the cycling boards, 1.5 s each. The first names why no two boards match, the second invites a reply from the demo players whose boards these are. No counts: the snapshot cache is a sample, the real number of boards is far larger (user call 2026-10-16).
- Captions (silent cut, music under, no VO, y 0.80): ROUND 1. · VS ROUND 15? (plant) · JUST... ONE UNIT. (insect) · LIKE EVERYONE, RIGHT? (slime) · ROUND 15. (hard cut, first flip) · 2 · 3 · 4 on the next flips, then none while the flips go under 0.2 s · TYPES × ELEMENTS. · WHICH ONE'S YOURS? over the cycle · outro: logo and WISHLIST ON STEAM.
- Round-1 collage: this file renders once per real round-1 board with `SHOT_BUILD=<id>`, 120 frames each: 1781454642-3f22a0ae plant (After_darK) · 1783679294-4da21988 insect (ORPGamer) · 1783440864-831684ba slime (MrSlayer), all a single bare 1★ in slot 0, level 1, Stage 1-1. User call 2026-10-16: round 1 as a collage too, not one plant.
- Cycle and outro (user call 2026-10-16): after the twelfth flip the boards keep cycling from the first at 5 frames each to the end of the short. At the outro a black layer fades the boards down, the Elementors logo (`ui/components/logo_elementors.png` in pwn-zz, nearest-upscaled x4) and WISHLIST ON STEAM with the Steam icon sit on top, and the last frames fade to black. This breaks the no-end-card rule of `hooks.md` on purpose; the user asked for the wishlist plate.
- Flip edit: twelve renders of `m_flip_round_fifteen`, one per board, each with its own seed (so its own shop), gold and a backpack of 1-3 units in the board's elements that cannot merge with the field (user call 2026-10-16: the same shop on every board read as a faked board swap). `refill_shop: true` fills the slots the level opens. Durations at 60 fps: 120, 90, 60, 45, then 30, 20, 13, 9, 6, 5, 4, 4 frames (about 2 s for the first board, user call 2026-10-16), then the cycle. Hard cuts, no transitions; the music hit lands on ROUND 15. and the buildup rides the acceleration. Consecutive boards differ in the main element, so every cut is a colour change.
- Flip order (snapshot ids, main element): 1785909172-ccd1ca98 wind · 1788327907-f17c6191 venom · 1785881573-3761878b fire · 1787572021-e7db638c water · 1787622894-655d7b15 light · 1785934148-5619415c ice/fire · 1789395146-3f09f8fd ghosts ice/light/venom · 1785863036-40c5d99c fire · 1787085720-bd80f00e light · 1785895478-1fd8bb13 wind · 1787513012-9fe98bc6 water · 1785670091-103cf3f1 venom. All have at least two 3★, no bare unit, no beast/fire; 38 distinct type × element pairs across the twelve.
- Critic (round 1, REVISE): hook, beat 2-3 captions and the button rewritten as suggested; the alt button no longer overclaims. User revision 2026-10-16: no board counts in captions, about 2 s on the first flip board.
- Render result 2026-10-16: timeline `m_round_one_round_fifteen 9x16`, 1126 frames (18.8 s). Round 1 collage 0-360 (120 frames per board), round-15 acceleration 360-766 (120, 90, 60, 45, 30, 20, 13, 9, 6, 5, 4, 4), then the twelve boards cycle at 5 frames each to the end; outro from 946: a black layer fades to 70% over 30 frames, logo from 961, Steam icon and WISHLIST ON STEAM from 991. Renders in `renders/m_round1/` and `renders/m_flip/` (NN_<id>), each clip from 1.4 s of its render, game audio off. One framing for every clip, zoom 0.9 (scale 2.844, position -0.9222, 0.05). Captions at y 0.665, between the board and the synergy tags: 0.72 covers the tags, 0.80 the backpack. Built over the MCP endpoint by a one-off script, not palmier_build.py: set the 9:16 aspect after the first clip is placed (the first clip resets the timeline to 16:9), and fix each clip's duration by frames, because a 5-frame span in source seconds lands as 4 frames. Music: Action 3 Loop (Fantasy RPG Music Pack Vol.3), 150 BPM, from 0.44 s of the source so a downbeat lands on the ROUND 15. cut at frame 360; +1 dB, 90-frame fade-out. Export `exports/m_round_one_round_fifteen.mp4`.
- Voice: none, silent cut first. A voiced cut can sit on the same renders later ("Round one. Round fifteen." from the backlog row).
- Alt hook (curiosity gap, silent): 0:00 EVERY GAME STARTS HERE. over the same opening; every other caption unchanged. Alt button: NO TWO ALIKE. · WHICH ONE'S YOURS?
- Render: multi. This file renders three times (round 1, one per board id). `m_flip_round_fifteen` renders twelve times with `SHOT_BUILD=<id>`; each run writes `renders/m_flip_round_fifteen/`, so move the output to `renders/m_flip_round_fifteen/<n>_<id>/` after each run. Same seed and setup on every flip, so the shop, the gold and the UI stay identical and only the board and the synergy tags change.
- Assumptions: round 1 has no dice (dice start at round 2), so `roll: false` and an empty stash are the real state. Level 1 shop shows two T1 bare cards. The flip renders set the level so the field cap equals the board (5 units level 7, 4 units level 5): a spare slot shows a red "N / M placed" warning. The stage label reads Stage 1-1 and Stage 3-5, which proves the rounds without a caption.
- Watch for: a flip board whose synergy tags overflow or whose units sit outside the board frame; drop it and take the next candidate (98 round-15 boards qualify). If the cursor at `cursor_start` tilts a shop card, it does so identically in every flip, which is fine; if it covers a unit, move `cursor_start` in the flip file and rerender all twelve.
