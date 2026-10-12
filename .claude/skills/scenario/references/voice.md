# Streamer voice: the slang layer

How a streamer sounds over an autobattler, taken from ten reference shorts (`docs/VOICE_REFERENCE_CLIPS.md`: Batomon Showdown, Backpack Battles, TFT; DroneDarc, Jama, Scrambled Egg, Dan Gheesling, JakeskiTFT, BoxBox, Send TFT) and the sources in `docs/SHORTS_RESEARCH.md`. `hooks.md` says what a line must do; this file says how it sounds. The `streamer-voice` agent works from it, and the streamer hat in `/scenario` reads it before the first draft.

## The gap

Our drafts read like captions: one tidy sentence per beat, every word carrying information. "Fire, two stars. Nothing special." "But now I've got venom build." A streamer narrates while thinking, so the speech carries the thinking: restarts, repeats, a question to nobody, a verdict before the reason. The highlight clips are 60-90% reaction; nobody explains a mechanic in a full sentence unless the whole short is a guide (JakeskiTFT) or a talking head (BoxBox).

## Density

Words per second while talking, from the clips: Gheesling 2.2-2.9, Send TFT 2.9-3.2, Scrambled Egg 2.1-3.4, DroneDarc 2.7, Jama 1.9, the guide short 3.4, BoxBox 3.9. Talking is near continuous; the silences sit on the thing being watched (DroneDarc: 42 words in 22 s, three bursts with the game between them; Send TFT's rat clip: 20 words in 31 s, the board does the talking).

A 15-25 s short with 5-8 lines carries 40-70 words. A beat with 2 s of action carries 5-6 words; a beat with `idle 2.0` after it carries two sentences. The lint (`SEC_PER_WORD` 0.38 plus 0.25 per sentence) is the budget, and a rewrite never adds a timing WARN. Silence belongs on the event and in the 1 s between an event and its reaction (`align.py`), never between two thoughts.

## What the clips do

| Device | In the clips | Ours |
|---|---|---|
| Repeat the pivot word, x2 for weight | "huge, huge" · "disgusting, disgusting" · "they hate us, they hate us" · "we're maxed here, we're maxed" · "I have to see that again. I have to see that again." | "One more. One more fire reptile." · "That was free. That was so free." |
| Chant x4+ over an action | "chill chill chill chill chill" over the fight · "12-0 ... 12-0 ... 12-0" | "Melt. Melt melt melt melt." over the battle beat |
| Stack x3 while processing | "okay okay okay" · "no no no" · "please please please" | after a hit, before the sentence that names it |
| Restart mid-sentence | "we're basically, we're starting our scaling" · "you need to, you need to get the buff" · "how are we, we're hitting big red numbers" | one per short, on a setup line: "I'm, okay, I'm playing venom. Five venom." |
| Stop at the event | "is that... no. NO." · silence over the fight, then "There's no way." | "...wait." The ellipsis is the player looking. |
| Count out loud | "One, two." · "Let's count, let's count how many times we see it" · "13-0 ... 14-0, send it, 15-0" | stars, units, HP: "One. Two. ...three?" |
| Ask the screen | "Excuse me." · "What is even happening?" · "Why is it so close by the way?" · "Why does it look kind of scary, man?" · "How was that funny?" | "That's it? That's the boss?" instead of "The boss is dead." |
| Hedged flex | "I think we got a shot here, chat" · "I like our chances" · "I'm pretty sure I won. I would be shocked if I haven't." · "Honestly, Draven's pretty good." · "I'm gonna be honest, I don't feel confident" | the button: "Probably my best board. Probably." |
| Verdict first, reasons after | "And now it's over. This guy looks strong. Level ten. But my Draven's a freak, man." | "Oh it's over. Look at him. Three star. Look at the stats." |
| Nickname the unit | "my Draven's a freak, man" · "potion seller", "sweat lord", "gem lord" · "four star Michelin" | one per short, kept to the end: "the lizard", "big slime", "cold boy", "this guy" |
| Vocative tail | "..., man" · "..., chat" · "gamers" · "ladies and gentlemen" · "are you guys seeing this?" | "chat" once; "man" or "bro" up to twice, at the end of a sentence |
| Plead with the game | "come on baby" · "please" · "send it" · "please send it" · "dream is alive" · "watch this move" | on the roll, the reroll click, the battle button |
| A bit, kept running | "stop calling it jellyfish. We don't live in the ocean" · "the reroll build where you don't reroll" | a bit started in line 2 pays in the button |
| Inversion only players hear right | "it's over" and "and now it's over" mean I win; "it's so over" means I lose | use the one the caption makes unambiguous |

Not in the clips, also live: "wait wait wait", "hold on hold on", "oh. OH.", "no way", "no shot", "hello?", "I'm sorry?", "we're so back", "we hit", "that's a unit", "he's him".

## Lexicon by Elementors moment

Pull from the bucket of the moment, not from the whole list; one short uses 4-8 of these, not twenty.

- **Setup, want:** one more · just one · give me the reptile · the plan is · we're playing venom · I'm greeding · locked in · okay so · right, so · he needs one more · we need the fire.
- **Roll, reroll click:** roll · two gold, roll · one more roll · come on · come on baby · please · one time · show me · let's see · give me · slam it · roll roll roll.
- **The hit:** WAIT · wait wait wait · hold on · no way · there's no way · no shot · excuse me? · hello? · is that... · oh my god · oh my gosh · YES · let's go · we hit · WE HIT · that's the one · that's it, that's it · lotto · we hit the lotto · that's free · we take those · thank you game.
- **Miss, lowroll, copium:** no · nope · nothing · dead shop · brick · it's so over · I'm cooked · chat, I'm cooked · pain · copium · we're fine, we're fine · this is fine · probably fine · okay one more · last one, I promise · rigged · scam · robbed · they hate us · the game hates me.
- **The turn:** we're so back · WE'RE SO BACK · okay okay okay · oh. OH. · wait, actually · that's actually good · huge · huge, huge · that's big · giga · let him cook · we're cooking · lock in.
- **Merge, 3★:** three star · THREE · that's the three · there it is · there it is, there it is · he's gold · shiny · we hit three star · that's a unit · he's a unit · he's a freak, man · he's a monster · he's him · built different · cracked · disgusting · filthy · nasty · criminal · that should be illegal · broken · busted.
- **Element apply:** fire on the lizard · fire goes here · slap it on · what does this do · okay what happens · oh he's on fire · he's lit · cold boy · he's frozen · it burns · the whole row? · wait, it heals AND burns?
- **Battle:** battle · send it · SEND IT · let's see · go go go · chill chill chill · melt · melt melt melt · hold, hold · stay alive · don't die · please don't die · we're winning, right? · is that... we won? · that's it? · he did nothing · not even close · one shot · zero damage · untouched · full HP · clean · that was free · so free · easy · GG · and it's over.
- **Numbers,** said as a player says them, never as a stat line: four seventy · four hundred and seventy · four point six million · twelve and oh · fourteen units · five venom · two HP · level seven · big numbers · big red numbers · look at the numbers · what is that number · that can't be right · times two?
- **Flex, button:** my best board so far · probably my best board · best board I've had, probably · tell me that's not · name a better board · this could be the run · this is the run · lobby's cooked · I would be shocked if I lose this · I think we're good · we're chilling · we're maxed · sell it, they said · chat said · told you · I told you, chat · GG everyone · free game · that's free.
- **Vocatives:** chat · guys · gamers · boys · man · bro · dude · ladies and gentlemen · are you guys seeing this? · chat, is this real · chat, look.
- **Hedges:** I think · I mean · honestly · genuinely · lowkey · kind of · kinda · basically · like · probably · pretty sure · I guess · or whatever · it's whatever · to be fair · not gonna lie.
- **Fillers:** okay · alright · so · uh · yeah · yeah yeah yeah · right · right right · oh · ohh · oh wait · wait · hold on · actually · just · man.

"insane", "disgusting", "broken", "unreal" are approval words in a player's mouth about a thing on screen ("this is insane, this is insane" over a shop that repeats the same card) and ad words when they describe the game. The test: the sentence has a subject on screen (this board, that number, he) and comes after the event, not before it.

## Budgets per short

Enough that it sounds like one person talking, not so much that it is a parody.

- 5-8 lines: at least three carry a device, at most two are clean full sentences, and no two neighbouring lines use the same device.
- One repeat x2 and one stack or chant x3+; one restart at most; "chat" once; "man" or "bro" twice at most; fillers 2-4 in the whole short.
- The hook (line 1) may open with "okay", "wait", "oh", "so", never with "like", "I mean", "honestly". It still names the stake in 8 words or fewer, with no jargon.
- The button keeps its job (callback, hedged flex, invitation) and may repeat: "That was free. That was so free."
- A reaction comes 1 s after the event, so a punch line opens with the blurt ("WAIT", "oh", "no"), not with the noun.
- The game name once at most, the way a streamer says it, or not at all. No CTA, no "free" as in free game ("that was free" is a verdict and fine).

## Do not

- Ad words: amazing, epic, awesome, incredible, satisfying, stunning, powerful, unleash, experience, strategy, ultimate, download, play now, free to play. `scenario_lint.py` flags them.
- Brainrot that dates the cut or sounds like a brand being young: skibidi, rizz, sigma, six seven, gyatt, fanum tax, it's giving, slay, bussin, delulu. Fine and current: cooked, lock in, crash out, aura (ironic), goated, W, L, GG, no shot, lowkey.
- Other games' lingo the TikTok viewer does not share: Mortdogged, fast 8, slow roll at 7, going eighth, Yi only. "Roll", "reroll", "three star", "lobby", "econ", "pivot" are ours.
- Swearing in a paid cut (TikTok and YouTube ad review): no f- or s-words, no spoken "wtf". "What the..." with a stop, hell, holy, freaking, dang, oh my god, good god are fine. Same voice in organic cuts; one brand.
- Two tidy sentences in a row: "This board is strong. The venom synergy is active." is a tutorial.
- A reaction with no cause on screen, enthusiasm before the event, a feature the viewer did not ask about.

## Writing for the voice (ElevenLabs v3, `ninja`)

- Ellipsis is a stop ("is that... no."), a comma is a stumble or a restart ("we're basically, we're starting"), a period is a full stop, "!" is a shout, "?" lifts the end. Short sentences read fast.
- Caps are for the caption: `tts.py` sends "THREE" as "Three" (v3 spells an all-caps word), so a shout needs "!" or a stretched spelling. "Yesss", "nooo", "ohhh", "yooo": three or four letters, the voice stretches them; "Lesgooo" reads fine, "LETS GOOOOO" does not.
- Numbers as words, as said: "four seventy", "twelve and oh", "four point six million".
- Audio tags, lowercase, in square brackets, first thing in the line, one per line and two per short at most: `[laughs]` `[chuckles]` `[sighs]` `[exhales]` `[exhales sharply]` `[whispers]` `[excited]` `[surprised]` `[happy gasp]` `[short pause]` `[nervously]` `[sarcastic]` `[deadpan]`. `tts.py` sends them to the voice and drops them from the captions; the lint knows this list. Not on the hook line (it has to be clean to land); good on a reaction or the button ("[laughs] Sell it, they said."). The voice may ignore a tag it was not trained on, so a tag never replaces the words that carry the emotion.
- No dashes in a line (the voice and the parser read them badly), no braces. Commas, semicolons and brackets inside the quotes are fine.
- Captions are the written line in 3-word chunks, cut at `. , ? !`, so punctuate a repeat for the chunk you want: "Melt. Melt melt melt." gives MELT. / MELT MELT MELT. The caps word is the highlight.

## Before and after

Lines from our own scenarios, flat and live. The live line keeps the fact and the timing budget.

| Flat (shipped) | Live | Device |
|---|---|---|
| Random board from a real player. | Okay this is some random guy's board. Real player. Let's see. | filler, fragments |
| Fire, two stars. Nothing special. | Fire two star. It's... it's fine. It's whatever. | restart, hedge |
| Let's see. | Okay. Battle. Please. | plead |
| Look at those stats. | Look at the stats. LOOK at the stats. | repeat x2 |
| But now I've got venom build. | Yeah but, uh, I'm five venom now. Five. | filler, count |
| Okay. Let's see. Battle. | Okay okay okay. Send it. | stack, plead |
| Come on. Come on... melt. | Melt. Melt melt melt melt. | chant |
| ...wait. That's it? | Wait. That's it? That's... that's the boss? | ask the screen, restart |
| Bro. This venom build is unreal. | Bro. BRO. He did nothing. | repeat, verdict |
| Couldn't beat him last run. That was free. | He killed me last run. That was free. That was so free. | callback, repeat |
| I need one more fire reptile. | One more. One more fire reptile and I'm done. | repeat, stake |
| Three star. THREE. | There it is. There it is, there it is. THREE. | repeat x3 |
| Everybody sells the slime. Maybe fire? | Everybody sells the slime. Everybody. ...fire? | repeat, stop |
| So I rolled fire. Let's see. | Okay I rolled fire. What does fire even do. | filler, ask |
