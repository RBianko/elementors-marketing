# Short-form game ads: research notes

Collected 2026-10-11 for the `/scenario` skill. Anything marked *unverified* is a vendor or blog claim with no primary data behind it. The working rules distilled from this live in `.claude/skills/scenario/references/hooks.md`.

## Hook window

- TikTok Ads Help: "Prioritize your hook in the first 6 seconds", "Introduce your content proposition in the first 3 seconds". https://ads.tiktok.com/help/article/creative-best-practices?lang=en
- TikTok Creative Center, hyper-casual guide: hook in 3-6 s; Dec-2022 CTR lifts: failure framing +9.99%, sound effects +7.61%, relaxing gameplay +7.71%, robot voice +11.56%, labelled "observations, not rules". https://ads.tiktok.com/business/creativecenter/quicktok/online/tiktok-hyper-casual-game-creative-tips/pc/en
- Singular podcast: "about 2 seconds to grab people's attention". https://www.singular.net/podcast/mobile-game-ad-creative/
- YouTube Shorts "Stayed to watch"; third-party target 70%+ (*unverified*). https://www.creatoressentials.com/glossary/stayed-to-watch/
- Opus.pro: >65% three-second retention correlates with 4-7x impressions (*unverified*). https://www.opus.pro/blog/tiktok-hook-formulas
- HookMafia: hook lands in 1-2 s, 8-15 words. https://www.hookmafia.io/tiktok-hook-examples

## Hook types

Curiosity gap, outcome-first, mid-action, reaction-first, chat-first, fail-to-win, contrarian, number, POV, challenge, confession, "this is illegal". Sources: https://hooklayer.dev/guides/tiktok-hook-examples · https://blog.eklipse.gg/beginner-guide-2/viral-gaming-clips.html · https://www.blog.udonis.co/mobile-marketing/mobile-games/fake-mobile-game-ads · https://www.gamedeveloper.com/game-platforms/big-mobile-marketing-creative-review-the-things-that-work · https://vidscape.ai/blog/mobile-game-ad-hooks

Eklipse rules worth keeping: "Start on the moment the situation becomes hard, not the moment you solve it"; "A static opening frame reads as a still image for the first beat and gets swiped as one"; one plain-English stakes line in the first 2 s, no jargon; cut "on the peak or half a beat after"; "End on the last meaningful frame, not on the celebration"; "Dead air at the end is what kills loops"; caption the self-talk, not what the UI already shows.

## Structure

- Hook → Retain → Reward; drop-off cliff at 5-8 s when the middle explains instead of unfolding; write the hook last and test several. https://www.selfstorming.com/tools/libraries/frameworks/hook-retain-reward
- UGC time codes for apps: hook 0-1.5 s, opening to 8 s, payoff 8-18 s, proof 18-25 s, CTA 25-30 s. https://www.rocketshiphq.com/how-to-create-ugc-ads-mobile-apps/
- Hook/Problem/Solution/Proof/CTA, "three seconds to earn the next thirty", visual cue every 5-8 s, five hooks per script. https://www.retiplex.com/blog/ugc-ad-script-guide
- Bold hooks must pay off within 10-15 s (Opus.pro). Length: 8-20 s per single moment (Eklipse); Meta Instant Games 15-30 s, shorter better, A/B 10/15/30. https://developers.facebook.com/documentation/games/acquire/click-to-play-ads/creative
- Test discipline: swap only the first 3 s; "The structure is the commodity. The hooks are the work." https://www.ugcroster.com/blog/brands/how-to-write-hook-first-ugc-script-brief
- "The button": sketch-comedy term for the capping line of a scene. https://theankler.com/transcript-no-place-for-thinkers/

## Streamer voice

- Narrate decisions aloud, "we" with chat. https://frostytools.com/blog/what-to-talk-about-while-streaming/
- Slang: chat, F, GG, Pog, "it's so over / we're so back", copium, lock in. https://instreamly.com/posts/twitch-slang-you-need-to-know-in-2022/ · https://knowyourmeme.com/memes/its-so-over-were-so-back · https://merriam-webster.com/slang/copium
- "Make every hook a sentence a customer would say aloud. Taglines fail on camera." (UGC Roster). "Read the script aloud, and rewrite any line that sounds like ad copy." (Retiplex). "If the brief sounds like an ad, the creator will too." https://motionapp.com/library/frameworks/voice-copy-standards
- Fake tells: wooden actors in headphones, false enthusiasm, selling the feeling not the game (https://www.thegamer.com/fake-streamers-mobile-games-promotion-adverts/); Nexon AI-streamer ads flagged for unnatural speech and superlatives (https://www.notebookcheck.net/Nexon-s-The-First-Descendant-gets-mired-in-controversy-over-using-streamer-s-AI-likeness-in-advertisements.1090166.0.html); "download now off this video, 100 free pulls" as the scam-sounding CTA (https://www.sanlo.io/resources/i-studied-30-mobile-game-ads-on-tiktok-this-is-what-i-learned).
- ElevenLabs pauses and tags: https://elevenlabs.io/docs/product/prompting/pauses · v3 audio tags and punctuation: https://elevenlabs.io/docs/best-practices/prompting
- Ten reference shorts from real streamers (Batomon Showdown, Backpack Battles, TFT), transcribed and distilled: `docs/VOICE_REFERENCE_CLIPS.md` → `.claude/skills/scenario/references/voice.md`.

## Autobattler moments

TFT shorts titles follow "3-star + highroll/insane/weirdest + chat-blame". Mobalytics glossary: high roll / low roll. Riot on variance being the content: https://teamfighttactics.leagueoflegends.com/en-us/news/dev/dev-teamfight-tactics-remix-rumble-learnings/ . Super Auto Pets grew on Northernlion and Ludwig streams. Moment list: 3★ on last gold, highroll opener, perfect econ, bugged interaction, "chat said it was bad", late-game flex, lowroll copium to comeback, sold the wrong unit.

## Captions

TikTok: 5-10 words per second on screen. Chunks of 2-5 words; highlight one word; bold sans, outline 3-6 px; band at 50-78% of height, never the upper third; keep text in a 900x1400 centered rectangle; paid bottom zone ~19-25%. https://recapo.ai/blog/best-caption-styles-for-shorts/ · https://blitzcutai.com/blog/best-caption-placement-short-form-video · https://ads.tiktok.com/help/article/tiktok-interactive-add-on-download-card-ad-specifications?lang=en

## Paid cut

- TikTok: clear CTA, DIY look, 9:16, sound on, 3-5 creatives per ad group. Meta Reels (via Adobe): 9:16 + sound + safe zone + one extra element gave -20% CPC, +56% CTR. https://blog.adobe.com/en/publish/2024/11/04/unlock-potential-reels-best-practices-for-creative-success-using-adobe-creative-cloud
- Spoken CTA reads more native than a graphic; soft "demo in replies" beat "wishlist now" for indies. https://sovran.ai/blog/cta-overlay-vs-verbal-cta · https://howtomarketagame.com/2022/02/07/seven-great-tips-for-marketing-your-indie-game-on-tiktok/
- Spark Ads cannot change caption or CTA after authorization. https://inbeat.agency/blog/tiktok-spark-ads
- ASA: footage must be from the game, a "not representative" disclaimer does not cure a misleading ad (Playrix 2020, Evony). https://www.asa.org.uk/advice-online/entertainment-mobile-app-games.html · https://www.mishcon.com/news/asa-rules-mobile-game-ad-was-misleading-gameplay-depicted-did-not-reflect-the-core-game-playing-experience
- Meta Ad Standards on deceptive practices: https://transparency.meta.com/policies/ad-standards/ · Apple App Previews: https://developer.apple.com/support/app-previews/

## Brief templates

- Launchcodex performance brief: one angle per brief, hook rate 30-40%, hold ≥25%, kill below 25% after 2,000 impressions; batch 1 angle × 3 hooks × 2 formats. https://launchcodex.com/blog/creative-brand-strategy/performance-creative-brief-template/
- UGC Roster hook-first brief: thesis, hook bank, body beats as bullets, CTA verbatim, do-not-say list; naming `SKU_angle_creatorID_version`. https://www.ugcroster.com/blog/brands/how-to-write-hook-first-ugc-script-brief
- Needle Meta brief: angle, viewer, hooks A/B/C word for word, one claim, avoid list, CTA exact. https://www.askneedle.com/blog/how-to-brief-ugc-creators-for-meta-ads-with-template
- Ad naming `[crid]_[concept]_[hook]_[format]_[creator]_[version]`. https://adsuploader.com/blog/ad-naming-conventions

## Gaps

No primary source quantifies the 1-3 s cliff beyond TikTok's 3 s / 6 s guidance. No published test of spoken CTA vs end card for game installs. No creator interviews on autobattler clip craft. "Wait for it", "this is illegal" and "reaction-first" are practice, not tested categories.
