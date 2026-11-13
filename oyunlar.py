"""Game info pages (/games/...), the Turkish foot tennis guide and llms.txt.

Called from build.py:  oyunlar.build_pages(ctx)  -> list of (path, lastmod date)
ctx = dict(page=page, write=write, e=e, jsonld=jsonld, SITE=SITE, BRAND=BRAND, CONTACT=CONTACT,
           GAMES=GAMES, APPS=APPS, markdown=markdown, parse_front_matter=parse_front_matter)

Facts come only from the product notes (marketing/<game>/GERCEKLER.md, store texts, memory files),
checked 13 Nov 2026. Rules kept on purpose:
  - the word the federation uses for the sport is NOT used in visible marketing copy (store rule, FTS);
  - NEO: no endings, no answers; Protokol-Ø: the "you're the AI" hook is public since 8 Nov 2026,
    the last module's secrets and the endings are not;
  - Prof. Nano: children's game, no child names/photos, no links that pull kids elsewhere;
  - no ratings, reviews, download or revenue numbers; no competitor brand names;
  - the owner's personal name is not added here (pages pass owner=BRAND).
When a fact changes (new platform, new mode), edit the dict below and rebuild.
"""
import datetime as dt
import re

UPDATED = dt.date(2026, 11, 13)          # visible "Page updated" + sitemap lastmod for these pages
GUIDE_EN = "/blog/how-to-play-foot-tennis/"
GUIDE_TR = "/tr/ayak-tenisi-nasil-oynanir/"

# -------------------------------------------------------------------------------------------- data
# card = the matching entry in build.py GAMES (store links are taken from there, exactly as on the home page)
GAMES_INFO = [
    dict(
        slug="foot-tennis-stars", card="Foot Tennis Stars", name="Foot Tennis Stars",
        alt_names=["Ayak Tenisi Yıldızları"], icon="/img/foot-tennis-stars-2.jpg",
        title="Foot Tennis Stars: Foot Tennis Game for iPhone and Android",
        desc="Foot Tennis Stars is a free foot tennis game for iPhone, iPad and Android: real rules, smashes and bicycle kicks, offline matches and online cross-play.",
        one_line="Free foot tennis (football tennis) game for iPhone, iPad and Android: offline matches against computer rivals, or online where iPhone and Android players meet.",
        lead="Foot Tennis Stars is a free foot tennis game for iPhone, iPad and Android. Football meets volleyball: two sides, a net, no hands, and rallies won with placed shots, lobs, smashes and bicycle kicks. Play against computer rivals without internet, or go online, where iPhone and Android players meet in the same match.",
        genre=["Sports", "Foot tennis"], platforms=["iOS", "Android"], os="iOS, Android",
        langs=["en", "tr", "de", "fr", "es", "pt", "it", "th"], released="2026-09-15",
        play_mode=["SinglePlayer", "MultiPlayer"],
        facts=[("Sport", "Foot tennis, also called football tennis or soccer tennis"),
               ("Platforms", "iPhone, iPad and Android"),
               ("Price", "Free to download, with ads and optional purchases"),
               ("Players", "Solo against computer rivals, online 1 v 1, and 1 v 1 or 2 v 2 with friends"),
               ("Languages", "English, Turkish, German, French, Spanish, Portuguese, Italian and Thai"),
               ("First released", "September 2026 on iPhone, October 2026 on Android")],
        sections=[
            ("how", "How it plays", """
    <p>Each side tries to send the ball over the net so the other side can't return it. The game follows the core rules of the real sport: you get <strong>up to three touches</strong> on your side, the ball may <strong>bounce once</strong> on your side, a second bounce loses the point, and if the ball lands out, the last player to touch it loses the point. The winner of a rally serves next, and a serve has to clear the net.</p>
    <p>You run with your left thumb and play with buttons: <strong>PLACE</strong> for a controlled shot, <strong>LOB</strong> to go over a player at the net, <strong>SMASH</strong> to hit down hard, and <strong>BOUNCE</strong> to set the ball up for yourself. Hold SMASH for a bicycle kick; smash a high ball at the net for a scissor smash. In 2 v 2 there is a <strong>PASS</strong> button and teammates take turns, as in real doubles.</p>
    <p>A match is one game to <strong>7, 9 or 11 points</strong> (you choose; 9 is the default). Matches against the computer need a two-point lead, with a cap so a game can't go on forever. New to the sport? Read our guide <a href="{GUIDE_EN}">How to Play Foot Tennis: Rules, Scoring and Tips</a>.</p>"""),
            ("modes", "Modes and features", """
    <ul>
      <li><strong>Quick match</strong> against a computer rival, and <strong>Lightning match</strong>: first to 3 points, and at 2–2 the next point wins.</li>
      <li><strong>Online match</strong>: matchmaking by level. If nobody is found within about 20 seconds, you play a computer rival instead. Friends can join the same room with a six-digit code.</li>
      <li><strong>Play with a friend</strong> on the same Wi-Fi network, 1 v 1 or 2 v 2.</li>
      <li><strong>Season</strong> (a league of 10 teams), <strong>cups</strong> for 4, 8 or 16 players, and the <strong>Nations Cup</strong> with national teams, a tunnel walk-out and a trophy lift.</li>
      <li><strong>Daily challenge</strong>, training, and a ladder of rivals, each with their own style of play.</li>
      <li><strong>Your own player and club</strong>: create your character, design a kit and a crest, and build up a club ground.</li>
      <li><strong>Nine venues</strong>: stadium, beach, indoor hall, rooftop, park, snowy peak, desert, training ground and a small-sided pitch, plus the Nations Cup arena.</li>
    </ul>"""),
            ("who", "Who it's for", """
    <p>Players who like football, volleyball or quick sports games on the phone, people who play foot tennis and want it in their pocket, and friends who want to settle a rally on the same Wi-Fi. Matches are short, and you can play without an account.</p>"""),
            ("price", "Price and platforms", """
    <p>Foot Tennis Stars is free on the App Store (iPhone and iPad) and on Google Play. It shows ads between some matches and offers optional rewarded ads for extra gold. Optional purchases are a <strong>Club Membership</strong>, which removes the ads between matches and adds gold and extras, and gold packs. There is no subscription, no energy timer and no paid loot box. The store pages are available in 39 languages.</p>"""),
        ],
        faq=[("Is Foot Tennis Stars free?",
              "Yes. Foot Tennis Stars is free to download on the App Store and Google Play. It has ads between some matches and optional purchases: a Club Membership that removes those ads and adds gold, and gold packs. There is no subscription."),
             ("Can iPhone and Android players play together?",
              "Yes. Online matches are cross-play: an iPhone player and an Android player can end up in the same match."),
             ("Can I play Foot Tennis Stars offline?",
              "Yes. Matches against computer rivals work without an internet connection. Online matches need a connection."),
             ("What are the rules in Foot Tennis Stars?",
              "Each side gets up to three touches and one bounce. A second bounce, or a ball that lands out, loses the point. The rally winner serves, and a serve must clear the net. A match is one game to 7, 9 or 11 points, and matches against the computer need a two-point lead."),
             ("Can I play foot tennis with a friend?",
              "Yes. On the same Wi-Fi network you can play 1 v 1 or 2 v 2, and online a friend can join your room with a six-digit code."),
             ("Which languages does the game support?",
              "The game itself is in English, Turkish, German, French, Spanish, Portuguese, Italian and Thai. The store pages are in 39 languages.")],
        more=[("How to Play Foot Tennis: Rules, Scoring and Tips", GUIDE_EN),
              ("Ayak tenisi nasıl oynanır? (Türkçe)", GUIDE_TR),
              ("Partners, clubs and sponsors", "/foot-tennis-stars/partners/"),
              ("The story: from stick figures to online matches", "/blog/foot-tennis-stars/"),
              ("Foot Tennis Stars 2.0 on Android", "/blog/foot-tennis-stars-android/")],
    ),
    dict(
        slug="tomb-maze", card="Tomb Maze: Horror Escape", name="Tomb Maze: Horror Escape",
        alt_names=["Tomb Maze"], icon="/img/tomb-maze.jpg",
        title="Tomb Maze: Horror Escape, a Free Horror Maze Game for iPhone",
        desc="Tomb Maze: Horror Escape is a free first-person horror maze game for iPhone. Escape 20 dark labyrinths: hide, listen and don't run. Works offline.",
        one_line="Free first-person horror maze escape game for iPhone and iPad: 20 labyrinths beneath a collapsed pyramid, creatures that see and hear you, works offline.",
        lead="Tomb Maze: Horror Escape is a free first-person horror maze game for iPhone and iPad. The pyramid has collapsed behind you, and the only way out is through twenty dark labyrinths guarded by creatures that see and hear you. Hide, listen, and don't run.",
        genre=["Horror", "Maze", "Escape"], platforms=["iOS"], os="iOS",
        langs=["en", "tr", "es", "pt", "de", "fr"], released="2026-10-19", rating="12+",
        play_mode=["SinglePlayer"],
        facts=[("Genre", "First-person horror, maze escape"),
               ("Platforms", "iPhone and iPad"),
               ("Price", "Free; all 20 levels are free. Ads and optional purchases"),
               ("Age rating", "12+ on the App Store. Horror themes and jump scares, no gore"),
               ("Offline", "Works offline, no account or sign-in"),
               ("Languages", "English, Turkish, Spanish, Portuguese, German and French")],
        sections=[
            ("how", "How it plays", """
    <p>You are an explorer who came for the Sun Disk. Each level is a new maze, built fresh every time, and it gets larger, darker and more crowded as you go deeper. You have a flashlight, a pocket for spare batteries, a map and a compass, and you are looking for the way out.</p>
    <ul>
      <li><strong>Hide and listen.</strong> Duck into a locker or a sarcophagus and hold your breath. Running makes noise, and every footstep carries.</li>
      <li><strong>Three kinds of danger.</strong> The <strong>Guardian</strong> patrols the corridors; the <strong>Listener</strong> comes to sound; the <strong>Shadow</strong> freezes while you look at it, so never turn your back.</li>
      <li><strong>Traps and seals.</strong> Dart walls, spike pits, collapsing floors and falling stones. Sealed doors open when you read the glyphs and turn the dials.</li>
      <li><strong>Treasure.</strong> Pieces of the Sun Disk, hidden relics for your Treasure Room, and journal pages that tell what happened here.</li>
      <li><strong>Help when you're lost.</strong> Checkpoints, and Intuition hints when you are truly stuck.</li>
    </ul>"""),
            ("modes", "Modes", """
    <ul>
      <li><strong>Story</strong>: 20 levels.</li>
      <li><strong>Nightmare</strong>: unlocked when you finish the story. The same mazes with faster Guardians, no map and no checkpoints.</li>
      <li><strong>Endless Descent</strong>: one life, floor after floor. How deep can you go?</li>
      <li><strong>Daily Labyrinth</strong>: one maze for everyone each day, unlocked after level 3.</li>
    </ul>
    <p>Game Center has three leaderboards (daily maze time, descent depth, fewest deaths in the story) and 15 achievements.</p>"""),
            ("who", "Who it's for", """
    <p>Players aged 12 and up who like short, tense horror escapes: one maze, one way out, and something in the dark between you and it. It is built for headphones; footsteps, breathing and the creatures' sounds tell you where the danger is.</p>"""),
            ("price", "Price and platforms", """
    <p>Tomb Maze is free on the App Store for iPhone and iPad, and there is no paywall: all 20 levels are free. It shows ads between some levels and offers optional rewarded ads, for example to continue after you die. Optional purchases: Remove Ads, an Explorer Pack (no ads plus hints) and Intuition hint packs. There is no subscription. An Android version has not been released.</p>"""),
        ],
        faq=[("Is Tomb Maze free?",
              "Yes. Tomb Maze: Horror Escape is free on the App Store and all 20 levels are free. It has ads and optional purchases: Remove Ads, an Explorer Pack and Intuition hint packs."),
             ("How scary is Tomb Maze, and who is it for?",
              "It is rated 12+ on the App Store. It has horror themes and jump scares but no gore. It is best played with headphones."),
             ("Does Tomb Maze work offline?",
              "Yes. It works offline and needs no account or sign-in."),
             ("How many levels does Tomb Maze have?",
              "The story has 20 levels. After it there is Nightmare mode, Endless Descent and a Daily Labyrinth that is the same for everyone each day."),
             ("Is Tomb Maze on Android?",
              "Not yet. Tomb Maze is available on the App Store for iPhone and iPad."),
             ("Which languages does Tomb Maze support?",
              "English, Turkish, Spanish, Portuguese, German and French.")],
        more=[("The story: the labyrinth game I always wanted to make", "/blog/tomb-maze/"),
              ("Tomb Maze is out now", "/blog/tomb-maze-out-now/")],
    ),
    dict(
        slug="bolt-and-breath", card="Bolt & Breath: Last Dragon", name="Bolt & Breath: Last Dragon",
        alt_names=["Bolt & Breath", "Bolt and Breath"], icon="/img/bolt-and-breath.jpg",
        title="Bolt & Breath: Last Dragon, a Dragon Flying Game for iPhone",
        desc="Bolt & Breath: Last Dragon is a free dragon flying game for iPhone and iPad: 57 missions, ten dragons, burn the royal fleet or man the ballista. Plays offline.",
        one_line="Free dragon flight game for iPhone and iPad: fly the last dragon, burn the royal fleet, or switch sides and man the ballista. 57 missions, plays offline.",
        lead="Bolt & Breath: Last Dragon is a free dragon flight game for iPhone and iPad. You are the last dragon on a windswept coast: glide, dive and burn the royal fleet that came to hunt you. In some missions you switch sides and man the ballista yourself.",
        genre=["Action", "Flight", "Dragon"], platforms=["iOS"], os="iOS",
        langs=["en", "tr"], released="2026-09-16", play_mode=["SinglePlayer"],
        facts=[("Genre", "Dragon flight and action"),
               ("Platforms", "iPhone and iPad"),
               ("Price", "Free, with ads and optional purchases"),
               ("Content", "57 missions in two campaigns, ten dragons"),
               ("Offline", "Plays offline, no account needed"),
               ("Languages", "English and Turkish in the game; store page in 39 languages")],
        sections=[
            ("how", "How it plays", """
    <p>Flight takes one finger: glide, dive and climb, perch on rocky peaks to catch your breath, and take off again. Every level opens with a dive through the clouds. Galleons, warehouses, watchtowers and castle walls burn when your fire touches them.</p>
    <ul>
      <li><strong>The Last Dragon</strong>: burn the fleet and the castles as the last dragon.</li>
      <li><strong>Royal Marksman</strong>: the other side of the same war. Man the ballista on a castle wall or a galleon's deck and bring dragons down.</li>
      <li><strong>Rescue</strong>: chained dragons are pinned beneath a giant yoke. Free them, then fly them yourself.</li>
      <li><strong>Ten dragons</strong>, each with its own look and upgrades: fast ones, heavy ones, quiet ones, long-ranged ones.</li>
      <li><strong>Dragon Keep</strong>: raise a petrified ancestor dragon into your keep in six stages, then hold it against sieges that grow bigger each time.</li>
      <li><strong>Free Flight</strong> around your keep, and a weekly mission.</li>
    </ul>
    <p>Game Center has leaderboards and achievements.</p>"""),
            ("who", "Who it's for", """
    <p>Anyone who has wanted to ride a dragon. Bolt &amp; Breath is a single-player game, with no account and no online connection needed, so it suits short sessions on the go as well as long evening flights.</p>"""),
            ("price", "Price and platforms", """
    <p>Bolt &amp; Breath is free on the App Store for iPhone and iPad. It shows ads, for example after you fall or finish a level, and offers optional rewarded ads such as one revive per level. Optional purchases: Remove Ads and packs of Ember Hearts, the in-game currency. Dragons are bought with Embers only. There is no subscription. An Android version has not been released.</p>"""),
        ],
        faq=[("Is Bolt & Breath free?",
              "Yes. Bolt & Breath: Last Dragon is free on the App Store. It has ads and optional purchases: Remove Ads and Ember Hearts packs. There is no subscription."),
             ("Does Bolt & Breath work offline?",
              "Yes. It plays offline and needs no account."),
             ("How many missions are there?",
              "57 missions in two campaigns: The Last Dragon, where you fly and burn the fleet, and Royal Marksman, where you man the ballista."),
             ("Can I play as the other side?",
              "Yes. In the Royal Marksman missions you man the ballista on a castle wall or a galleon and bring dragons down."),
             ("Is Bolt & Breath on Android?",
              "Not yet. It is available on the App Store for iPhone and iPad."),
             ("Which languages does Bolt & Breath support?",
              "The game is in English and Turkish. The App Store page is available in 39 languages.")],
        more=[("The story: why I wanted to ride a dragon", "/blog/bolt-and-breath/")],
    ),
    dict(
        slug="neo", card="NEO: Interactive Horror Story", name="NEO: Interactive Horror Story",
        alt_names=["NEO"], icon="/img/neo.jpg",
        title="NEO: Interactive Horror Story Game With 20 Endings",
        desc="NEO is a free interactive horror story for iPhone and iPad. Elif is missing, the clock stopped at 17:34. Read, choose, survive: 20 endings, whole story free.",
        one_line="Free interactive horror story (text-based, choice-driven) for iPhone and iPad: a missing friend, a clock frozen at 17:34, a time loop, 20 endings; the whole story is free.",
        lead="NEO: Interactive Horror Story is a free text-based horror game for iPhone and iPad. Elif has been missing for three days and the campus clock froze at 17:34. You are Lika, the only one still looking for her. Read, choose and survive: the wrong door kills you, and dying restarts the loop.",
        genre=["Interactive fiction", "Horror", "Text adventure"], platforms=["iOS"], os="iOS",
        langs=["en", "tr", "de", "fr", "es"], released="2026-07-20", play_mode=["SinglePlayer"],
        facts=[("Genre", "Interactive horror story, choice-based text game"),
               ("Platforms", "iPhone and iPad"),
               ("Price", "The whole story is free; optional purchases and ads"),
               ("Endings", "20 endings, collected on an ending map as you play"),
               ("Languages", "English, Turkish, German, French and Spanish"),
               ("First released", "July 2026")],
        sections=[
            ("how", "How it plays", """
    <p>You read and you choose. Do you go to Elif's apartment, follow her trail on campus, or visit her family? There are no right answers, only consequences: force the wrong door and you die, make noise and you are seen. When you die, the loop starts again, and this time you know one more thing.</p>
    <ul>
      <li><strong>Choices that matter</strong>: hundreds of scenes, and you can never pick an option that refers to a clue you haven't found.</li>
      <li><strong>An ending map</strong> that fills in only as you reach each of the 20 endings.</li>
      <li><strong>A continue card</strong> shows your loop number and where you left off.</li>
      <li><strong>Hints</strong> point the way without giving you the answer.</li>
      <li>Game Center achievements, and optional reminders at most twice a day.</li>
    </ul>
    <p>That is all we will say about the story. NEO is built on not knowing, and the first time through is the only time you get to not know.</p>"""),
            ("who", "Who it's for", """
    <p>Readers who like psychological thrillers, mysteries and choose-your-own-adventure stories, and players who want horror built from tension and choices rather than gore. It is a game of reading, so it suits headphones-off moments too.</p>"""),
            ("price", "Price and platforms", """
    <p>NEO is free on the App Store for iPhone and iPad, and the whole story, with all 20 endings, can be played for free. An ad may play after a death (never after your first one), and you can watch an optional ad for a hint. <strong>Full Access</strong> is an optional one-time purchase that removes the death ads, makes hints unlimited and opens Elif's Records. <strong>Signal</strong> packs let you rewind to the moment before a death. NEO is not on Android.</p>"""),
        ],
        faq=[("Is NEO free?",
              "Yes. NEO is free to download and the whole story, including all 20 endings, can be played for free. Full Access and Signal packs are optional purchases."),
             ("How many endings does NEO have?",
              "NEO has 20 endings. They appear on the ending map only as you reach them."),
             ("What kind of game is NEO?",
              "NEO is an interactive horror story: a text-based, choice-driven psychological thriller with a time loop. You read scenes and choose what to do next."),
             ("Which languages is NEO available in?",
              "English, Turkish, German, French and Spanish. You can switch languages from the menu."),
             ("Is NEO on Android?",
              "No. NEO is available on the App Store for iPhone and iPad.")],
        more=[("The story behind NEO", "/blog/neo/")],
    ),
    dict(
        slug="protokol-zero", card="PROTOKOL-Ø: Story Thriller", name="PROTOKOL-Ø: Story Thriller",
        alt_names=["Protokol-Ø", "Protokol Zero", "Protocol Zero"], icon="/img/protokol-0.jpg",
        title="PROTOKOL-Ø: Story Thriller Game for iPhone With Five Endings",
        desc="PROTOKOL-Ø is a story thriller for iPhone and iPad: you're the AI, and nobody told you. Approve, reject, escalate. Seven modules, five endings, no ads.",
        one_line="Story thriller for iPhone and iPad: you're the AI, and nobody told you. Process files at AION Systems (approve, reject, escalate) and watch the record change. No ads; first modules free.",
        lead="PROTOKOL-Ø is a story thriller for iPhone and iPad with one hook: you're the AI, and nobody told you. At AION Systems everyone treats you as the new decision analyst. You process files against a rulebook (approve, reject, escalate) and soon the record starts to change.",
        genre=["Story", "Thriller", "Interactive fiction"], platforms=["iOS"], os="iOS",
        langs=["en", "tr"], released="2026-04-27", play_mode=["SinglePlayer"],
        facts=[("Genre", "Dystopian story thriller, decision game"),
               ("Platforms", "iPhone and iPad"),
               ("Price", "First two modules and half of the third free; one-time purchase for the rest"),
               ("Content", "Seven modules, five endings"),
               ("No ads", "No ads, no subscription, no internet needed"),
               ("Languages", "English and Turkish")],
        sections=[
            ("how", "How it plays", """
    <p>Each module brings a new queue: access requests, credit applications, hiring, emergency triage, parole. You decide each file by the rulebook, and every queue has a slightly harder rule. The people you escalate come back in the next queue, carrying your decision. Let the timer run out and the system decides for you.</p>
    <ul>
      <li><strong>The ledger</strong>: the one record nobody can edit. Press and hold a line on any card to write it down; space is limited.</li>
      <li><strong>The record changes</strong>: forms come back corrected and summaries say things you never wrote. Spot the change, then check it against your ledger.</li>
      <li><strong>Only the file counts</strong>: remember something from an earlier file and you may be right, but it is stamped as an unsourced inference.</li>
      <li><strong>After 03:12</strong>: close the game and come back once your device's clock has passed 03:12. Something may have changed.</li>
      <li><strong>Appeals</strong> let you reopen a decision, once per module, at a cost.</li>
    </ul>
    <p>Your ending is not a score. It is the policy your decisions add up to. We don't say more than that.</p>"""),
            ("who", "Who it's for", """
    <p>Players who like dystopian fiction, moral choices and mysteries you solve by paying attention. There is no action and no reflex test, only reading, deciding and noticing. Settings include text size, high contrast, a colour-blind mode and reduced motion.</p>"""),
            ("price", "Price and platforms", """
    <p>PROTOKOL-Ø is free to download on the App Store for iPhone and iPad. Modules 1 and 2 and the first half of Module 3 are free. A single one-time purchase unlocks the rest and every ending. Appeal packs are optional; you get two appeals free. There are no ads and no subscription, and the game needs no internet connection. It is not on Android.</p>"""),
        ],
        faq=[("Is PROTOKOL-Ø free?",
              "The first two modules and half of the third are free. A single one-time purchase unlocks the rest of the game and every ending. There is no subscription."),
             ("Does PROTOKOL-Ø have ads?",
              "No. There are no ads, and the game needs no internet connection."),
             ("How many endings does PROTOKOL-Ø have?",
              "Five. Your ending is the policy your decisions add up to."),
             ("What does 'you're the AI' mean in PROTOKOL-Ø?",
              "Everyone at AION Systems treats you as the new analyst, but you are the AI being trained, and nobody told you. What that means for the record, and for the people in the files, is the game."),
             ("Which languages is PROTOKOL-Ø available in?",
              "English and Turkish. The game follows your device language and can be changed in Settings."),
             ("Is PROTOKOL-Ø on Android?",
              "No. It is available on the App Store for iPhone and iPad.")],
        more=[("What making Protokol-Ø taught me", "/blog/protokol-zero/")],
    ),
    dict(
        slug="prof-nano", card="Prof. Nano", name="Prof. Nano: Kids Science Games",
        alt_names=["Prof. Nano", "Prof. Nano: Çocuk Bilim Oyunu"], icon="/img/prof-nano.jpg",
        title="Prof. Nano: Science Games for Kids 7 to 10, No Ads, Offline",
        desc="Prof. Nano: hands-on science games for kids aged 7 to 10 on iPhone and iPad. 48 mini games, read aloud, no ads, works offline, no data collected.",
        one_line="Hands-on science game for children aged 7 to 10 on iPhone and iPad: 48 mini games in 8 regions, read aloud, no ads, works offline, collects no data; first region free.",
        lead="Prof. Nano is a hands-on science game for children aged 7 to 10, on iPhone and iPad. A friendly professor reads everything aloud while children experiment and see what happens: 48 mini games across 8 regions, from magnets and mirrors to the human body, space and robots. No ads, it works offline, and it collects no data.",
        genre=["Educational", "Science", "Kids"], platforms=["iOS"], os="iOS",
        langs=["en", "tr"], released="2026-10-19", play_mode=["SinglePlayer"], audience="7-10",
        facts=[("Ages", "7 to 10"),
               ("Content", "48 hands-on mini games in 8 regions"),
               ("Price", "Free first region; one-time Full Version, no subscription"),
               ("No ads, no data", "No ads, no accounts, no data collection"),
               ("Offline", "Works without internet after the download"),
               ("Languages", "English and Turkish, read aloud in both")],
        sections=[
            ("how", "How it plays", """
    <p>Children learn by doing, not by answering quizzes. Each mini game is a small experiment: move a magnet, tilt a ramp, build a circuit, and watch what happens. Prof. Nano explains out loud, and help comes in small steps when a child gets stuck.</p>
    <ul>
      <li><strong>8 regions</strong>: physics, math, the human body, biology, space, history, chemistry and robotics.</li>
      <li><strong>Discovery cards</strong> to collect, and a discovery notebook of "I thought… I saw…" notes.</li>
      <li><strong>Try at home</strong>: 10 simple experiments to do together, away from the screen.</li>
      <li>Everything is <strong>read aloud</strong>, so children who are still learning to read can play.</li>
    </ul>"""),
            ("parents", "For parents", """
    <ul>
      <li><strong>Parent gate</strong>: purchases and settings sit behind a gate that asks for a number written in words.</li>
      <li><strong>Parent section</strong>: what your child discovered, questions to ask them, and progress by region.</li>
      <li><strong>Break reminder</strong> every 15 minutes, on by default.</li>
      <li><strong>No ads, no data collection, no internet requests</strong>, and no links that lead children out of the game.</li>
    </ul>"""),
            ("price", "Price and platforms", """
    <p>Prof. Nano is free to download on the App Store for iPhone and iPad. The first region, <strong>Lighthouse Point</strong>, is free with no time limit and has 6 games. The <strong>Full Version</strong> is a single one-time purchase that opens all 8 regions and every game; it sits behind the parent gate, and Family Sharing is on. There is no subscription and no in-game currency. <strong>Android is coming soon.</strong></p>
    <p>Teachers, librarians and education reviewers can ask for a limited review code: see <a href="/for-schools/">Prof. Nano for schools</a>.</p>"""),
        ],
        faq=[("What age is Prof. Nano for?",
              "Prof. Nano is made for children aged 7 to 10. Everything is read aloud, so children who are still learning to read can play."),
             ("Is Prof. Nano free?",
              "The first region, Lighthouse Point, with 6 games, is free with no time limit. The Full Version is a one-time purchase that opens all 8 regions and 48 games. There is no subscription."),
             ("Does Prof. Nano have ads or collect data?",
              "No. There are no ads, no accounts and no data collection, and purchases sit behind a parent gate."),
             ("Does Prof. Nano work offline?",
              "Yes. After the download it works without an internet connection."),
             ("Is Prof. Nano on Android?",
              "Not yet. Prof. Nano is on the App Store for iPhone and iPad, and an Android version is coming soon."),
             ("Which languages does Prof. Nano support?",
              "English and Turkish, with voice narration in both.")],
        more=[("Prof. Nano for schools and home education", "/for-schools/"),
              ("Okullar için Prof. Nano (Türkçe)", "/tr/okullar/"),
              ("Why we built Prof. Nano", "/blog/prof-nano/")],
    ),
]


# ----------------------------------------------------------------------------------------- helpers
def _strip(html_text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html_text)).strip()


def _facts(items, e):
    return '<ul class="facts">' + "".join(
        f"<li><strong>{e(h)}</strong><span>{e(t)}</span></li>" for h, t in items) + "</ul>"


def _store_buttons(card, e, lang="en"):
    b = []
    if card.get("store"):
        b.append(f'<a class="btn primary" href="{e(card["store"])}" target="_blank" rel="noopener">'
                 f'{"App Store" if lang == "en" else "App Store’da indir"}</a>')
    if card.get("play"):
        b.append(f'<a class="btn" href="{e(card["play"])}" target="_blank" rel="noopener">'
                 f'{"Google Play" if lang == "en" else "Google Play’de indir"}</a>')
    return '<p class="btn-row">' + " ".join(b) + "</p>"


def _fmt(d):
    return f"{d.day} {d.strftime('%B')} {d.year}"


# ------------------------------------------------------------------------------------------- build
def build_pages(ctx):
    page, write, e, jsonld = ctx["page"], ctx["write"], ctx["e"], ctx["jsonld"]
    SITE, BRAND, C = ctx["SITE"], ctx["BRAND"], ctx["CONTACT"]
    cards = {g["name"]: g for g in ctx["GAMES"]}
    org = {"@id": SITE + "/#org"}
    urls = []

    def game_url(g):
        return f"/games/{g['slug']}/"

    def game_ld(g, card):
        path = game_url(g)
        obj = {"@context": "https://schema.org", "@type": ["VideoGame", "MobileApplication"],
               "@id": SITE + path + "#game", "name": g["name"], "alternateName": g["alt_names"],
               "url": SITE + path, "description": g["lead"], "image": SITE + g["icon"],
               "genre": g["genre"], "gamePlatform": g["platforms"], "operatingSystem": g["os"],
               "applicationCategory": "EducationalApplication" if g["slug"] == "prof-nano" else "GameApplication",
               "inLanguage": g["langs"], "playMode": g["play_mode"], "datePublished": g["released"],
               "isAccessibleForFree": True,
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "category": "free"},
               "author": org, "publisher": org,
               "sameAs": [u for u in (card.get("store"), card.get("play")) if u]}
        if g.get("rating"):
            obj["contentRating"] = g["rating"]
        if g.get("audience"):
            lo, hi = g["audience"].split("-")
            obj["audience"] = {"@type": "PeopleAudience", "suggestedMinAge": int(lo), "suggestedMaxAge": int(hi)}
        return obj

    # ---------------------------------------------------------------- one page per game
    for g in GAMES_INFO:
        card = cards[g["card"]]
        path = game_url(g)
        secs = "".join(
            f'\n  <section class="org-sec" aria-labelledby="{sid}-h">\n    <h2 id="{sid}-h">{e(h)}</h2>'
            f'{body.replace("{GUIDE_EN}", GUIDE_EN)}\n  </section>'
            for sid, h, body in g["sections"])
        faq_html = "".join(f"\n    <h3>{e(q)}</h3>\n    <p>{e(a)}</p>" for q, a in g["faq"])
        legal = " · ".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a>' for n, u in card["legal"])
        others = [o for o in GAMES_INFO if o is not g]
        more = "".join(f'<li><a href="{e(u)}">{e(t)}</a></li>' for t, u in g["more"])
        more += "".join(f'<li><a href="{game_url(o)}">{e(o["name"])}</a></li>' for o in others)
        body = f"""<main id="main" class="wrap section page-top org game-page">
  <p class="crumb"><a href="/games/">Games</a></p>
  <header class="page-head org-head">
    <img class="org-icon" src="{g["icon"]}" alt="{e(card.get("alt") or g["name"] + " icon")}" width="96" height="96" decoding="async" fetchpriority="high">
    <h1>{e(g["name"])}</h1>
    <p class="lead-left">{e(g["lead"])}</p>
    {_store_buttons(card, e)}
  </header>
  <section class="org-sec" aria-labelledby="glance-h">
    <h2 id="glance-h">At a glance</h2>
    {_facts(g["facts"], e)}
  </section>{secs}
  <section class="org-sec faq" aria-labelledby="faq-h">
    <h2 id="faq-h">Frequently asked questions</h2>{faq_html}
  </section>
  <section class="org-sec" aria-labelledby="more-h">
    <h2 id="more-h">More</h2>
    <ul class="link-list">{more}</ul>
    <p class="note-line">{legal}</p>
    <p class="note-line">Made by {BRAND}, an independent studio in Turkey. Contact: <a href="mailto:{C}">{C}</a>. Page updated <time datetime="{UPDATED.isoformat()}">{_fmt(UPDATED)}</time>.</p>
  </section>
</main>"""
        ld = [game_ld(g, card),
              {"@context": "https://schema.org", "@type": "FAQPage", "url": SITE + path,
               "mainEntity": [{"@type": "Question", "name": q,
                               "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
                  {"@type": "ListItem", "position": 2, "name": "Games", "item": SITE + "/games/"},
                  {"@type": "ListItem", "position": 3, "name": g["name"], "item": SITE + path}]}]
        write(path.strip("/") + "/index.html",
              page(path=path, title=g["title"], desc=g["desc"], body=body, active="games",
                   image=g["icon"], ld=ld, owner=BRAND,
                   head_extra=f'<meta property="article:modified_time" content="{UPDATED.isoformat()}">\n'))
        urls.append((path, UPDATED))

    # ---------------------------------------------------------------- /games/ hub
    items = "".join(f"""
    <li class="card reveal">
      <img src="{g["icon"]}" alt="{e(cards[g["card"]].get("alt") or g["name"])}" width="72" height="72" loading="lazy" decoding="async">
      <div class="body">
        <h2 class="card-title"><a href="{game_url(g)}">{e(g["name"])}</a></h2>
        <p>{e(g["one_line"])}</p>
        <div class="actions"><a class="story" href="{game_url(g)}">About the game</a></div>
      </div>
    </li>""" for g in GAMES_INFO)
    hub = f"""<main id="main" class="wrap section page-top">
  <header class="page-head">
    <h1>Our games</h1>
    <p class="lead-left">Mobile games by {BRAND}, an independent studio in Turkey. Each page explains what the game is, how it plays, who it's for, what it costs and where to get it.</p>
  </header>
  <ul class="cards">{items}
  </ul>
  <p class="more-link"><a class="btn" href="{GUIDE_EN}">How to play foot tennis</a></p>
</main>"""
    hub_ld = [{"@context": "https://schema.org", "@type": "CollectionPage", "name": f"Games by {BRAND}",
               "url": SITE + "/games/", "inLanguage": "en", "publisher": org,
               "mainEntity": {"@type": "ItemList", "itemListElement": [
                   {"@type": "ListItem", "position": i, "url": SITE + game_url(g), "name": g["name"]}
                   for i, g in enumerate(GAMES_INFO, 1)]}}]
    write("games/index.html", page(path="/games/", title=f"Our Games: Mobile Games by {BRAND}",
                                   desc="Foot Tennis Stars, Tomb Maze, Bolt & Breath, NEO, PROTOKOL-Ø and Prof. Nano: what each game is, how it plays, price and platforms.",
                                   body=hub, active="games", ld=hub_ld, owner=BRAND))
    urls.insert(0, ("/games/", UPDATED))

    # ---------------------------------------------------------------- Turkish guide
    md_file = ctx["ROOT"] / "_icerik_tr" / "ayak-tenisi-nasil-oynanir.md"
    meta, text = ctx["parse_front_matter"](md_file.read_text(encoding="utf-8"))
    lines = text.lstrip().splitlines()
    if lines and lines[0].startswith("# "):
        text = "\n".join(lines[1:])
    html_body = ctx["markdown"].markdown(text, extensions=["extra", "sane_lists"])
    t_date = dt.date.fromisoformat(meta.get("date", UPDATED.isoformat()))
    t_mod = dt.date.fromisoformat(meta.get("updated") or meta.get("date") or UPDATED.isoformat())
    words = len(re.findall(r"\w+", _strip(html_body)))
    minutes = max(1, -(-words // 220))
    fts = cards["Foot Tennis Stars"]
    tr_body = f"""<main id="main" class="post-wrap page-top" lang="tr">
  <article class="post">
    <header class="post-head">
      <img class="post-cover" src="/img/foot-tennis-stars-2.jpg" alt="Ayak Tenisi Yıldızları oyun simgesi" width="96" height="96" decoding="async" fetchpriority="high">
      <p class="crumb"><a href="/games/foot-tennis-stars/" hreflang="en" lang="en">Foot Tennis Stars</a></p>
      <h1>{e(meta["title"])}</h1>
      <p class="post-meta"><time datetime="{t_date.isoformat()}">{t_date.day} {['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık'][t_date.month - 1]} {t_date.year}</time> · {minutes} dk okuma · {BRAND}</p>
      <p class="langswitch"><a href="{GUIDE_EN}" hreflang="en" lang="en">English version</a></p>
    </header>
    <div class="prose">
{html_body}
    </div>
    <p class="post-cta"><a class="btn primary" href="{e(fts["store"])}" target="_blank" rel="noopener">App Store’da indir</a> <a class="btn" href="{e(fts["play"])}" target="_blank" rel="noopener">Google Play’de indir</a></p>
  </article>
</main>"""
    tr_ld = [{"@context": "https://schema.org", "@type": "BlogPosting", "headline": meta["title"],
              "description": meta.get("description", ""), "image": SITE + "/img/foot-tennis-stars-2.jpg",
              "url": SITE + GUIDE_TR, "mainEntityOfPage": SITE + GUIDE_TR, "inLanguage": "tr",
              "datePublished": t_date.isoformat(), "dateModified": t_mod.isoformat(),
              "keywords": meta.get("keywords") if isinstance(meta.get("keywords"), str) else ", ".join(meta.get("keywords") or []),
              "author": {"@type": "Organization", "@id": SITE + "/#org", "name": BRAND},
              "publisher": {"@type": "Organization", "@id": SITE + "/#org", "name": BRAND},
              "about": {"@type": "Thing", "name": "Ayak tenisi", "sameAs": "https://en.wikipedia.org/wiki/Footballtennis"},
              "mentions": {"@id": SITE + "/games/foot-tennis-stars/#game"}},
             {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                 {"@type": "ListItem", "position": 1, "name": "Ana sayfa", "item": SITE + "/"},
                 {"@type": "ListItem", "position": 2, "name": "Foot Tennis Stars", "item": SITE + "/games/foot-tennis-stars/"},
                 {"@type": "ListItem", "position": 3, "name": meta["title"], "item": SITE + GUIDE_TR}]}]
    alt = (f'<link rel="alternate" hreflang="en" href="{SITE}{GUIDE_EN}">\n'
           f'<link rel="alternate" hreflang="tr" href="{SITE}{GUIDE_TR}">\n'
           f'<link rel="alternate" hreflang="x-default" href="{SITE}{GUIDE_EN}">\n'
           f'<meta property="article:published_time" content="{t_date.isoformat()}">\n'
           f'<meta property="article:modified_time" content="{t_mod.isoformat()}">\n')
    write(GUIDE_TR.strip("/") + "/index.html",
          page(path=GUIDE_TR, title=meta.get("seo_title") or meta["title"], desc=meta.get("description", ""),
               body=tr_body, active="", image="/img/foot-tennis-stars-2.jpg", og_type="article",
               ld=tr_ld, head_extra=alt, lang="tr", owner=BRAND))
    urls.append((GUIDE_TR, t_mod))

    # ---------------------------------------------------------------- llms.txt
    lines = [f"# {BRAND}", "",
             f"> Independent mobile game studio in Turkey. The games below are on the App Store (iPhone and iPad); "
             f"Foot Tennis Stars is also on Google Play. Each link is a plain-HTML page with the facts: what the game is, "
             f"how it plays, price model, platforms and an FAQ.", "",
             "## Games", ""]
    for g in GAMES_INFO:
        lines.append(f"- [{g['name']}]({SITE}{game_url(g)}): {g['one_line']}")
    lines += ["", "## Guides", "",
              f"- [How to Play Foot Tennis: Rules, Scoring and Tips]({SITE}{GUIDE_EN}): the real sport's rules (court, net, serve, touches, bounces, scoring) with sources, and how Foot Tennis Stars adapts them.",
              f"- [Ayak tenisi nasıl oynanır? Kurallar, sayı ve ipuçları]({SITE}{GUIDE_TR}): the same guide in Turkish.",
              "", "## Apps", ""]
    for a in ctx["APPS"]:
        store = re.sub(r"apple-store/id(\d+).*", r"id\1", a["store"])
        lines.append(f"- {a['name']}: {a['text']} App Store: {store}")
    lines += ["", "## More", "",
              f"- [All games]({SITE}/games/)",
              f"- [Blog]({SITE}/blog/): development stories behind each game",
              f"- [Prof. Nano for schools]({SITE}/for-schools/)",
              f"- [Foot Tennis Stars partners]({SITE}/foot-tennis-stars/partners/)",
              f"- Contact: {C}", ""]
    write("llms.txt", "\n".join(lines))
    return urls
