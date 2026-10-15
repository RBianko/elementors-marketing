# Elementors: what the game does and what the harness can film

Source of truth is the game repo `/Users/a1/DEV/pwn-zz` (`documentation.md`, `data/balance/*.tsv`, `tests/shot_movie.gd`). Numbers below were read on 2026-10-11; re-check when a short depends on an exact value.

## Vocabulary the voice line may use

| Say | Means |
|---|---|
| element | fire, ice, wind, water, light, venom (the 6 playable in the demo). Nature, storm, shadow, arcane, blood, power, chaos exist in data but players cannot get them; they render with a generic burst only. |
| unit / creature | slime, insect, plant (T1, 3g) · beast, reptile (T2, 4g) · ghost (T3, 5g) · demon (T4, 6g) · dragon (T5, 7g). Weapon, creation, elemental, giant, god exist but are not recruitable. |
| bare | a unit with no element yet. Only a bare unit of the same star takes an element. Applying is permanent and never changes the star. |
| star | 1★, 2★, 3★ (max). Three identical units (same type, same element or both bare, same star) merge automatically into the next star. Bench and board are one pool. Cascades happen in one pass: a fresh 2★ with two 2★ copies becomes 3★ immediately. |
| stash | 8 slots on the left for rolled elements. Three identical elements auto-merge into the next star of that element. |
| roll (dice) | the ROLL button throws element d12 dice into the stash. First roll of a round is free, then 4g, 8g, 16g. 1 die in rounds 2-5, 2 in 6-10, 3 from round 11. |
| reroll (shop) | REROLL button, 2g, refreshes every visible shop card. Hovering it shows tier odds for this level and the next. |
| level | LEVEL UP button, 4g for 4 XP. Shop slots: 2 at levels 1-3, 3 at 4-7, 4 at 8-9, plus one trailing bonus slot (index 4). Field cap: 1,2,3,4,4,5,5,6,6. |
| gold | +5 per round start, +1 win, streak 1/2/3 at 2/4/6 wins, interest 1 per 10 capped at 5. Sell refunds half of cost x 3^(star-1). |
| lucky roll | the special offer in the shop bonus slot. 12% per refill from round 1, 18% from round 5, 20% from round 11; pity forces one after 5 dry rounds. Kinds: `elem_1star` (rounds 1-4, elemented 1★), `echo_1star` ("COPY!"), `echo_2star` (copy of a 2★ you own, "COPY!", merges to 3★ on buy), `two_star_bare` ("TWO STAR!"), `tier_jump` ("RARE TIER!"). Reveal plays the `lucky_roll` sound and rainbow bursts; `echo_2star` and `tier_jump` also flash the screen edges rainbow and shake. |
| synergy | each board unit adds 1 to its type and 1 to its element (bare adds nothing to element). Thresholds 2/3/4 on both ladders. Tags above the backpack, gold/silver/bronze by rank. Fire 4: burn stacks every second. Ice 4: freeze all enemies 3 s at start. Light 3: revive once. |
| round / stage | 15 rounds, 5 per stage. Label "Stage 3-3" = round 13. Round 8 = Stage 2-3. |
| late game | rounds 13-15 (Stage 3-3 .. 3-5), Bandit creeps and the Bandit Boss at 15. Mid game is 6-10, early is 1-5. |
| boss | rounds 5 (Goblin Boss), 10 (Golem Boss), 15 (Bandit Boss). Winning 5 or 10 offers a pick of 3 items. |
| PvP | rounds 2-3, 6-7, 9, 11-12, 14 fight other players' saved boards. Creeps at 1, 4, 8, 13. |
| HP | trainer HP 30, a lost boss round costs 10. |

Tier odds per level (T1..T5): L1-2 100/0/0/0/0 · L3 75/25 · L4 60/30/8/2 · L5 50/35/13/2 · L6 40/35/20/5 · L7 25/35/30/10 · L8 15/30/35/15/5 · L9 10/25/35/20/10. Regular shop offers are always bare 1★.

Screen events worth a punch: element impact (apply + suction, 0.48 s after the drop), star-up sparkle with an edge glow (medium for 2★, strong for 3★ with a shake), lucky-roll reveal (rainbow bursts), 3★ cascade, battle result overlay, recap numbers.

## What the harness films (`tests/shot_movie.gd`)

Frontmatter keys passed through: `seed`, `round` (default 3), `level` (default max(3, board size)), `gold` (10), `dice` (fire/ice/wind), `roll` (true), `board`, `bench`, `stash`, `offer`, `cursor_start`, `settle_s`, `save`, and the player-pool keys `pick`, `stage`, `exclude`, `min_units`, `require_bare`.

Actions: `wait s`, `idle s`, `wander s rN`, `drift dx,dy`, `hover <target> [hold]`, `click <target>`, `drag <from> -> <to> [hold]`, `battle hold= speed= open=`, `summary focus=dps:N hold=`. `buy` is the same code as `click`.

Targets: `board:N`, `bench:N`, `stash:N`, `shop:N` (bonus slot is `shop:4`), `recap:N`, `syn:<element|type>` (a synergy tag; hovering it opens the ladder tooltip in the left rail), `loot:N` / `loot:take` (boss loot cards and the Take button), `board:bare|best|any|empty`, `node:%RollButton`, `node:%RerollButton`, `node:%LevelUpButton`, `node:%FreezeButton`, `node:%EndRoundButton`. Region names (`shop`, `board`, `synergies`, `bench`, `stash`, `dice`, `battle`, `roll`, `gold`, `level`, `hp`, `tooltip`) work only in `focus:`, never as click targets.

Markers the edit can land on: `warmup`, `beat:N`, `drag_start:<el>`, `drop:<el>`, `apply:<el>`, `impact:<el>`, `star_up` (one per promotion), `cascade_end`, `battle_start`, `battle_open_end`, `battle_end`, `summary`, `summary:focus`, `summary:dps:N`, `summary:kills:N`, `summary:unit:N`, `summary:damage`, `summary:synergies`. No marker fires for a click, a buy, a refused drop or a stash merge; use the default `beat:N` for those.

### Hard limits, and the workaround for each

- **A shop card is armed, not placed.** `offer: {"kind": "echo_2star", "unit": "reptile", "element": "fire", "stars": 2}` in the frontmatter sets `RunState.debug_next_offer`; the next shop refresh puts exactly that card into the bonus slot `shop:4` and clears the override. The regular slots still roll from the seed. Kinds: `elem_1star`, `echo_1star`, `echo_2star`, `two_star_bare`, `tier_jump` (the last two are always bare). The setup refill runs before the harness arms the offer, so the card appears on the first refresh the scenario triggers: `click node:%RerollButton` (2g, full reveal FX, rainbow and shake for `echo_2star` and `tier_jump`). The same override is in the game's debug menu as "Next offer / Arm", for checking a card by hand. Fallbacks when `offer:` is not enough: `save: <path>` with a hand-written save JSON (`docs/save-schema.md` in pwn-zz) or a seed search.
- **A regular shop card is a seed hunt.** `offer:` only fills the bonus slot, which in the real game always carries a stamped special kind; a plain card there reads as fake. For a bare unit in a regular slot (on the first, second or third reroll), scan seeds with `tools/shop_scan.gd` (`docs/PIPELINE.md`): headless, a few seconds for 500 seeds.
- **The cascade lands where the element was applied.** Apply on a bench unit and the 2★ and 3★ end on the bench at the bottom of the screen; apply on the board (move the bare unit to an empty board slot first, which may need a higher `level:` for the field cap).
- **The reveal FX only plays on a refresh after mount.** A card already in the shop at setup shows the stamp but no rainbow burst. For the "YESSS" moment, the reroll click is the shot.
- **Buying lands on the bench**, never straight on the board (no right-click). A merge on buy still happens, with `star_up` markers, even with a full bench.
- **`roll: true` is a silent setup roll**: faces land in the stash before the screen exists; with a `stash` key the stash is then replaced. To film a dice throw set `roll: false` and `click node:%RollButton`; that throw is physics, faces are not repeatable.
- **Real player boards** (`board: supabase`): stages 1-3 only, at most 5 units, mvp types and demo elements only. `stage: [3, 3]` picks rounds 11-15; pin with `pick: <id>` or set `round:` explicitly. A 6-unit board must be hand-written.
- **Beast/fire has static art only.** Avoid it as the hero unit.
- **Setup units merge like bought ones.** Three identical bare units of one star in `board:`/`bench:` collapse into the next star while the harness places them (the log says "field cap refused board:N, forcing it"), and a 1★ element is then refused on the 2★ body. A row of six "the same unit" needs six types or mixed stars; e_six_reptiles_six_elements lost its first render to this on 2026-10-14.
- **A boss win shows Boss Loot first**: `battle_end` fires on the loot pick, and the result overlay (and `summary`) only comes after `click loot:N; click loot:take`.
- A fight is ~39 s at speed 1; `speed=4..6` for battle beats. `open=N` plays the first N s of the fight at speed 1 and then switches to `speed` (marker `battle_open_end`), for an opening that has to read, like the Ice-4 freeze (3 s). The harness never waits for speech: the beat's actions must last at least as long as the line.
