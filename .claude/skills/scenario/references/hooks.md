# Hooks, structure and voice for Elementors shorts

Distilled from `docs/SHORTS_RESEARCH.md` (sources there). This is the producer's and the streamer's reference; the harness side is in `game.md`.

## Timing that is not negotiable

- The hook is spoken and on screen inside the first 2 s; the stake is clear by 3 s (TikTok: proposition in 3 s, hook in 6 s). Frame one already moves: a cursor on its way, a reroll being pressed, never a static board.
- Cold open: payoff inside 5 s, then the reaction, then the button. Slow build: setup by 3 s, tension to 8-12 s, payoff by 15 s at the latest, button right after. Nothing explains between 5 and 8 s; that is where viewers leave when the middle narrates instead of unfolding.
- Length 10-25 s for one moment. End on the last meaningful frame, not on the celebration; no dead air at the end, loops die there.
- Something visibly changes every 5-8 s: a punch, a new region, a number on screen, a second event.

## Hook types (pick one per cut; two cuts of the same moment use two different ones)

| Type | What it does | Elementors line |
|---|---|---|
| outcome-first / stakes-first | opens on the moment it is hard, so the play is the payoff | "Two HP. Four gold. One roll." |
| need-first | names the one thing missing, the game answers | "I need one more fire reptile. One." |
| curiosity gap | withholds the answer | "I have never seen the shop do this." |
| reaction-first | the reaction before the cause | "WHAT. Okay, rewind, look at the shop." |
| contrarian / chat-said | challenges a belief, then proves it wrong | "Chat said rerolling at nine gold is throwing." |
| number | a specific figure as proof of odds or testing | "Twenty percent. Watch." |
| fail-to-win | the obvious move botched, then rescued; fail framing lifted CTR ~10% in TikTok's hyper-casual data | "I had the three star and I sold it." |
| challenge | a dare the viewer can replicate | "Find the line here. I'll wait." |
| confession | admits a mistake, shows the lesson | "I've been playing reptile wrong the whole demo." |
| this-is-illegal | an interaction that looks broken; only ever real footage | "This should not be allowed." |
| POV | names the viewer | "POV: round fourteen and the lobby is all three stars." |

Rules: the hook is a sentence a player would say aloud, not a tagline; no jargon in the first line ("if I miss this I'm out", not "slow-rolling at seven"); the on-screen caption at 0:00 states the stake in 5-7 words and agrees with the spoken line.

## Structure

`HOOK (0-2 s) → SETUP (one line, what is at stake on screen) → TURN (the event the camera punches on) → REACTION (blurted, not explained) → BUTTON (last line, a callback to the hook or an invitation to reply)`.

The button is the last line, lands on the last meaningful frame, and does one of: calls back the hook ("Throwing, huh."), flexes with a hedge ("Probably my best board. Probably."), invites a reply ("Tell me you've seen a luckier shop."). It is never a slogan and never a CTA. The game name may be said once in the whole short, the way a streamer says it, or not at all.

A/B: the body is the commodity, the hook is the work. Two cuts of one moment keep the beats and swap only the first line, the caption at 0:00 and the button. Name variants by hook type, not "v2".

## Moments that carry autobattler content

Hit the 3★ on the last gold · highroll opener · lucky roll that answers the exact need · perfect econ flex (interest cap, 50 gold) · "chat said it was bad" vindication · late-game board flex against the lobby · lowroll copium turning into "we're so back" · sold the wrong unit · the bugged-looking interaction · recap number nobody expected. Fail and relax are two different angles; do not mix them in one short.

## Voice: what a streamer sounds like

Keep: decisions said aloud ("okay, reroll, two gold, fine"), "we" with chat, stacked interjections ("okay okay okay"), the stop mid-word at the moment of the roll ("is that... no. NO."), hedged confidence ("this is probably fine"), the swing phrases "it's so over" / "we're so back", "copium", "lock in", "cooked", numbers the way players say them ("four seventy"). One address to chat per short at most.

Cut: adjectives from an ad (amazing, epic, insane as a description, satisfying), superlatives about the game, feature explanations the viewer did not ask for, complete tidy sentences, enthusiasm with no cause on screen, "download now", "free pulls", any line that would sound like a promo if read flat. Read every line aloud; if it sounds like copy, rewrite it as what the player would blurt.

ElevenLabs shaping: ellipses and periods for stops, exclamation marks for a shout, short sentences for pace. All-caps words are fine in the line (the captions keep them) because `tts.py` sends them capitalized: eleven_v3 reads a capitalized-all word as an acronym, letter by letter. Avoid dashes inside a line; the parser and the voice both read them badly.

## Captions

Max 3 words per caption (project rule), bold uppercase, highlight one word, band at y 0.72, never in the upper third. Caption the self-talk, not what the UI already shows (gold, round label). The 0:00 caption is the stake, not a transcript. Platform CTA buttons cover the bottom, so nothing important lives there.

## Paid-cut constraints

Only real captured footage; a "not actual gameplay" disclaimer does not save a misleading ad (ASA rulings on Playrix, Evony). A "bugged" angle must be an interaction the game really produces. Spark Ads cannot change caption or CTA after authorization, so whatever CTA exists is in the original cut. Three to five creatives per ad group; swap hooks, not bodies.

## Brief fields (what the brief block of a scenario carries)

angle (one sentence) · hook type + line · promise (what the viewer is told will happen) · emotion arc (three words with arrows) · proof frame (the beat and the marker the camera punches on) · button · captions list · render route (plain / save / reroll seed hunt) · assumptions · alt hook + alt button · watch-for (what can break at render time).
