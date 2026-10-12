---
name: j_venom_golem_boss
voice: ninja
hook: fail-to-win
angle: the round 10 golem boss ended the last two runs; this time the board is five venom and the boss melts
mood: dread -> anticipation -> disbelief -> smug
promise: a five venom board walks into the golem boss that killed the last run and wins without a scratch
button: "Couldn't beat him last run. That was free."
render: plain
camera: wide
seed: 61
round: 10
level: 6
gold: 12
dice: ["venom", "fire", "ice"]
board: [{"slot": 0, "unit": "plant", "element": "venom", "stars": 2}, {"slot": 1, "unit": "reptile", "element": "venom", "stars": 2}, {"slot": 2, "unit": "demon", "element": "venom", "stars": 1}, {"slot": 3, "unit": "plant", "element": "venom", "stars": 2}, {"slot": 4, "unit": "slime", "element": "venom", "stars": 2}]
bench: []
stash: []
cursor_start: [760, 500]
---
1. wander 0.7 r12; hover board:2 0.9; idle 0.8 {focus: board} — "Golem boss. He killed me last run."
2. hover syn:venom 1.5 {focus: tooltip, zoom: 0.7} — "But now I've got venom build."
3. hover node:%EndRoundButton 0.3 {focus: node:%EndRoundButton, zoom: 1.3, anchor: end} — "Okay. Let's see. Battle."
4. battle hold=0.4 speed=6 {at: battle_start, lead: 80, zoom: 0.58} — "Come on. Come on... melt."
5. drift -490,-300; idle 2.4 {at: battle_end, punch, focus: board} — "...wait. That's it?"
6. hover loot:0 0.7; click loot:0; idle 0.5; hover loot:take 0.5; click loot:take {focus: board, zoom: 0.62} — "Bro. This venom build is unreal."
7. summary hold=3.0 {at: summary, zoom: 0.78} — "Couldn't beat him last run. That was free."

## Brief
- Angle: round 10, Golem Boss. The last runs died right here; now the board is plant, reptile, demon, plant, slime, all venom, mostly 2★, and the fight ends before the player finishes worrying.
- Hook: fail-to-win. "Golem boss. He killed me last run." The stake (a boss that already won once) is out by 2 s, the fight starts by about 8 s.
- Emotion arc: dread, anticipation, disbelief, smug.
- Proof frame: beat 5 on `battle_end`, the Boss Loot pick after a speed 6 fight full of poison ticks (a boss win shows the loot before the result overlay). Beat 6 takes Awakening, beat 7 lands the button on the combat summary. Beat 2 is the setup proof: the synergy tags show venom at its top tier (+100% magic DoT taken by enemies).
- Button: "Couldn't beat him last run. That was free." Callback to the hook; the user's "прошлый раз не проходил, сейчас изи" anchor.
- Captions: HE KILLED ME · VENOM BUILD · LET'S SEE · MELT · THAT'S IT? · UNREAL · THAT WAS FREE
- Alt hook (contrarian): "Chat said venom can't kill a boss." 0:00 caption: CHAT SAID NO. Alt button: "Can't kill a boss, huh."
- Alt hook (curiosity): "Watch how long this boss lasts." 0:00 caption: WATCH THE BOSS. Alt button: "Last run he lasted longer than me."
- Camera: wide. The whole scene stays in frame, mirrored dark copies fill the bands above and below; zoom only moves between 0.5 and 0.78.
- Render: plain. Board from Supabase snapshot `1788612516-855ad828` (demo 0.7.0, round 10, HP 18), written by hand so the render does not depend on the snapshot cache. The same player's round 11 snapshot `1788612561-ab034d86` has the same board and HP 18: the real fight was a clean win. Two earlier runs of that account ended at round 10 on water boards, so "killed me last run" is true to the data.
- Assumptions: `round: 10` makes End Round start the Golem Boss (`boss_stage_2` in `rounds.tsv`); level 6 gives the 5 unit field cap; five venom units reach the venom 4 tier (`amplify_dot_magic`, 1.00). The harness combat is seeded, so a win on one render is a win on every render with seed 61.
- Watch for: render once before the voice pass and check where `battle_end` lands; past 15 s, raise beat 4 to `speed=8` or trim the `idle 0.8` in beat 1. If the overlay says defeat, try another `seed`, or swap the 1★ demon for a 2★; the boss fight at speed 6 may run longer than the ~6.5 s the lint assumes, which only stretches the silence under beat 4. Venom tags must read on screen in beat 2, otherwise move the focus to the board.
- Critic: suggested replacing "This venom build is unreal" with "We're so back"; refused, the line is the user's anchor ("собрал нереальный venom build").
