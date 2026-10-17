---
name: k_fifteen_seconds
voice: none
hook: number
angle: the whole game in one breath: throw the dice, put the faces on creatures, merge to three star, freeze the lobby
mood: curiosity -> rush -> clarity -> want
promise: four real moments from the demo back to back inside twelve seconds, each one a different mechanic landing on screen
button: "WHICH BUILD NEXT?"
render: edit
---

## Brief
- Angle: a gameplay pitch with no explaining. Four punches from renders already made, one mechanic each, hard cuts on the music: the dice throw (l), the faces landing on bare creatures (l, e), one buy cascading into a 3★ (c), the fourth ice freezing the whole enemy board at the fight start (b). The viewer gets the loop of the game, roll, apply, merge, fight, in the time it takes to read the hook.
- Hook: number, silent. 12 SECONDS. · MY AUTOBATTLER. over the dice in the air; frame one is the throw already moving. The backlog line "Fifteen seconds of my autobattler." split into two captions, with the number set to the real length of the cut (12.4 s).
- Emotion arc: curiosity, rush, payoff, want.
- Proof frame: every shot is a punch on its marker. Shot 1 on `throw` (l 6.23), shot 2 on `impact:water` (l 13.52), shots 3-4 on `impact:ice` and `impact:venom` (e 17.38, 30.63), shot 5 on `impact:fire` then `star_up` (c 18.28, 18.92), shot 6 on the ice wash (b ≈24.0, timeline frame 1246 of the b silent cut).
- Shot list (60 fps, timeline frames, cuts on 24-frame multiples for Action 3 Loop at 150 BPM; source seconds in the render):
  - S1 0-144: `l_dice_decide` 5.75-8.15, ROLL click, three dice fly and land; focus the dice rect (x 2952, y 246, 852 × 1080).
  - S2 144-216: `l_dice_decide` 12.95-14.15, the water die onto the bare dragon, impact at frame 178; focus the impact.
  - S3 216-264: `e_six_reptiles_six_elements` 17.0-17.8, ice impact at frame 239.
  - S4 264-312: `e_six_reptiles_six_elements` 30.25-31.05, venom impact at frame 287.
  - S5 312-576: `c_one_buy_three_star` 17.4-21.8, fire die onto the reptile, impact at 365, star_up at 403, cascade_end at 463, the 3★ stats tooltip from 474.
  - S6 576-744: `b_fourth_ice_freeze` 23.4-26.2, PvP at x2, the ice wash at about 612, frozen to about 690.
- Captions (silent cut, music under, no VO, y 0.72, the Poppins highlightPop style of `palmier_build.py`; WATER. ICE. VENOM. split one word per impact shot): 12 SECONDS. (0-72) · MY AUTOBATTLER. (72-144) · WATER. ICE. VENOM. (150-312, one word per impact shot) · MATCH THREE, (318-400) · STAR UP. (420-576) · ICE BUILD: (582-630) · FREEZES EVERYONE. (630-690, while the ice holds) · WHICH BUILD NEXT? (690-876, 3.1 s). Nothing over the throw itself beyond the hook; the star-up and the freeze get their caption a few frames after the event.
- Button: WHICH BUILD NEXT? over the fight's tail (b 26.2-28.4, S6 extended to 300 frames). Asks the viewer to pick the next build showcase, a reply prompt that sets up a series.
- Camera: each shot reuses the framing its source cut already has at those source seconds (`renders/<src>/plan.json`, or `plan_silent.json` for b), so the 9:16 crops are the ones that already passed review. Push-in about 6% over each short shot, as in the trailer.
- Audio: Action 3 Loop from 0.44 s of the source, so the downbeats land on the cuts; game audio from the renders under it at -8 dB so the throw, the impacts, the merge and the freeze are heard.
- Render: edit only, no new render. Build with a one-off script over the MCP endpoint in the style of `tools/trailer_build.py` (9:16, 1080 × 1920), not `palmier_build.py`; set the 9:16 aspect after the first clip is placed and fix each clip's duration by frames.
- Voice: none, the voice pass skipped (no lines); silent cut only by the user's call (2026-10-17). A voiced cut on the same timeline can come later ("Fifteen seconds of my autobattler.").
- Alt hook (curiosity gap, silent): 0:00 DICE, BUT... · AUTOBATTLER. over the same throw; every other caption unchanged. Alt button: PICK ONE.
- Critic (round 1, REVISE): the middle captions taken as suggested (order fixed to the shots: water, ice, venom). The hook rewrite ONE THROW... · WHOLE LOBBY? refused: one throw does not freeze the lobby, the ice synergy does, on another board. The point about the untrue number taken: 15 became 12. MY AUTOBATTLER. kept, the genre word is the pitch of this template. The button ONE THROW. ONE. refused with its hook; BEST PART? instead of AGAIN?. Round 2: SHIP. The S6 freeze has no marker; checked by eye on frames, the wash is on from b 23.7-24.0 (frame 1246 of the b silent cut).
- Assumptions: the backlog row asked for the lucky roll reveal as the second punch; the dice throw (l) takes that place, because the dice are the build (user call 2026-10-16) and the COPY! card needs context a 1.5 s shot cannot give. Four punches instead of three, since the freeze is the only shot that shows a fight. Source times are the marker times in each `cursor.json`, which match the mp4 times (checked against the trailer cuts).
- Watch for: S6 unit tooltips open on the left from b 24.8; if one falls inside the 9:16 crop, end S6 at 24.8 and move BEST PART? onto 640-696. In S2 the TRASH panel flashes red at the top of the frame during the drag in l; crop it out or start at 13.1. In S5 the tooltip covers the left board from 20.1; fine, it is the stat proof.
- Build result 2026-10-17: timeline `k_fifteen_seconds 9x16` in `shorts/k_fifteen_seconds/`, 744 frames (12.4 s), built by a one-off script over the MCP endpoint (trailer style: one gameplay track, each clip's framing rebased from its source plan, a blurred backdrop under the b shot, game audio -8 dB, Action 3 Loop from 0.44 s at +1 dB with a 30-frame fade-out). The source framing of S3 sat off the ice impact (the voiced e cut follows the cursor), so S3 got its own push-in 1.6 → 1.7 centred on the impact. S6 checked: no unit tooltip inside the crop, the freeze reads from frame 612. Exported 2026-10-17: `exports/k_fifteen_seconds.mp4`, 1080x1920, 14.6 s.
- User revision 2026-10-17: the cut shows mechanics, so the captions explain instead of reacting. ONE BUY... · WAIT. THREE? became MATCH THREE, · STAR UP.; FROZEN. FROZEN. became ICE BUILD: · FREEZES EVERYONE.; the BEST PART? button dropped. Edited in the timeline over MCP.
- User revision 2026-10-17, second pass: WHICH BUILD NEXT? added at the end; S6 and the music extended to 816 frames (13.6 s), so the hook now reads 14 SECONDS. FREEZES EVERYONE. ends at 690, where the ice wears off.
- User revision 2026-10-17, third pass: WHICH BUILD NEXT? ended too soon; S6, the backdrop and the music extended by 60 frames to 876 (14.6 s), the hook back to 15 SECONDS.
