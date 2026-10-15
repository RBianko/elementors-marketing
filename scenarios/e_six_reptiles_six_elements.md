---
name: e_six_reptiles_six_elements
voice: ninja
hook: curiosity
angle: the one rule of the game shown on one row: any creature takes any element, six different bare creatures become six elemental ones
mood: calm -> curiosity -> rising hype -> smug
promise: six bare 1★ creatures in a row (reptile, slime, insect, plant, ghost, dragon) take fire, ice, wind, water, light and venom one after another, each with its impact, and the row ends as six elemental creatures
button: "Six guys, six elements. Pick one, chat."
render: plain
seed: 11
round: 4
level: 9
gold: 10
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "reptile", "element": "bare", "stars": 1}, {"slot": 1, "unit": "slime", "element": "bare", "stars": 1}, {"slot": 2, "unit": "insect", "element": "bare", "stars": 1}, {"slot": 3, "unit": "plant", "element": "bare", "stars": 1}, {"slot": 4, "unit": "ghost", "element": "bare", "stars": 1}, {"slot": 5, "unit": "dragon", "element": "bare", "stars": 1}]
bench: []
stash: [{"element": "fire", "stars": 1}, {"element": "ice", "stars": 1}, {"element": "wind", "stars": 1}, {"element": "water", "stars": 1}, {"element": "light", "stars": 1}, {"element": "venom", "stars": 1}]
cursor_start: [760, 520]
---
1. wander 0.5 r10; hover board:2 0.6; hover stash:0 0.5 {focus: board} — "Okay. Six guys, six elements. Watch."
2. drag stash:0 -> board:0; wait 0.9 {at: impact:fire, punch, focus: board:0} — "Oh! Fire."
3. drag stash:1 -> board:1; wait 0.9 {at: impact:ice, lead: 50, focus: board:1} — "Ice. Cold boy."
4. drag stash:2 -> board:2; wait 0.9 {at: impact:wind, lead: 50, focus: board:2} — "Wind. Wind wind wind."
5. drag stash:3 -> board:3; wait 0.9 {at: impact:water, lead: 50, focus: board:3} — "[deadpan] Water... sure."
6. drag stash:4 -> board:4; wait 0.9 {at: impact:light, lead: 50, focus: board:4} — "Light. Oh he glows."
7. drag stash:5 -> board:5; wait 0.5; idle 2.0 {at: impact:venom, punch, focus: board:5} — "Oh venom. VENOM! That's nasty."
8. wander 4.2 r14; idle 0.7 {focus: board, zoom: 1.0} — "[chuckles] Six guys, six elements. Pick one, chat."

## Brief
- Angle: the game's one rule on one row. Six different bare 1★ creatures, the stash holds one of each demo element, six drags turn the row into six elemental creatures. Nothing is explained; the row does it.
- Hook: curiosity. "Six guys, six elements. Watch." The stake is the promise of a transformation; the first impact answers it inside 3 s.
- Silent cut A (primary): VO track off, music under, captions only. 0:00 ANY CREATURE. · ANY ELEMENT. over beat 1, then the element name on each impact: FIRE · ICE · WIND · WATER · LIGHT · VENOM, then SIX CREATURES. · SIX ELEMENTS. · PICK ONE. over beat 8. The 0:00 caption is a design-rule statement, not a player line; a deliberate break of the hook rule, because it is the user's anchor and the "unique design in one sentence" template (Sugardew, RECUR) in the TikTok data works exactly this way.
- Silent cut B (A/B of the silent cut): 0:00 SIX GUYS. · SIX ELEMENTS. (the stake), the six element names as in A, then ANY CREATURE. · ANY ELEMENT. · PICK ONE. over beat 8, the anchor as the verdict after the proof. Same timeline, captions only.
- Voiced cut (second variant): the lines above, same timeline.
- Emotion arc: calm, curiosity, rising hype on each impact, smug.
- Proof frame: six impacts. Beat 2 punches `impact:fire` on board:0, beat 7 punches `impact:venom` on board:5; beats 3-6 land on their own `impact:<element>` marker with `lead: 50` so each reaction follows the impact by close to a second without a camera punch, and the follow camera carries the row left to right.
- Button: "Six guys, six elements. Pick one, chat." Callback to the hook plus the one chat address, an invitation to reply with a creature or an element.
- Captions (voiced cut): SIX GUYS · WATCH · OH! FIRE · COLD BOY · WIND WIND WIND · WATER... · SURE · HE GLOWS · VENOM! · NASTY · PICK ONE
- Voice: pass applied 2026-10-14. Beats 2 and 7 opened on the element noun, which read as a caption of the impact; both now open on the blurt. Tags: `[deadpan]` on beat 5, `[chuckles]` on beat 8, the two allowed. Beat 8 alt with a second "Pick one" kept in reserve if the voiced cut feels sparse between beats 3 and 6 (33 words over 22 s, the row is the content). Beats 1, 3, 4, 6 kept as drafted.
- Alt hook (contrarian, voiced): "Chat said the element doesn't matter." 0:00 caption: DOESN'T MATTER? Alt button: "Doesn't matter, huh." (the button drops "chat" so the short keeps one chat address).
- Render: plain. Six bare creatures of six different types, six 1★ elements, all setup keys; no offer, no save, no seed hunt. `level: 9` for the six-unit field cap (`max_field_units` 6 from level 8).
- Revision 2026-10-14: the first render used six bare reptiles; three identical bare 1★ units auto-merge, so the row collapsed into 2★ bodies and the 1★ elements were refused on them (only light and venom landed). Six different types never merge. Reptile stays in slot 0 as the hook unit.
- Assumptions: all six pairs (reptile/fire, slime/ice, insect/wind, plant/water, ghost/light, dragon/venom) have animated 1★ art; beast is left out because beast/fire is static. Six different 1★ elements in the stash do not auto-merge. Every drop target is bare and 1★, so every drop applies. Markers `impact:<element>` fire once each.
- Material for k: beats 2 and 7 are the apply punches for the "fifteen seconds" pitch cut.
- Watch for: a "Bestiary unlocked" toast on every apply (six toasts at the top over the shop); keep the camera on the board, which the per-beat `focus: board:N` does. A missing `impact:<element>` marker means that drop was refused; check the stars and the merge.
