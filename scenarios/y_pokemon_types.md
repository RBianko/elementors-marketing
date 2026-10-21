---
name: y_pokemon_types
voice: none
hook: curiosity
angle: the element is the creature's type: one reptile body, four elements, four different moves, read straight off the tooltip
mood: recognition -> curiosity -> rhythm -> choice
promise: four bare reptiles take fire, ice, light and wind one after another, and after each impact the tooltip shows the move that element gave it: burn, freeze, heal, extra strike
button: "WHICH TYPE NEXT?"
render: plain
seed: 11
round: 6
level: 4
gold: 10
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "reptile", "element": "bare", "stars": 1}, {"slot": 1, "unit": "reptile", "element": "bare", "stars": 1}, {"slot": 2, "unit": "reptile", "element": "bare", "stars": 2}, {"slot": 3, "unit": "reptile", "element": "bare", "stars": 2}]
bench: []
stash: [{"element": "fire", "stars": 1}, {"element": "ice", "stars": 1}, {"element": "light", "stars": 2}, {"element": "wind", "stars": 2}]
cursor_start: [760, 520]
---
1. wander 0.4 r10; hover board:0 0.4 {focus: board:0}
2. wander 1.2 r4 {focus: tooltip, zoom: 1.4}
3. drag stash:0 -> board:0; wait 0.9 {at: impact:fire, punch, focus: board:0}
4. drift 70,-50; hover board:0 0.3 {focus: board:0}
5. wander 1.6 r4 {focus: tooltip, zoom: 1.4}
6. drag stash:1 -> board:1; wait 0.9 {at: impact:ice, punch, focus: board:1}
7. drift 70,-50; hover board:1 0.3 {focus: board:1}
8. wander 1.6 r4 {focus: tooltip, zoom: 1.4}
9. drag stash:2 -> board:2; wait 0.9 {at: impact:light, punch, focus: board:2}
10. drift 70,-50; hover board:2 0.3 {focus: board:2}
11. wander 1.6 r4 {focus: tooltip, zoom: 1.4}
12. drag stash:3 -> board:3; wait 0.9 {at: impact:wind, punch, focus: board:3}
13. drift 70,-50; hover board:3 0.3 {focus: board:3}
14. wander 1.6 r4 {focus: tooltip, zoom: 1.4}
15. drift -80,40; wander 2.2 r12 {focus: board, zoom: 1.0}

## Brief
- Angle: Pokémon types read the other way round. In Pokémon the type comes with the creature; here the player gives the type, and the element rewrites the creature's move. One body, the reptile, takes four elements, and after each impact the tooltip's element box names what changed: fire burns, ice freezes, light heals the neighbours, wind strikes twice. The e mould (the mechanic on a row of creatures, captions name what happens) plus the tooltip as proof.
- Hook: curiosity, silent. 0:00 POKÉMON TYPES? over the bare reptile's tooltip (no element box yet); the question is answered by the first impact at about 2 s.
- Correction to the backlog row (2026-10-20): the game has no element-vs-element type chart and no counter rule (pwn-zz `element_skill_modifiers.tsv`: each element modifies the creature's own skill). "If you remember type charts, you already know this game" and the counter-pick fight would claim a mechanic that does not exist, so the angle moved from "type chart" to "the element is the type and changes the move".
- Emotion arc: recognition, curiosity, rhythm over four applies, choice at the end.
- Proof frame: four `impact:<element>` punches on board:0-3, each followed by a hover beat (the cursor drifts off the unit and back, since the tooltip does not open under a parked cursor after an apply) and a wander-only tooltip beat (`focus: tooltip`, zoom 1.4) where the element box shows the new move. The tooltip beats are wander-only on purpose: align.py frames a region only on a beat without other actions; with a hover in the same beat the camera followed the cursor and the tooltip stayed out of frame (first render, 2026-10-20).
- Captions (silent, music under, y 0.72, no trailing periods; the element word in its colour from n): POKÉMON TYPES? (beat 1) · FIRE TYPE (impact 1) · BURNS (tooltip 1) · ICE TYPE · CAN FREEZE · LIGHT TYPE · HEALS · WIND TYPE · EXTRA STRIKE · SAME CREATURE (beat 10) · WHICH TYPE NEXT? held to the end.
- Button: WHICH TYPE NEXT? held over the four reptiles, the silent-cut ending; it invites the six-element answer in the comments.
- Tooltip text (pwn-zz `i18n/translations.csv`): fire "Strikes apply 10 burn stack to the primary and the 2nd enemy"; ice "30% chance to freeze the proc target for 0.5s"; light "Each hit heals adjacent allies +5 HP"; wind "20% chance for an extra strike on the front enemy". The captions stay inside the tooltip: CAN FREEZE for the 30%, EXTRA STRIKE for the 20%.
- Voice: none. Silent cut only, the shape that broke out (e silent).
- Alt hook (contrarian, silent): 0:00 TYPES COME BUILT IN? over the same tooltip; SAME CREATURE stays at beat 10, the held button becomes YOU PICK THE TYPE?.
- Render: plain. Four reptiles: two bare 1★ and two bare 2★, so no three identical units merge at setup; fire and ice 1★ for the 1★ pair, light and wind 2★ for the 2★ pair (only a bare unit of the same star takes an element). Once elemented, every unit has its own key, nothing merges. Level 4 for the four field slots.
- Assumptions: reptile has animated art for fire, ice, light and wind at 1★ and 2★ (fire at 1★ in c and l, 2★ in n). The 2★ element box shows the same text as 1★, possibly with bigger numbers. `roll: true` (default) rolls silently at setup and the `stash:` key replaces the faces. Round 6 is a shop round with nothing scripted around it.
- Critic (round 1, REVISE): STRIKES TWICE overclaimed the 20% (now EXTRA STRIKE), FREEZES now CAN FREEZE, the alt changed the body instead of the button (fixed). Round 2: SHIP. The note that POKÉMON in the hook is third-party IP stands: fine organic, keep it out of a paid cut.
- Watch for: a refused drop (no `apply:<el>` before the `impact:`) means a star mismatch. If the tooltip does not open in a tooltip beat, raise the drift or add a `hover` off the unit first. A "Bestiary unlocked" toast is off by default.
- Render result 2026-10-20 (pwn-zz main, second render): all four applies land, every tooltip shows its element box (Passive bonus line) for fire, ice, light and wind. The first render (tooltip beats with a hover in them) left the tooltip out of frame and was discarded.
- Build result 2026-10-20: timeline `y_pokemon_types 9x16`, 1599 frames (26.7 s), no music. Five ripple cuts after the build (source tail of each tooltip and the empty rail before each drag, 413 frames). The camera on each drag is set by hand from the cursor track (stash to the target unit), since after the cuts it held on the tooltip rail. The tooltip captions sit at y 0.86 because the Passive bonus line is at 0.72 in the tooltip shot; the TYPE captions are in the element colours of n. The last shot zooms out to the whole board (scale 3.16) so the four reptiles are in frame under WHICH TYPE NEXT? (112 frames). Audio (user call 2026-10-20: the game's own background music jumped at every cut): game audio at -10 dB with no fades at the cuts, the game's round music (`pwn-zz/sound/round.mp3`, user call: round, not combat) at -2 dB as one continuous clip under the whole cut, 60-frame fade-out. A rerun of align.py or palmier_build.py drops all of this.
- Exported 2026-10-20: `exports/y_pokemon_types.mp4`, 1080x1920, 26.7 s, round music.
