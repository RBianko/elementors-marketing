---
name: b_fourth_ice_freeze
voice: ninja
hook: need-first
angle: three ice units on the board, a bare dragon and one ice in the stash; the fourth ice tips the synergy and the fight opens with the whole enemy board frozen
mood: want -> count -> hype -> disbelief -> smug
promise: the player drops ice on the bare dragon, the ice tag turns gold at four, and when the battle starts every bandit is iced over before anyone swings
button: "Did they move? They didn't even move, man."
render: plain
seed: 34
round: 13
level: 7
gold: 10
dice: ["ice", "fire", "wind"]
board: [{"slot": 0, "unit": "slime", "element": "ice", "stars": 2}, {"slot": 1, "unit": "beast", "element": "ice", "stars": 2}, {"slot": 2, "unit": "ghost", "element": "ice", "stars": 2}, {"slot": 3, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 4, "unit": "dragon", "element": "bare", "stars": 2}]
bench: []
stash: [{"element": "ice", "stars": 2}]
cursor_start: [700, 520]
---
1. hover board:4 0.9; hover stash:0 1.5 {focus: board} — "Okay. One more ice and they all FREEZE."
2. hover syn:ice 2.0 {focus: synergies} — "Three ice. I need four. Four."
3. drag stash:0 -> board:4; idle 1.8 {at: impact:ice, punch, focus: board:4, zoom: 1.6} — "Oh he's cold. Cold boy."
4. hover syn:ice 2.4 {focus: synergies} — "[whispering] Four. Okay okay okay. Send it."
5. battle hold=0.3 speed=1 {at: battle_start, punch, lead: 165, focus: battle} — "[gasping] Wait... frozen. They're all frozen. Go go go go."
6. idle 4.9 {at: battle_end, lead: -230, focus: battle} — "[laughs] Did they move? They didn't even move, man."

## Brief
- Angle: round 13, three 2★ ice units on the board next to a bare 2★ dragon and one 2★ ice in the stash. The ice goes on the dragon, the ice tag tips to four, and the fight against the bandits opens with every enemy iced over.
- Hook: need-first. "Okay. One more ice and they all FREEZE." The line names the missing piece and the payoff; the 0:00 caption is ONE MORE ICE.
- Emotion arc: want, count, hype, disbelief, smug.
- Proof frame: beat 3 punches `impact:ice` on board:4 (the dragon turns ice). Beat 4 holds on the ice tag at four with the ladder tooltip open; the tag only changes rank, it has no animation, so the tooltip is what reads. Beat 5 punches `battle_start` with `lead: 165`: Ice-4 freezes every enemy for 3 s of combat time, an ice wash and shine sweep over each sprite. Beat 6 lands on `battle_end` with a negative lead, no punch.
- Button: "Did they move? They didn't even move, man." The line asks the screen and answers it, and plays back to the "they all freeze" hook.
- Captions: OKAY. · ONE MORE ICE · AND THEY ALL · FREEZE. · THREE ICE. · I NEED FOUR. · FOUR. · OH HE'S COLD. · COLD BOY. · FOUR. · OKAY OKAY OKAY. · SEND IT. · WAIT... · FROZEN. · THEY'RE ALL FROZEN. · GO GO GO GO. · DID THEY MOVE? · THEY DIDN'T EVEN · MOVE, MAN.
- Silent cut: ONE MORE ICE. at 0:00, THREE ICE. over the tag, FOUR. on the impact, EVERYONE FROZEN. on `battle_start`, DIDN'T EVEN MOVE. over beat 6.
- Voice: Liam placeholder (Ninja is a library voice, 402 on the free API plan), a hand read replaces `vo/b_fourth_ice_freeze/` later. Pass applied with no refusals. Beat 2 became "Three ice" because "Three" alone did not say what was being counted. Beat 4 gets a whisper on the plead. Beat 5 stops on the freeze, says it twice and chants "go" over the rest of the fight (critic rewrite).
- Alt hook (outcome-first): "Every single one of them. Frozen. Watch." 0:00 caption: EVERY ONE FROZEN. Alt button: "Four ice. That's the whole trick."
- Alt hook (number): "Four ice. Three seconds. Nobody moves." 0:00 caption: FOUR ICE. Alt button: "Three seconds. Felt like ten."
- Render: plain route, nothing armed, no seed hunt. Round 13 is a creep round (`creep_stage_3`): two bare 1★ bandit warriors and three venom 2★ cutthroats, five enemies under the freeze.
- Speed: the fight plays at game speed (`speed=1`, user call 2026-10-15: no acceleration). The combat intro takes ~2.2 s after the BATTLE click, the freeze holds ~2.8 s on screen (render frames 1225-1395), `lead: 165` puts "Wait..." 0.5 s into it. The fight is 19.5 s; the button rides its last 4 s (`at: battle_end, lead: -230`) over our five untouched units instead of the dark result panel. The `open=` harness param (first N s at speed 1) stays available but is unused here.
- Assumptions: level 7 caps the field at 5, so the five units fit. A 2★ ice in the stash goes on the bare 2★ dragon because the stars match. Five 2★ units beat the round-13 bandits. Seed 34 only matters for the shop, which is never touched.
- Material for k: beat 5, all five bandits frozen in the first second of the fight.
- Watch for: the freeze wash has to be on screen when "Wait..." starts. The fight camera zooms out to 0.55 over a blurred backdrop so both teams fit the 9:16 frame. If the overlay shows a defeat, swap the fire reptile for a 2★ ice demon or raise the stars. Check that the ice tooltip is readable in beat 4 at `focus: synergies`. Dragon-6 immunity does not apply, the bandits have no dragons.
