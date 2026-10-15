---
name: b_fourth_ice_freeze
voice: ninja
hook: need-first
angle: three ice units on the board, a bare dragon and one ice in the stash; the fourth ice tips the synergy and the fight opens with the whole enemy board frozen
mood: want -> count -> hype -> disbelief -> smug
promise: the player drops ice on the bare dragon, the ice tag turns gold at four, and when the PvP fight starts every one of the opponent's units is iced over before anyone swings
button: "First second. Frozen. All five, man."
render: plain
seed: 34
round: 12
opponent: 1788714261-883417cc
level: 7
gold: 10
dice: ["ice", "fire", "wind"]
board: [{"slot": 0, "unit": "slime", "element": "ice", "stars": 3}, {"slot": 1, "unit": "beast", "element": "ice", "stars": 3}, {"slot": 2, "unit": "ghost", "element": "ice", "stars": 2}, {"slot": 3, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 4, "unit": "dragon", "element": "bare", "stars": 2}]
bench: []
stash: [{"element": "ice", "stars": 2}]
cursor_start: [700, 520]
---
1. hover board:4 0.9; hover stash:0 1.0; hover syn:ice 0.4 {focus: board} — "Okay. One more ice and they all FREEZE."
2. wander 2.8 r6 {focus: tooltip} — "Three ice. I need four. Four."
3. drag stash:0 -> board:4; idle 1.6; hover syn:ice 0.3 {at: impact:ice, punch, lead: 15, focus: board:4, zoom: 1.6} — "Oh he's cold. Cold boy."
4. wander 3.2 r6 {focus: tooltip} — "[whispering] Four. Okay okay okay. Send it."
5. battle hold=0.3 speed=2 {at: battle_start, punch, lead: 125, focus: battle} — "[gasping] Wait... FROZEN. All of them."
6. idle 3.9 {at: battle_end, lead: -260, focus: battle} — "[laughs] First second. Frozen. All five, man."

## Brief
- Angle: round 12, a PvP round. Two 3★ and one 2★ ice units on the board next to a bare 2★ dragon and one 2★ ice in the stash. The ice goes on the dragon, the ice tag tips to four, and the fight against a real player's board opens with all five of their units iced over.
- Hook: need-first. "Okay. One more ice and they all FREEZE." The line names the missing piece and the payoff; the 0:00 caption is ONE MORE ICE.
- Emotion arc: want, count, hype, disbelief, smug.
- Proof frame: beats 2 and 4 frame the ice ladder tooltip (`focus: tooltip`, the cursor parked on the tag from the end of the beat before): at three, then at four with "Combat start: freeze every enemy for 3s" lit. Beat 3 punches `impact:ice` on board:4 (`lead: 15`). Beat 5 punches `battle_start` with `lead: 125`: the ice wash lands about 2.5 s after the BATTLE click and holds about 1.5 s at x2. Beat 6 lands on `battle_end` with `lead: -260`, so the button ends before the result panel.
- Button: "First second. Frozen. All five, man." The freeze is a combat-start effect, so the button says when it happened, not that they never moved (they did, after 3 s).
- Captions: OKAY. · ONE MORE ICE · AND THEY ALL · FREEZE. · THREE ICE. · I NEED FOUR. · FOUR. · OH HE'S COLD. · COLD BOY. · FOUR. · OKAY OKAY OKAY. · SEND IT. · WAIT... · FROZEN. · ALL OF THEM. · FIRST SECOND. · FROZEN. · ALL FIVE, MAN.
- Silent cut: `renders/b_fourth_ice_freeze/plan_silent.json`, same picture and game audio, no VO. ONE MORE ICE. at 0:00, THREE ICE. over the tooltip, FOURTH ICE. from the impact, ALL FIVE FROZEN. from the first frozen frame (timeline 1246), FROM SECOND ONE. over the fight's tail. Music still to be laid under it.
- Voice: Liam placeholder (Ninja is a library voice, 402 on the free API plan), a hand read replaces `vo/b_fourth_ice_freeze/` later. Revision 2026-10-15 (user): beat 5 cut to "Wait... FROZEN. All of them." to fit the 1.5 s freeze at x2, the button rewritten around the combat start.
- Alt hook (outcome-first): "Every single one of them. Frozen. Watch." 0:00 caption: EVERY ONE FROZEN. Alt button: "Four ice. That's the whole trick."
- Alt hook (number): "Four ice. Three seconds. Nobody moves." 0:00 caption: FOUR ICE. Alt button: "Three seconds. Felt like ten."
- Render: plain route. The opponent is a real player's round-12 board pinned with `opponent: 1788714261-883417cc` (TheLost12, Steam portrait, five 2★ fire/light units, Fire 4 and Ghost 2), read from `pwn-zz/build/pvp_portraits.json`, which holds the demo snapshots with an `author_portrait` for rounds 11, 12 and 14 (fetched 2026-10-15). The harness makes it the whole PvP pool for the round and preloads the portrait. Bestiary unlock toasts are off (harness default; `unlock_toasts: true` brings them back).
- Speed: x2 (user call 2026-10-15). The fight is 11.4 s; the cursor roams the field and the units during it, so unit tooltips open on the left now and then.
- Assumptions: level 7 caps the field at 5. A 2★ ice in the stash goes on the bare 2★ dragon because the stars match. With all-2★ the fight was a draw; slime and beast at 3★ win it.
- Material for k: beat 5, the whole enemy board frozen in the first second of the fight.
- Watch for: the freeze wash has to be on screen when "FROZEN" is said; if a rerender moves the intro, re-read the first frozen frame and reset `lead`. The fight camera zooms out to 0.55 over a blurred backdrop so both teams fit the 9:16 frame. A defeat or draw means the opponent outclasses the board: raise stars, not the opponent.
