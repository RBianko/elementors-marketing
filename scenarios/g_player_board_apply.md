---
name: g_player_board_apply
voice: ninja
seed: 71
board: supabase
stage: [2, 3]
pick: random
require_bare: true
gold: 12
dice: ["fire", "ice", "wind"]
stash: [{"element": "fire", "stars": 1}]
cursor_start: [700, 520]
---
1. idle 2.2 {focus: board} — "Random board from a real player."
2. hover stash:0 0.5 — "Fire goes... here."
3. drag stash:0 -> board:bare; wait 0.5; drift 30,28; idle 0.8 {at: impact, punch} — "Oh that's nasty."
4. hover board:best 1.2; idle 0.8 {focus: board:best} — "Still not the best thing on this board though."
