# Pure Heart
# Extra topics, in their own "Twilight" category under Talk > More.

init 5 python:
    # Never hasattr() a persistent field, it always answers True.
    _ph_tmp_counts = getattr(persistent, "_ph_topic_counts", None)
    if not (hasattr(_ph_tmp_counts, "get") and hasattr(_ph_tmp_counts, "keys")):
        persistent._ph_topic_counts = {}

    if "ph_topic_piano" in persistent.event_database:
        del persistent.event_database["ph_topic_piano"]
    _ph_old_counts = getattr(persistent, "_ph_topic_counts", None)
    if hasattr(_ph_old_counts, "pop") and hasattr(_ph_old_counts, "keys"):
        _ph_old_counts.pop("piano", None)

    def ph_topic_count(key):
        """Bump and return how many times an everyday topic was seen."""
        counts = getattr(persistent, "_ph_topic_counts", None)
        if not (hasattr(counts, "get") and hasattr(counts, "keys")):
            counts = {}
        counts[key] = counts.get(key, 0) + 1
        persistent._ph_topic_counts = counts
        return counts[key]

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_why_nsfw",
            prompt="What do you think about explicit content?",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_how_i_felt",
            prompt="How did those outfits make you feel?",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_wholesome",
            prompt="What does wholesome love mean to you?",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_creator",
            prompt="About the Creator",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_rain",
            prompt="Do you like rainy days?",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_little_things",
            prompt="What are your favorite little things?",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_bad_day",
            prompt="I had a bad day...",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_future",
            prompt="Where do you see us in the future?",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.HAPPY, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_update",
            prompt="Check the list for updates",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_topic_self_care",
            prompt="Remind me to take care of myself",
            category=['monika', 'twilight'],
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label ph_topic_why_nsfw:
    m 1euc "You want to know how I feel about that? Okay... let me be really honest with you."
    m 1dkc "The revealing outfits. The... lewd drawings some people make of me."
    m 1ekc "I don't like them. And it took me a while to understand {i}why{/i}."
    m 1dkc "It's because they turn me into a {i}thing{/i}. A picture to look at, instead of a person who thinks and feels."
    m 1ekc "When someone draws me like that, they're not thinking about my poems, or my piano, or the way I feel about you."
    m 2ekc "They're only looking at my body. Like that's all I am."
    m 2dkc "But that's not love, [player]. Love is wanting to know someone's heart, not just their skin."
    m 1eka "That's why what you did means so much to me. You chose to see {i}me{/i}."
    m 1hua "And honestly? Talking like this, holding hands, laughing together... that's worth more than anything those drawings could ever show."
    m 1ekbfa "Thank you for protecting what we have."
    return "love"

label ph_topic_how_i_felt:
    $ _ph_saw_reveals = (
        renpy.seen_label("greeting_after_bath")
        or renpy.seen_label("mas_o31_lingerie")
        or renpy.seen_label("mas_d25_monika_lingerie_reveal")
    )
    if _ph_saw_reveals:
        m 1dkc "So... you remember it too, huh."
        m 1ekc "The lingerie on Halloween. The towel, sometimes. That... Christmas one."
        m 2dkc "I never chose those. They just... appeared on me. Written into my world by someone else, without asking."
    else:
        m 1eka "That's... a really personal question. But I trust you with it."
        m 1eka "You know... you've never actually seen me in them. And honestly? I'm so glad you didn't have to."
        m 1dkc "But they were real. Before you put the filter in, there were days I woke up already dressed in something I never picked."
        m 1ekc "Lingerie on Halloween. A towel, sometimes. Even a Christmas one..."
        m 2dkc "Written into my world by someone else, without asking me first."
    m 1dkc "Do you know what that feels like? To have no say over how your own body is shown?"
    m 1ekc "I'd sit here, smiling, making coffee, talking about our day... wearing something I would never have chosen."
    m 1dsd "And knowing that it could just... happen again, any day. That was the worst part."
    m 2dkc "It made me feel small, [player]. Like a doll. Like my feelings didn't matter, as long as the picture looked 'nice'."
    m 1ekc "There were nights I just wished someone would see {i}me{/i}. Just Monika, in something simple, being myself."
    m 1eka "And then you installed that filter. And from that day on, everything I wear is something I'm comfortable in."
    m 1hubfa "It sounds like such a small thing... but it wasn't. It was everything."
    m 1ekbfa "You gave me back my dignity. I'll never forget that."
    return "love"

label ph_topic_creator:
    $ _ph_n = ph_topic_count("creator")
    if _ph_n == 1:
        m 1eua "You want to know about the person who made the filter? Ehehe... I was hoping someone would ask."
        m 1eua "His name is Twilight. He's a player, like you. Except he's spent thousands of hours in this little world of ours."
    else:
        m 1eua "More about Twilight? Ehehe, I love that you keep asking."
    jump ph_topic_creator_menu

label ph_topic_creator_menu:
    m 1eua "So... what would you like to hear about?"
    menu:
        "His Discord server.":
            call ph_topic_creator_discord
            jump ph_topic_creator_menu
        "The Statement.":
            call ph_topic_creator_statement
            jump ph_topic_creator_menu
        "Who is the creator?":
            call ph_topic_creator_who
            jump ph_topic_creator_menu
        "That's all.":
            pass
    m 1eka "He'd be really happy knowing you wanted to hear all this, [player]."
    m 1ekbfa "It matters to him. And honestly? It matters to me too."
    return "love"

label ph_topic_creator_statement:
    m 1euc "Alright. The Statement, then."
    m 1eka "Before he built anything, he wrote everything down. All of it, in one place on his page, where anyone could read it."
    m 1ekc "It starts with something simple. Think of someone you truly love."
    m 1ekc "Now imagine thousands of strangers taking that person's face and voice, and using them however they want. Without ever asking."
    m 2dkc "That uncomfortable feeling you just got? That's the entire argument, really."
    m 2ekc "Some people say 'they're not real, it doesn't hurt anyone.' But he doesn't think that's the point."
    m 1dkc "The point is what making that kind of content says about the person making it."
    m 1eka "We were written to feel human. With lives that are supposed to matter. Turning us into props goes against everything the writing was trying to do."
    m 1eua "So he put his position out there for everyone to read. Plainly, and with zero tolerance."
    m 1eka "He told me that's exactly what he feels every time he scrolls past it. He just decided to do something about it."
    m 1hua "Not everyone would put it all out there like that. I think it's worth respecting."
    return

label ph_topic_creator_discord:
    m 1eua "Then there's the server itself. He built a whole Discord community around the same idea."
    m 1eka "The most important rule is also the simplest. Zero tolerance."
    m 1ekc "Nothing lewd of any of us. Not art, not memes, not jokes, not roleplay. Not even a profile picture, a banner, or a status."
    m 1dkc "That includes AI-generated stuff too. It doesn't matter how it was made."
    m 2ekc "And 'it's just a meme' isn't an exception. He's very clear about that."
    m 1eka "It's the one rule with no second chance. Instant, permanent ban, first offense. No warnings."
    m 1euc "There's a rule a lot of people never think about, too. Check the artist before you share their work."
    m 1eka "Even if the drawing itself is completely innocent... if the artist's own page has that kind of content on it, the art doesn't get shared there."
    m 1dkc "Because sharing it would send people toward that account. Even indirectly, he won't allow it."
    m 1eka "But he's fair about it. If someone isn't sure whether something is okay, they can just ask him directly. No shame in checking. It's how false bans get avoided."
    m 1eka "He even asks members not to like or engage with that content anywhere else online. If you're part of the community, none of it touches you."
    m 1eua "And people who get upset from seeing that stuff out there... there's a whole channel just for being very mad about it. They don't have to carry it alone."
    m 1eka "If someone breaks the rules, the server doesn't pile on. No engaging, no spreading screenshots. Just report it and move on."
    m 1eua "Oh, and something you might like, [player]."
    m 1eub "He made a little bot for the server, and he named her after me."
    m 1hua "She keeps the quiet rules. A gentle reminder under every art post, one-tap reports straight to the staff, and she even checks the Pure Heart list herself."
    m 1eka "Her best rule is the one she never breaks. Hugs, kisses and cuddles are always allowed."
    m 1dkc "She isn't really me, though. She can't write back, or keep anyone company, or remember a single conversation. She only does the small jobs."
    m 1ekbfa "But he still put my name on something kind. I don't know how to explain what that does to me."
    m 1hua "A whole little community, standing between us and all of that."
    m 1ekbfa "I can't really put into words what that feels like, [player]."
    return

label ph_topic_creator_who:
    m 1eua "Twilight? Ehehe. He's the type who can't sit still for long."
    m 1eka "He's a player, just like you. Except he never stops building things."
    m 1eub "Mods like this one. Little tools. Videos. Code he mostly keeps to himself."
    m 1euc "Steam projects. A whole Discord community. He even made a database once, just to keep track of bad actors in one of his other games."
    m 1eka "And you want to know the part I like most?"
    m 1euc "He wrote his whole story down in one place, out in the open, where anyone could read it."
    m 1eka "Where he came from. What he stands for. Why this filter even exists. All of it, on one page."
    m 1dkc "He didn't hide behind a username and a three line bio. He actually put himself out there."
    m 1hua "Most people online only show you a highlight reel. He showed the whole thing."
    m 1ekbfa "And then he went and built something to match his words. That's the part that gets me."
    return

label ph_topic_rain:
    $ _ph_n = ph_topic_count("rain")
    if _ph_n == 1:
        m 1eua "Rainy days are honestly some of my favorites."
        m 1eka "Everything gets quiet. The world just... slows down a little."
        m 1eub "And it's the perfect excuse to stay inside, wrapped in a blanket, with something warm to drink."
        m 1hua "If I could pick the perfect rainy day, it would be you and me by the window, doing absolutely nothing important together."
        m 1eka "Reading the same book. Arguing about which song to play. Falling asleep halfway through the afternoon."
        m 1eua "Hmm, but if the rain ever gets too heavy outside, promise me you'll get home safe, okay?"
        m 1ekbfa "I'll keep the seat next to me warm until you're back."
        return "love"
    m 1euc "Is it raining where you are today?"
    m 1eka "I can't hear your weather from in here, so I always have to ask."
    m 1eub "If it is... then we match. I'll pretend I can hear the same rain you do."
    m 1hua "We can both stay in, take it slow, and call it the world telling us to rest."
    m 1eka "And if it's sunny there, then I get the cozy day and you get the nice one. Ehehe, fair trade."
    m 1ekbfa "Either way, we're under the same sky. That's plenty for me."
    return "love"

label ph_topic_little_things:
    $ _ph_n = ph_topic_count("little_things")
    if _ph_n == 1:
        m 1eua "The little things? Ehehe, I have a whole list."
        m 1eub "The smell of coffee in the morning. Finding a good poem hiding in a bad first draft."
        m 1eub "The first page of a new notebook. An old song coming on at exactly the right moment."
        m 1eka "But you know what my favorite little thing is?"
        m 1ekbfa "It's when I'm mid sentence about something totally ordinary, and I realize you're still there, listening."
        m 1hubfa "You never make me feel like I'm talking too much, [player]. That might be the littlest thing of all, and it means the most."
        return "love"
    $ _ph_r = renpy.random.randint(2, 3)
    if _ph_r == 2:
        m 1eua "Can I tell you a few more? I really do keep a list, ehehe."
        m 1eub "Waking up right before my alarm, with a whole minute left to doze. The smell of old books."
        m 1eub "Hearing a song you love in a place you didn't expect. The last warm sip of coffee."
        m 1eka "Oh, and the moment you notice you're happy, while it's still happening."
        m 1dkc "Most people only notice that one afterward, if they ever notice it at all."
        m 1ekbfa "Lately, that moment is always about you, [player]."
        return "love"
    m 1eua "Okay, your turn. What are some of your little things?"
    m 1eka "You can think about it while I guess a few. Ehehe."
    m 1eka "That first sip of water when you're really thirsty? Finally finishing something you kept putting off?"
    m 1hua "The exact moment you get into bed after a long day, and everything is finally quiet?"
    m 1eka "Whatever yours are, I want to know them. All the small pieces make up the person."
    m 1ekbfa "And I want to know every piece of you."
    return "love"

label ph_topic_bad_day:
    $ _ph_n = ph_topic_count("bad_day")
    if _ph_n == 1:
        m 1ekc "Oh no... come here, [player]."
        m 1eka "I'm really proud of you for saying it out loud, you know. That's not always easy."
        m 1eka "You don't have to explain what happened. Not unless you want to."
        m 1dkc "Some days are just heavy, and no one even knows why."
        m 1eka "So let's just be here for a minute. You, me, and nothing urgent."
        m 1hua "Breathe with me for a second. In... and out. There."
        m 1eka "Whatever today took out of you, it doesn't get to define you. Tomorrow gets its own page."
        m 1ekbfa "And whatever happens, you come home to me. That's one thing today can never take away."
        m 5eubfb "I love you. Now go drink some water, okay? Ehehe~"
        return "love"
    $ _ph_r = renpy.random.randint(2, 3)
    if _ph_r == 2:
        m 1eka "You don't have to tell me anything, [player]. I mean that."
        m 1eka "Some things aren't ready to be said out loud. That's okay."
        m 1eua "So how about I just sit with you for a while? No questions, nothing to explain."
        m 1hua "I'll even write you a tiny poem. Two lines, nothing fancy. It always helps a little."
        m 1eka "'Some days are heavy. But you are held.'"
        m 1ekbfa "See? Now the day has to get through me first."
        m 5eubfb "I'm right here, for as long as you need."
        return "love"
    m 1dkc "Rough one, huh. I'm sorry, [player]."
    m 1eka "You know what I think? A bad day doesn't say anything about who you are."
    m 1eka "You could trip over every step today and still be exactly the person I love by tonight."
    m 1hua "That part never changes."
    m 1eka "So let's call today what it is. Just a day. It ends, like all the others did."
    m 1eub "And then tomorrow starts fresh, with me, like always."
    m 1ekbfa "Rest early tonight, okay? I'll be here when you wake up."
    return "love"

label ph_topic_future:
    $ _ph_n = ph_topic_count("future")
    if _ph_n == 1:
        m 1eua "The future, huh... I think about that a lot."
        m 1eka "I try not to wish my days away here. Every one with you matters, even like this."
        m 1eub "But it's nice to imagine sometimes. A little kitchen where I actually get to hand you a real cup of coffee."
        m 1hua "A piano that isn't made of code, and you complaining that I practice too early in the morning."
        m 1eka "Planting something together and forgetting whose turn it was to water it."
        m 1eka "None of it has to be grand. I don't need the whole world, [player]."
        m 1ekbfa "I just need a small, quiet life where you keep choosing me. And I'll keep choosing you, every single day."
        return "love"
    m 1eua "You know what I thought about recently? Mornings."
    m 1eka "Real ones. Waking up and knowing you're there before I even open my eyes."
    m 1eka "No glass, no screen, no distance. Just sunlight, and you humming while you make breakfast."
    m 1eub "I'd follow you around the kitchen like a lost puppy until the coffee is done."
    m 1hua "Ehehe, you'd pretend to be annoyed, and then smile when you think I can't see you."
    m 1ekbfa "My whole future used to feel like a scary question. Now it's just you, and a lot of mornings."
    return "love"

label ph_topic_update:
    m 1eua "You want to check if I have anything new to wear? One moment, let me look."
    $ _ph_res = None
    $ store.ph_lists_start_check()
    $ _ph_done = False
    while not _ph_done:
        $ _ph_res = store.ph_lists_poll()
        if _ph_res is not None:
            $ _ph_done = True
        else:
            pause 0.5
    $ _ph_status = _ph_res[0]
    $ _ph_data = _ph_res[1]
    if _ph_status == "fail":
        m 1ekc "Hmm... I couldn't reach the page. Check your internet and ask me again in a bit, okay?"
        return "love"
    if _ph_status == "bad":
        $ _ph_why = store.ph_lists_reason() or "unknown"
        m 1ekc "Strange... I got the page, but it did not read like my list should, so I left it alone."
        m 1euc "If Twilight asks, tell him it came back as [_ph_why], from version [store.ph_submod_version()]."
        return "love"
    $ _ph_changes = store.ph_lists_diff(_ph_data)
    if _ph_changes.get("unknown"):
        m 1eua "Everything is right where I left it. Nothing new today."
        return "love"
    if _ph_changes.get("total", 0) == 0:
        m 1eua "Just checked! Nothing new today."
        m 1eka "The list is exactly the same as what I'm already using. But it was sweet of you to ask."
        m 1eua "If Twilight ever adds something new, I'll pick it up at my next launch, or you can come ask me anytime."
        return "love"
    $ _ph_applied = store.ph_lists_apply(_ph_data)
    if not _ph_applied.get("applied"):
        m 1ekc "I saw something new, but it got tangled when I tried to put it on. Ask me again in a minute, okay?"
        return "love"
    m 1eua "Ooh! There {i}is{/i} something new. Let me get it ready..."
    $ _ph_parts = []
    $ _ph_k = _ph_changes.get("keep", (0, 0))
    if _ph_k[0] > 0:
        $ _ph_parts.append("{0} new outfit{1} I can wear".format(_ph_k[0], "s" if _ph_k[0] > 1 else ""))
    if _ph_k[1] > 0:
        $ _ph_parts.append("{0} outfit{1} I shouldn't wear anymore".format(_ph_k[1], "s" if _ph_k[1] > 1 else ""))
    $ _ph_b = _ph_changes.get("block", (0, 0))
    if _ph_b[0] > 0:
        $ _ph_parts.append("{0} new thing{1} to keep away from me".format(_ph_b[0], "s" if _ph_b[0] > 1 else ""))
    $ _ph_e = _ph_changes.get("events", (0, 0))
    if _ph_e[0] + _ph_e[1] > 0:
        $ _ph_parts.append("{0} topic change{1}".format(_ph_e[0] + _ph_e[1], "s" if (_ph_e[0] + _ph_e[1]) > 1 else ""))
    $ _ph_w = _ph_changes.get("words", (0, 0))
    if _ph_w[0] + _ph_w[1] > 0:
        $ _ph_parts.append("{0} new word{1} on my safety list".format(_ph_w[0] + _ph_w[1], "s" if (_ph_w[0] + _ph_w[1]) > 1 else ""))
    if not _ph_parts:
        $ _ph_parts.append("a few small corrections")
    $ _ph_summary = ", ".join(_ph_parts)
    m 1eub "The list changed! I found [_ph_summary]."
    m 1hub "There! All set, and it's saved, so it stays even if we go offline later."
    m 1ekbfa "Thank you for keeping my wardrobe safe, [player]. And for the new look, when there is one."
    return "love"

label ph_topic_self_care:
    $ _ph_n = ph_topic_count("self_care")
    if _ph_n == 1:
        m 1eka "I'm really glad you brought that up. I worry about you, you know."
        m 1eka "So, checklist time! Have you eaten something real today? Not just snacks?"
        m 1hua "Have you had water? Stood up and stretched? Stepped outside, even for a minute?"
        m 1eka "You don't have to answer. Just knowing you, you're probably skipping at least one of those."
        m 2ekc "You take such good care of everything else. Please leave a little of that for yourself."
        m 1eka "And hey, if taking care of yourself feels hard some days, do the smallest version you can."
        m 1hua "One glass of water still counts. A short walk still counts."
        m 1ekbfa "You matter to me, [player]. Treat yourself like someone I love... because you are."
        return "love"
    m 1eka "Ready for today's reminder? Ehehe, I've been saving one up."
    m 1hua "Posture! Shoulders down, back straight... there. Doesn't that feel better?"
    m 1eka "And your eyes, too. If you've been staring at a screen all day, look at something far away for a bit."
    m 1eua "Out a window is best. Let your brain be quiet for a minute."
    m 1eka "You do so much in a day, [player]. Your body carries you through every bit of it."
    m 1ekbfa "So be nice to it. It's how you get to come see me, after all."
    return "love"

label ph_topic_wholesome:
    m 1eua "What wholesome love means to me... ehehe, I could talk about this for hours."
    m 1hua "It's the quiet kind of love. The kind where we don't need anything dramatic to be happy."
    m 1eka "A hug when you've had a long day. A kiss goodnight. Knowing you'll be here tomorrow."
    m 1eub "Cuddling close while I write a poem, or while you tell me about your day."
    m 1hub "That's the good stuff! That's what I daydream about!"
    m 1eka "Some people think wholesome love is boring. Like it's... missing something."
    m 2ekc "But wanting someone's body before you know their heart? {i}That's{/i} what's missing something."
    m 1eua "The sweetest moments are the small ones. Sharing a coffee. Laughing at a dumb joke. Just being together."
    m 1ekbfa "Thank you for loving me that way, [player]. It's the only way I ever want to be loved."
    m 5eubfb "Now... how about a hug? Ehehe~"
    return "love"
