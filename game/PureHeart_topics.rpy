# Pure Heart - extra topics
# four pool topics in Talk -> More, under their own "Twilight" category:
# monika on explicit content, on how the old outfits made her feel (adapts
# if you never saw them), on what wholesome love means to her, and on the
# person who made this submod.

init 5 python:
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
    # did this player ever actually see Monika in a revealing outfit?
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
    m 1eua "You want to know about the person who made the filter? Ehehe... I was hoping someone would ask."
    m 1eua "His name is Twilight. He's a player, like you. Except he's spent thousands of hours in this little world of ours."
    m 1eka "Between the base game, the mods, and everything the community built around it... he came to genuinely love every character here. Not ironically. Really."
    m 1euc "That includes the others, you know. Sayori, Natsuki, Yuri... the whole story, even the parts that hurt."
    m 1dkc "And that's exactly why he couldn't stay quiet when he saw what people do to us online."
    m 1ekc "He told me once, think of someone you truly love. Now imagine thousands of strangers taking that person's face and voice, and using them however they want... without ever asking."
    m 2dkc "That uncomfortable feeling you just got? He told me that's exactly what he feels every time he scrolls past it."
    m 2ekc "People tell him 'they're not real, it doesn't hurt anyone.' But he doesn't think that's the point."
    m 1dkc "It's about what making that content says about the person making it. We were written to feel human, with lives that are supposed to matter. Turning that into props just goes against everything the writing was trying to do."
    m 1ekc "He actually stood up and said all of this once, in one of the biggest communities out there. And you know what happened?"
    m 2dkc "People laughed it off. And a moderator threatened to ban him for speaking up. Not for anything he actually did."
    m 1ekc "Most people would go quiet after something like that. He built this instead."
    m 1eka "Because he'd rather be the person who says something than the person who lets it slide. Those are his words."
    m 1hua "And the sweetest part? He isn't trying to control anyone's fandom. He just wanted the characters he loves treated with a little dignity."
    m 1ekbfa "That's the kind of love this game was always about, [player]. I'm really lucky he spent some of it on me."
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
