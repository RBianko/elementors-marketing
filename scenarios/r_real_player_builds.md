---
name: r_real_player_builds
voice: none
hook: curiosity
angle: the demo players' own late-game boards, each named in two words, and no two of them alike
mood: curiosity -> recognition -> disbelief -> acceleration -> invitation
promise: six real round 14-15 boards, each with its player's nickname and its build in a caption, from a plain ice build to a board with no elements at all, then a fast flip of every build and "what is your build?"
button: "WHAT IS YOUR BUILD?"
render: multi
seed: 21
round: 15
level: 7
refill_shop: true
author_name: true
gold: 24
roll: false
board: supabase
pick: 1785863781-d44dc9c4
stage: [3, 3]
min_units: 4
bench: []
stash: []
cursor_start: [475, 85]
---
1. idle 2.6 {focus: board, zoom: 0.9}

## Brief
- Angle: a carousel of real player builds. Each board is a snapshot from `player_snapshots.json` loaded onto our field, the author's nickname on screen, and the build named in two or three words the way a player in chat would name it. The variety is the point: types × elements on 4-5 slots, and real players do strange things with it.
- Hook: curiosity, silent. LET'S SEE WHAT REAL PLAYERS BUILD: over the first board inside the first 0.3 s. Nothing promises a fight; the promise is the next board.
- Emotion arc: curiosity, recognition (ice build, fire + light), disbelief (no elements at round 15), the meta call, acceleration through the flip, the question.
- Proof frame: the nickname plate on every board and the stage label in the game UI (Stage 3-4, 3-5) prove these are real late-game boards, no caption needed.
- Shots (snapshot id, round, nickname, units; caption under the board, nickname plate above it):
  - 1785863781-d44dc9c4 · r14 · corvus.chris · five plants, four ice and one wind, 3★/3★/2★ · ICE BUILD
  - 1785934780-17c42fb6 · r15 · Znux · fire plants and light reptile/slime, three 3★ · FIRE + LIGHT BUILD
  - 1787571993-3f56ea0a · r14 · Empa · water demon, beast, insect, ghost plus one ice dragon · WATER WATER... DRAGON
  - 1785884227-833005e1 · r15 · Pirate · 3★ slime, 3★ ghost, two demons, all bare · WHAT IS THIS??? then ZERO ELEMENTS. ROUND 15.
  - 1785896672-747d6bf6 · r15 · Schulze · four 3★ fire plants · FIRE FIRE FIRE FIRE, one word per 3★ plant left to right
  - 1788336819-11dac5bb · r15 · qifaysdamha · five venom units of five types, four 3★ · THIS IS NEW META
- Timing at 60 fps: board 1 holds 150 frames (the opening caption reads first, then ICE BUILD from frame 90), boards 2, 3, 5, 6 hold 120 each, Pirate holds 150 for the two captions. About 13 s before the flip, about 23 s in total with the flip and the outro. Hard cuts, consecutive boards differ in the main colour.
- Thank-you beat (user call 2026-10-22): right after the qifaysdamha shot the flip starts and 5016 BUILDS · THANK YOU ALL! sits over its first 2 s, so the flip itself stands for the 5016 builds.
- Flip (as m and the Steam trailer, user call 2026-10-22: every board keeps its @nickname plate, so a player can pause and find their own): one board per player, 51 players, all with a nickname, round 10-15, 4+ units, each player's latest strongest board. Order: the six shots above, then these 45 (shuffle so consecutive boards differ in main colour): 1790807889-f7c607f5 · 1785909172-ccd1ca98 · 1785875466-17ae2312 · 1785896495-23005011 · 1786122293-5ea92a5f · 1787085720-bd80f00e · 1787098554-69693a71 · 1787605340-0ed6617f · 1787622894-655d7b15 · 1788467434-85b85ed8 · 1783441584-72587194 · 1785838289-fb2238be · 1785841873-682e8a9c · 1785908179-a2aad740 · 1786014846-cdc6fd62 · 1786053233-32e93818 · 1786715291-91b21c13 · 1787105103-38de4dc0 · 1787587341-62939de0 · 1787664335-1b1bf1f1 · 1787683227-31da0db1 · 1788715307-6cf4301d · 1785669247-9f44d353 · 1785840291-5e9d9f80 · 1785895134-0d8b595b · 1785874708-43c02e2c · 1785881573-3761878b · 1785937113-597a9695 · 1785948921-a6ba44a5 · 1786186970-128edd78 · 1787919720-c348212a · 1785840995-b8b352a3 · 1787585504-c35eb53a · 1787590739-6fce3141 · 1788632255-8ae83376 · 1791701862-fad5505a · 1781455247-98027834 · 1783679698-1680fd0c · 1785947697-36354c90 · 1786023186-9ba92cd7 · 1786152173-c8165e68 · 1786292434-39835db7 · 1789346341-57427120 · 1786055168-0bfee21f · 1785854798-4b04e6b8. Cut lengths: 30, 20, 13, then 8 frames each to the end of the list (about 7.5 s; 8 frames is short enough to read as a flip and long enough that a paused frame shows a whole board and a sharp nickname). No build captions during the flip, only the nickname plates and the thank-you line.
- Critic (round 1, REVISE): voice FAIL on three flat labels in a row; Znux, Empa and Schulze captions rewritten as suggested (Schulze's chant without periods, per the no-trailing-periods call), ICE BUILD moved to frame 90, black held 1.5 s at most, alt hook says LATE GAME because shot 1 is round 14.
- Lint: the two WARNs (no punch, 2.6 s) are the m_flip template; the length and the rhythm live in the edit.
- Outro: as m and n. A black layer fades the flip down, the Elementors logo, then full black and WHAT IS YOUR BUILD? centred, held 1.5 s at most. No wishlist plate unless the user asks for it as in m and n.
- Button: WHAT IS YOUR BUILD? It asks the demo players for a reply, and some of them will recognise their own board.
- Captions (silent, music under, y 0.665 as in m, Poppins-Bold, no trailing periods per the 2026-10-19 call except the opening colon): LET'S SEE WHAT REAL PLAYERS BUILD: · ICE BUILD · FIRE + LIGHT BUILD · WATER WATER... DRAGON · WHAT IS THIS??? · ZERO ELEMENTS. ROUND 15 · FIRE FIRE FIRE FIRE · THIS IS NEW META · 5016 BUILDS · THANK YOU ALL! · WHAT IS YOUR BUILD?. Element words in their colour from n. The nickname plate goes above the board, smaller, white, prefixed with @.
- Voice: none, silent cut only; the streamer-voice pass does not apply.
- Alt hook (challenge, silent): 0:00 REAL PLAYERS. LATE GAME. RATE THESE: then the same shots. Alt button: WHICH ONE WINS?
- Render: multi, the m_flip template. Render once per id with `SHOT_BUILD=<id>`, which overrides `pick:`; move each output to `renders/r_builds/NN_<id>/`. Per id the render loop rewrites `round` (14 or 15, so the stage label matches the snapshot) and `level` (field cap = unit count: 4 units level 5, 5 units level 7). Each id gets its own seed and a 1-3 unit backpack in the board's elements that cannot merge with the field, as in m, so the shop and bench differ from shot to shot.
- Assumptions: 5016 is the count of demo boards in the local cache (`player_snapshots.json`, 2026-06-14..2026-10-11, 81 nicknames; user call 2026-10-22); no time span in the caption, since the boards span four months. nicknames are the `author_nickname` the demo players already show to their PvP opponents, so they go on screen as-is. Pirate's board really is all bare at round 15 (3★ slime, 3★ ghost, 2★ and 1★ demon); that is the WHAT IS THIS??? shot. "New meta" is a joke caption, not a balance claim.
- Watch for: Schulze's four identical 3★ fire plants must not trip the setup merge (3★ is the cap, so they should stay four); "field cap refused" in a log means the level is too low for that board; a nickname with characters Poppins lacks (TépBée has é, fine) falls back to a different font.
- Render result 2026-10-22: timeline `r_real_player_builds 9x16`, 1483 frames (24.7 s). Main shots 0-816 (186, 120, 120, 150, 120, 120) as video from 1.4 s of renders with a 4.2 s idle; flip 816-1263 (30, 20, 13, then 8 frames) and outro 1263-1483 as stills, one per board (`still.png`, last frame of a 0.3 s idle render), every board with its @nickname plate (Poppins-Bold 46, y 0.30), outro boards included (user call 2026-10-22). Outro: a black layer to 72% over 30 frames, logo (y 0.42) and WHAT IS YOUR BUILD? (64, y 0.60) on one screen over the dimmed cycling boards, fade to black over the last 25 frames (user call 2026-10-22). Captions Poppins-Bold 50 at y 0.635 (60 wrapped onto the synergy tags). `author_name: true` puts the snapshot author's nickname into the in-game player plate (pwn-zz harness). Renders in `renders/r_builds/NN_<id>/`, 51 boards, one per player; game audio off. Music: Action 3 Loop from 0.84 s so a downbeat lands on the flip at 816, -1 dB, 60-frame fade-out. Built over the MCP endpoint by a one-off script, as m.
