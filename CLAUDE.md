# elementors-marketing

Shorts for Elementors: scenario markdown → Godot render → ElevenLabs voice → Palmier timeline. `README.md` has the layout and the commands.

## Start of a session

1. Read `docs/CONTENT_PLAN.md`. The next cut is the first `todo` row of the lowest open wave; its gate must be met.
2. Read the backlog row for that ID in `docs/SCENARIO_BACKLOG.md` (template, moment on screen, hook direction, route).
3. Run `/scenario` with the row as the idea, then `/short`. Update the status column in the plan as each step lands.

## Where the research lives

| Question | File |
|---|---|
| What to film next and why | `docs/SCENARIO_BACKLOG.md` |
| Production status, results log, pending decisions | `docs/CONTENT_PLAN.md` |
| Hook timing, structure, caption and paid-cut rules, with sources | `docs/SHORTS_RESEARCH.md` → distilled in `.claude/skills/scenario/references/hooks.md` |
| How a streamer talks, transcribed reference clips | `docs/VOICE_REFERENCE_CLIPS.md` → distilled in `.claude/skills/scenario/references/voice.md` |
| Game mechanics and what the harness can film | `.claude/skills/scenario/references/game.md` (source of truth is the game repo `/Users/a1/DEV/pwn-zz`) |
| Harness contract, timing rule, edit tools | `docs/PIPELINE.md` |
| Raw material: Indie Game Luke transcript and the six sheet tabs as CSV | `docs/research/` |

New research goes next to these: raw material in `docs/research/`, the distilled rules into the skill references, the sources into `docs/SHORTS_RESEARCH.md`. A finding that changes what we film goes into the backlog, not into chat.

## Conventions

- No branches: commit to `main` when asked.
- Scenario files and voice lines are English; chat is Russian.
- Renders, voice files and Palmier media are not committed.
