# Content plan: wave by wave

The working plan for producing the shorts in `docs/SCENARIO_BACKLOG.md`. One row per cut, status updated as work lands. Dates are absolute. Rules and evidence stay in the backlog; this file only says what is next and what is done.

Status values: `todo` · `scenario` (markdown written and linted) · `rendered` · `cut` (timeline built) · `posted` · `dropped`.

Every rendered moment ships as two cuts: the streamer-voice cut and a silent text-only cut under music. Both count as one row until posted; post them a few days apart.

## Wave 1: renderable today

| # | ID | Cut | Needs | Status | Notes |
|---|---|---|---|---|---|
| 1 | e | Six creatures, six elements | one render, six drags; silent cut first | posted | `scenarios/e_six_reptiles_six_elements.md`, 2026-10-14; timelines `e_six_reptiles_six_elements 9x16 v3` (voiced, Liam placeholder until the Ninja track is hand-made) and `... silent A 9x16`; material for k |
| 2 | c | 1→2→3★ cascade | one render, seed 34, three rerolls, bare reptile bought, fire applied on the board | posted | `scenarios/c_one_buy_three_star.md`, 2026-10-15; timelines `c_one_buy_three_star 9x16` (voiced, hand-recorded Lewis Moore read) and `... silent 9x16` (captions only, music still to lay); 30.5 s after the pace pass; material for k |
| 3 | b | Fourth ice, everyone frozen | one render, PvP vs a real board, fight at x2 | cut | `scenarios/b_fourth_ice_freeze.md`, 2026-10-15; timelines `b_fourth_ice_freeze 9x16` (voiced, Liam placeholder until a hand read) and `... silent 9x16` (captions only, music still to lay), 31.3 s; opponent TheLost12; material for k |
| 4 | l | Dice decide | one render, `roll: false`, live throw | posted | `scenarios/l_dice_decide.md`, 2026-10-16; silent cut only (user call): timeline `l_dice_decide 9x16`, 23.3 s, captions only, music still to lay; dice as the build, the throw as luck, the placement as skill; faces water, venom, venom; seed 12 repeats the throw |
| 5 | m | Round 1 vs round 15 | one round-1 render, twelve flip renders, accelerating cuts | posted | `scenarios/m_round_one_round_fifteen.md` + `m_flip_round_fifteen.md`, 2026-10-16; silent, no fight: three real round-1 boards, then twelve real round-15 boards accelerating and cycling to the end, logo and WISHLIST ON STEAM on the dimmed cycle; timeline `m_round_one_round_fifteen 9x16`, 18.8 s, captions and music (Action 3 Loop, downbeat on the ROUND 15. cut), exported |
| 6 | k | Fifteen seconds of Elementors | edit from l, e, c, b; silent | posted | `scenarios/k_fifteen_seconds.md`, 2026-10-17; silent cut only (user call); timeline `k_fifteen_seconds 9x16`, 14.6 s, music laid, exported `exports/k_fifteen_seconds.mp4`; six shots: throw, three impacts, 3★ cascade, freeze; captions explain the mechanics: 15 SECONDS. · MY AUTOBATTLER. · WATER. ICE. VENOM. · MATCH THREE, · STAR UP. · ICE BUILD: · FREEZES EVERYONE. · WHICH BUILD NEXT? |
| 7 | a/h/j | Silent re-cuts | edit only, existing renders | dropped | user call 2026-10-17: a carries only the voiced reaction, h repeats the 3★ cascade of c and k, j was not wanted either |
| 8 | n | Loop: apply and suction | one render, 2★ applies | posted | `scenarios/n_apply_loop.md`, 2026-10-17; new render on the current build: six bare 2★ creatures take six 2★ elements (fire reptile, ice slime, wind insect, water dragon, light ghost, venom plant), opens on one die throw from l landing water, then the six applies starting with water, each shown to the end of its animation; timeline `n_apply_loop 9x16`, 18.6 s, music laid, ends on a fade with the logo and WISHLIST ON STEAM as in m, exported `exports/n_apply_loop.mp4`; captions ROLL AN ELEMENT, · DROP IT ON ANY CREATURE., each element named in its colour over its shot |
| 9 | e2 | Repost of e, new hook | edit only, silent A timeline copied | cut | 2026-10-18, per the first results: the captions change, after silent cut B of the e brief; 0:00 SIX GUYS · SIX ELEMENTS, then each impact as TYPE × ELEMENT with the element in its colour from n (REPTILE × FIRE · SLIME × ICE · INSECT × WIND · PLANT × WATER · GHOST × LIGHT · DRAGON × VENOM; Poppins-Bold 56, outline 10, popIn, y 0.72, two clips per pair centred by hand; user call 2026-10-18), then ANY CREATURE · ANY ELEMENT · PICK ONE as the verdict, no trailing periods (user call 2026-10-19); timeline `e_six_reptiles_six_elements silent B 9x16`, 29.2 s, no music (as A), exported `exports/e_six_reptiles_six_elements_silent_b.mp4` |

Order: 1, 2, 3 first (cheapest, and k is built from them), then 4, 5, then the edits 6, 7, 8.

## Wave 2: after the first posts

Needs a posting account with comments, a milestone, or a thing from the game side. Not before wave 1 is posted.

| ID | Cut | Gate | Status |
|---|---|---|---|
| o | This is TFT with dice | none; one render | cut |
| p | Find the three-star line | none; one render with a hold still | cut |
| z | One whole round, no cuts | none; one 60-90 s render, captions only | cut |
| y | Pokémon types, but it's an autobattler | none; one render | cut |
| u | How it started, how it's going | an old pwn-zz build that runs; account decision | todo |
| q | Which element on the dragon? | comments on the account; then one render per winning answer | todo |
| r | Real player's board, can it win? | `board: supabase`; a series, one per week | todo |
| s | Demo day trailer / milestone | the milestone | todo |
| t | Nobody cares about your autobattler | a real negative comment | todo |
| cr | Discovery creators outreach | cuts k, c, h posted; demo link | todo |

## Wave 3: needs things we do not have

| ID | Cut | Gate | Status |
|---|---|---|---|
| v | The dumb interaction | a found interaction, or a small one added to the game | todo |
| w | A streamer hits the 3★ | creator footage | todo |
| x | Trend / CapCut | one try at most, lowest priority | todo |

## Per-cut loop

1. `/scenario <idea>` → `scenarios/<id>_<name>.md`, lint, voice pass, critic.
2. `/short <name>` → render, voice, timeline. Then the silent variant: same timeline, VO track off, captions from the brief.
3. Export both, post the voiced cut first, the silent one 3-5 days later.
4. Log the row in the results table below after 7 days.
5. A cut that lands gets a repost with one change (speed, first line, caption). Each style gets two or three tries before it is called.
6. Cross-post to YouTube Shorts and Reels the next day, no watermark.

## Results

Filled after each post. Dates up to 2026-10-18 are the export dates (the posts went out the same day or the next); the numbers come from the user 7 days after each post. Followers per 1M views is the number that mattered in the data (about 290 is the median for gameplay hits); views alone said nothing.

| Date | ID | Variant | Platform | Views 7d | Likes | Comments | Steam followers Δ | Note |
|---|---|---|---|---|---|---|---|---|
| 2026-10-11 | h | voiced, ninja | YouTube Shorts + TikTok | | | | | |
| 2026-10-11 | h | voiced, ninja_chat | YouTube Shorts + TikTok | | | | | |
| 2026-10-11 | i | voiced, v3 | YouTube Shorts + TikTok | | | | | |
| 2026-10-11 | i | voiced, slime fire | YouTube Shorts + TikTok | | | | | |
| 2026-10-13 | j | voiced | YouTube Shorts + TikTok | | | | | |
| 2026-10-14 | e | silent A | YouTube Shorts + TikTok | ~7k | | | | best of wave 1 by far |
| 2026-10-15 | c | voiced | YouTube Shorts + TikTok | | | | | |
| 2026-10-16 | l | silent | YouTube Shorts + TikTok | | | | | |
| 2026-10-16 | m | silent | YouTube Shorts + TikTok | | | | | |
| 2026-10-17 | k | silent | YouTube Shorts + TikTok | | | | | |
| 2026-10-18 | n | silent | YouTube Shorts + TikTok | | | | | |

Snapshot 2026-10-18 (user, rough): e silent about 7k views, two other cuts about 1k (which ones not recorded), the rest 100-200 each. Wishlists: about 80 in total across all the shorts plus a few Reddit posts, not attributable per cut. Likes, comments and per-cut wishlist deltas are not tracked yet.

## Decisions pending

- Account for the progress series (u): game account or a personal one. The author's data says personal reads as "real indie" and gets rooted for.
- Old builds: which pwn-zz commit still runs and shows a visibly different game. Ask on the game side.
- Hate comments (t): only real ones, per the backlog. Revisit if the account gets none.
