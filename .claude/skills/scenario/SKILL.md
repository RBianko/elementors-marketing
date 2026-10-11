---
name: scenario
description: Turn a raw idea for an Elementors short (one sentence in Russian or English, a chat note, a bullet list) into a produced scenario markdown for /short — the angle, the hook, the beat-by-beat actions the Godot harness can film, streamer-style voice lines, captions, mood and an A/B variant, plus a producer brief. Use whenever the user asks for a scenario, a script, hooks, voice lines or "сценарий / скрипт / хуки для шортса", pastes a rough moment description ("делаем ролл, попадается lucky roll, мерджим в 3 star"), or asks to turn a gameplay moment into a short, even if they do not say "scenario".
---

# /scenario

Input is a raw moment. Output is `scenarios/<name>.md` that `/short` can build without a rewrite, and a brief that says why the short should work. Four hats, in order: **producer** (angle, hook, structure), **streamer** (voice lines), **harness engineer** (actions that render), **editor** (humanize, lint, A/B), then an outside **critic** (the `shorts-critic` agent). Keep the hats separate; the usual failure is a voice line written by the engineer or a beat written by the producer.

Repo root `/Users/a1/DEV/elementors-marketing`. Read `references/game.md` before writing a single beat (mechanics, vocabulary, what the harness can and cannot film) and `references/hooks.md` before choosing the hook (hook types, structure, VO authenticity rules, caption rules).

## Arguments

- `/scenario <raw text>` — produce one scenario from the text.
- `/scenario <raw text> --variants 3` — write the main scenario plus two A/B variants as separate files. A variant is the same short with a different first line, 0:00 caption and button: `scenarios/<name>__<hooktype>.md` with `base: <name>` in the frontmatter and beats identical to the base. `/short` reuses the base render for it and only voices, aligns and builds. Without the flag the alt hooks live in the brief only.
- `/scenario <raw text> --name <slug>` — force the file name; otherwise `<letter>_<slug>` continues the `a..g` series in `scenarios/`.
- `/scenario rehook <name>` — keep the beats of an existing scenario, rewrite only the hook line, the button line and the captions.
- `/scenario brief <name>` — print the brief block of an existing scenario.

## Steps

1. **Intake.** Pull out of the raw text: the game moment (what happens on screen), the emotion the user wants (hype, disbelief, smug, copium), explicit lines they already hear in their head (keep them verbatim as anchors, e.g. "YESSSS", "my best board so far"), the stage of the run, any constraint (voice, length, platform). What is missing, decide yourself and state it in the brief as an assumption; do not ask.

2. **Producer: pick the angle and the structure.** From `references/hooks.md` choose one hook type for the main cut and a different one for the alt. Write the one-sentence promise of the short ("a 2★ copy shows up in the bonus slot at round 14 and the board goes 3★ on the spot"). Decide the structure: cold open (payoff inside 5 s) or slow build (setup, tension, payoff, button) and where the proof moment lands in seconds. Decide the button: the last line that makes the viewer replay, comment or try it. No CTA of any kind, no plate, no "download now", no "it's free"; the game name may be said once at most, as a streamer would, or not at all.

3. **Streamer: write the lines.** One line per beat, 3-12 words, English, spoken not written. Reactions before explanations. Self-talk, stacked "okay okay okay", mid-sentence stops, hedges ("this is probably fine"), chat address at most once. Numbers said the way a player says them ("four seventy" not "470 damage"). No adjectives from an ad ("amazing", "epic", "satisfying"), no feature lists, no perfect grammar. Every line answers "what would the player blurt out right now", not "what does the viewer need to know". The user's anchor lines go in untouched.

4. **Harness engineer: write the beats.** Use only actions, targets, markers and frontmatter keys from `references/game.md`. The visible event of each line is on screen while the line is said. The punch beat is the on-screen event the hook promised, with `at:` set to the marker the harness emits for it (`impact`, `star_up`, `summary:focus`), `punch`, and a `focus`. Give every voiced beat enough action time for its line; silent beats after a punch line are where the line lands. A reaction never fires on the frame of the event: after a roll, a drop, a merge, a reveal or a tooltip with the new stats, the player first looks, then reacts. Budget about 1 s between the event and the line (`align.py` starts a punch line 60 frames after the punch), so a punch beat needs the line plus 1 s of action after its marker. Set up the frontmatter so the moment is reachable: board, bench, stash, gold, round, level, seed. When the moment needs a shop card (lucky roll, a specific unit), arm it with the `offer:` key and place the card with a reroll click, as `references/game.md` describes; a card that is already in the shop at setup shows no reveal FX.

5. **Editor: humanize, lint, A/B.** Run the `humanizer` skill in embedded mode on the voice lines and the brief: no AI vocabulary, no rule-of-three stacks, no dashes inside lines, no tidy explanations. Then:
   ```
   python3 -I tools/scenario.py scenarios/<name>.md --beats
   python3 -I tools/scenario_lint.py scenarios/<name>.md
   ```
   Fix every WARN that is not a deliberate slow build. With `--variants`, write each variant file now (same beats, `base:` set, only line 1, the 0:00 caption and the button differ) and lint it too; the lint refuses a variant whose beats drift from the base.

6. **Critic.** Spawn the `shorts-critic` agent on the file (Agent tool, `subagent_type: shorts-critic`, prompt = the path). Agents from `.claude/agents/` register at session start; if the type is not available, spawn `general-purpose` with the body of `.claude/agents/shorts-critic.md` as the prompt followed by the path. It returns SHIP or REVISE with up to three rewrites. On REVISE apply the rewrites you agree with, re-lint, run the critic once more. After two rounds stop either way and carry any remaining FAIL into the brief as "Critic: ...". The critic is a second pair of eyes, not an authority: a rewrite that breaks the game facts or the user's anchor lines is refused with a one-line reason in the brief.

7. **Report** in chat: file path, the hook line, the promise, the punch second, the render route (plain / save file / seed hunt) and the open questions, in five lines or fewer. Then stop; `/short <name>` is the next command, not yours to run.

## Output file

`scenarios/<name>.md`, in this exact shape. The frontmatter keys `hook`, `angle`, `mood`, `promise`, `button`, `render`, `base` are edit-side and never reach the harness; the rest is the harness setup.

```md
---
name: h_lucky_roll_three_star
voice: ninja
hook: need-first
angle: the one card you were missing shows up in the bonus slot at round 14
mood: want -> disbelief -> hype -> smug
promise: a 2★ fire reptile lands in the lucky slot on a reroll and the board goes 3★ on the spot
button: "My best board so far. Not even close."
render: offer
seed: 83
round: 14
level: 7
gold: 24
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "reptile", "element": "fire", "stars": 2}, ...]
bench: [{"unit": "reptile", "element": "fire", "stars": 2}]
stash: []
offer: {"kind": "echo_2star", "unit": "reptile", "element": "fire", "stars": 2}
cursor_start: [700, 520]
---
1. idle 0.4; hover board:0 0.6 {focus: board:0} — "Round fourteen. I need one more fire reptile."
2. hover node:%RerollButton 0.4; click node:%RerollButton; wait 0.7 {focus: shop} — "Two gold. Come on."
3. hover shop:4 0.8; idle 0.3 {punch, focus: shop:4, zoom: 2.0} — "...wait."
4. click shop:4; wait 0.5; idle 1.2 {at: star_up, punch, focus: board:0} — "YESSSS."
5. hover board:0 1.2; idle 0.8 {focus: board:0} — "That's the three star."
6. drift 30,20; hover board:2 0.6; idle 2.0 {focus: board} — "My best board so far. Not even close."

## Brief
- Angle: late game, the player is one copy short of a 3★ carry and the lucky slot hands it over on a two-gold reroll.
- Hook: need-first. The first line names the one missing piece, the shop answers it inside 7 s.
- Emotion arc: want, disbelief, hype, smug.
- Proof frame: two punches. Beat 3 on the rainbow reveal in shop:4, beat 4 on the `star_up` marker with the 3★ sparkle and edge glow on board:0.
- Button: "My best board so far. Not even close." Flex with a dare in it.
- Captions: ROUND 14 · ONE MORE · COME ON · WAIT · YESSSS · THREE STAR · BEST BOARD
- Alt hook (contrarian): "Chat said sell the second reptile. Chat." Alt button: "Sell it, they said."
- Alt hook (number): "Twenty percent. That's the odds on this slot." Alt button: "Twenty percent. Sure."
- Render: offer route. `offer:` arms the bonus slot, the reroll click in beat 2 places the card with the full reveal FX. No save file, no seed hunt.
- Assumptions: price of a 2★ echo offer is about 17 gold (4 × 3 × 1.4) and the reroll costs 2, gold 24 covers both; the buy merges board:0 + bench:0 + the card and the 3★ lands on board:0 (board-first, lowest slot). Beast is ice, not fire, because beast/fire has static art.
- Watch for: the reroll also rerolls slots 0-2, fine; if `star_up` is missing from the render, the buy was refused (gold) or the merge landed on the bench.
```

Rules the parser imposes: beat lines start with `N. `, actions are `;`-separated, options in one `{}`, the line after ` — ` in straight or curly quotes. Nothing else in the file may start with a number and a period, so the brief uses bullets. Every voiced beat without an explicit `at:` lands on `beat:N`.

## What good looks like

- The hook line is something a player would say, and it names the stake ("I need one more", "this is supposed to be mid").
- The payoff is a thing the camera can punch on, and the line right after it is a reaction, not a caption.
- The button is a line that invites a reply ("tell me that's not the best board you've seen today"), not a slogan.
- The brief fits on one screen and tells `/short` exactly what has to be true at render time.
- Two shorts from the same moment differ in hook and button, not in beats.

## A/B variants

A variant file is the base file with three edits: the first voice line, the 0:00 caption in the brief, the button. Frontmatter adds `base: <base name>` and changes `hook:` and `button:`. Beats, markers, punches and the harness setup are byte-identical; the lint checks that. Name by hook type: `h_lucky_roll_three_star__contrarian.md`. Two variants of one moment never differ in the body, otherwise the test says nothing.
