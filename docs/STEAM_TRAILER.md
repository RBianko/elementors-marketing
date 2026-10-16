# Steam trailer v5: mechanics showcase

Replaces `elementors_trailer_v4.mp4` (2026-08-04, `pwnz-assets/steam_capsule/videos/project/`, cut from screen recordings of an older build). Built only from the renders already made for the shorts, so it shows the current build at 4K source.

Neutral store-page trailer: no streamer voice, no hooks, no stream-clip framing. Gameplay from the first frame, one mechanic per shot, a short plate per mechanic, logo and wishlist at the end. It autoplays muted on the store page, so the plates carry the meaning and the music only sets the pace.

## Format

- 1920x1080, 60 fps, about 45 s. Timeline `steam_trailer 16x9` in `palmier/ELEMS.palmier`.
- Music: Action 3 Loop, 150 BPM (24 frames a beat), from 0.44 s of the source so the downbeats land on the cuts; every cut sits on a multiple of 24 frames. Fade out over the last 90 frames.
- Game audio from the renders under the music at -8 dB, so impacts, merges and the throw are heard.
- Plates: BoldPixels, uppercase, white with a black outline, at y 0.86, `slideUp`, the same family as v4.
- Camera: every shot is a slow push-in (zoom grows 6% over the shot) centred on the marker focus of the moment, so the small 1280x720 UI reads at 1080p.

## Shots

Source times are seconds in the render; length in frames.

| # | Frames | Source | Moment | Zoom | Plate |
|---|---|---|---|---|---|
| 1 | 48 | `e_six_reptiles_six_elements` 16.88 | ice impact | 1.8 on impact | |
| 2 | 48 | `c_one_buy_three_star` 18.3 | 3★ merge flash | 1.8 on impact | |
| 3 | 48 | `b_fourth_ice_freeze` 23.0 | PvP, enemies frozen at the start | 1.3 | |
| 4 | 48 | `j_venom_golem_boss` 15.6 | boss fight hit | 1.25 | |
| 5 | 96 | black + logo | title | | logo |
| 6 | 192 | `l_dice_decide` 5.6 | live dice throw | 1.5 on dice | ROLL ELEMENT DICE |
| 7 | 144 | `l_dice_decide` 12.6 | water die onto a bare creature | 1.6 on impact | EVERY FACE IS AN ELEMENT |
| 8-13 | 6 × 72 | `e_six_reptiles_six_elements`, each impact −0.55 | fire, ice, wind, water, light, venom | 1.7 on impact | ANY ELEMENT ON ANY CREATURE, then 6 ELEMENTS × 8 CREATURES |
| 14 | 216 | `c_one_buy_three_star` 16.9 | apply, 2★ then 3★ cascade | 1.6 on impact | THREE OF A KIND MERGE UP |
| 15 | 96 | `h_lucky_roll_three_star` 5.8 | lucky roll reveal, COPY! card | 1.6 on shop | HUNT THE LUCKY ROLL |
| 16 | 120 | `h_lucky_roll_three_star` 10.6 | buy merges into 3★ | 1.6 on star-up | |
| 17 | 144 | `b_fourth_ice_freeze` 13.2 | four ice, synergy lights up | 1.5 on impact | STACK SYNERGIES |
| 18 | 240 | `b_fourth_ice_freeze` 25.0 | PvP at x2 vs a real board | 1.1 | FIGHT REAL PLAYERS' BOARDS |
| 19 | 240 | `j_venom_golem_boss` 14.2 | Lava Lord boss fight | 1.15 | BEAT THE BOSSES |
| 20 | 300 | `m_flip/01..12` 1.4 | twelve real round-15 boards, accelerating 48 → 12 frames | 1.35 on board | NO TWO RUNS THE SAME |
| 21 | 300 | `m_flip` cycle at 6 frames, dimmed 70% | outro | | logo, WISHLIST ON STEAM |

Avoid `j_venom_golem_boss` 13.4-13.9 (the fight intro fades through black) and `b_fourth_ice_freeze` before 22.5 (the board still slides from the table into the arena).

## Build

`tools/trailer_build.py` creates the timeline over the Palmier MCP endpoint from the table above and can export (`--export exports/steam_trailer_v5.mp4`). First build 2026-10-16: timeline `steam_trailer 16x9`, 2712 frames (45.2 s), exported.
