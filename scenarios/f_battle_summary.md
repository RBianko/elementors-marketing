---
name: f_battle_summary
voice: ninja
seed: 61
round: 8
level: 5
gold: 14
dice: ["fire", "ice", "wind"]
board: [{"slot": 0, "unit": "reptile", "element": "fire", "stars": 2}, {"slot": 1, "unit": "slime", "element": "ice", "stars": 1}, {"slot": 2, "unit": "insect", "element": "fire", "stars": 1}, {"slot": 3, "unit": "plant", "element": "wind", "stars": 1}, {"slot": 4, "unit": "beast", "element": "fire", "stars": 1}]
stash: []
cursor_start: [700, 520]
---
1. idle 0.6 — "Okay. This reptile is supposed to be mid."
2. hover board:0 1.2; idle 0.5 {focus: board:0} — "Fire, two stars. Nothing special."
3. battle hold=0.2 speed=4 {focus: battle} — "Let's see."
4. summary focus=dps:0 hold=0.3; hover recap:0 1.5; drift 40,30; idle 1.2 {at: summary:focus, punch, zoom: 2.4, align: right} — "...Four hundred and seventy?! Okay. Okay okay okay."
