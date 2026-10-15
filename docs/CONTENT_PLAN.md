# Content plan: wave by wave

The working plan for producing the shorts in `docs/SCENARIO_BACKLOG.md`. One row per cut, status updated as work lands. Dates are absolute. Rules and evidence stay in the backlog; this file only says what is next and what is done.

Status values: `todo` · `scenario` (markdown written and linted) · `rendered` · `cut` (timeline built) · `posted` · `dropped`.

Every rendered moment ships as two cuts: the streamer-voice cut and a silent text-only cut under music. Both count as one row until posted; post them a few days apart.

## Wave 1: renderable today

| # | ID | Cut | Needs | Status | Notes |
|---|---|---|---|---|---|
| 1 | e | Six creatures, six elements | one render, six drags; silent cut first | cut | `scenarios/e_six_reptiles_six_elements.md`, 2026-10-14; timelines `e_six_reptiles_six_elements 9x16 v3` (voiced, Liam placeholder until the Ninja track is hand-made) and `... silent A 9x16`; material for k |
| 2 | c | 1→2→3★ cascade | one render, seed 34, three rerolls, bare reptile bought, fire applied on the board | cut | `scenarios/c_one_buy_three_star.md`, 2026-10-15; timelines `c_one_buy_three_star 9x16` (voiced, hand-recorded Lewis Moore read) and `... silent 9x16` (captions only, music still to lay); 30.5 s after the pace pass; material for k |
| 3 | b | Fourth ice, everyone frozen | one render, battle speed 4 | todo | material for k |
| 4 | l | Dice decide | one render, `roll: false`, live throw | todo | faces are physics, not repeatable |
| 5 | m | Round 1 vs round 15 | two renders, hard cut in the edit | todo | |
| 6 | k | Fifteen seconds of Elementors | edit from 1-3, one spoken line | todo | after 1-3 are rendered |
| 7 | a/h/j | Silent re-cuts | edit only, existing renders | todo | a and h have two VO cuts already |
| 8 | n | Loop: apply and suction | edit only, 7-9 s, seamless | todo | from the a or i render |

Order: 1, 2, 3 first (cheapest, and k is built from them), then 4, 5, then the edits 6, 7, 8.

## Wave 2: after the first posts

Needs a posting account with comments, a milestone, or a thing from the game side. Not before wave 1 is posted.

| ID | Cut | Gate | Status |
|---|---|---|---|
| o | This is TFT with dice | none; one render | todo |
| p | Find the three-star line | none; one render with a hold still | todo |
| z | One whole round, no cuts | none; one 60-90 s render, captions only | todo |
| y | Pokémon types, but it's an autobattler | none; one render | todo |
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

Filled after each post. Followers per 1M views is the number that mattered in the data (about 290 is the median for gameplay hits); views alone said nothing.

| Date | ID | Variant | Platform | Views 7d | Likes | Comments | Steam followers Δ | Note |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

## Decisions pending

- Account for the progress series (u): game account or a personal one. The author's data says personal reads as "real indie" and gets rooted for.
- Old builds: which pwn-zz commit still runs and shows a visibly different game. Ask on the game side.
- Hate comments (t): only real ones, per the backlog. Revisit if the account gets none.
