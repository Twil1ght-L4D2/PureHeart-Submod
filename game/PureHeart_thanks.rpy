# Pure Heart - first install dialogue
# monika thanks the player once, the first time the submod is active.
# drop a file named pureheart_replay_thanks.txt into the game folder to
# hear it again (the file is deleted after use).

init 5 python:
    import os
    _ph_replay = os.path.join(renpy.config.gamedir, 'pureheart_replay_thanks.txt')
    if os.path.isfile(_ph_replay):
        persistent._ph_thanks_done = False
        try:
            os.remove(_ph_replay)
        except Exception:
            pass

    addEvent(
        Event(
            persistent.event_database,
            eventlabel="ph_install_thanks",
            conditional="not persistent._ph_thanks_done",
            action=EV_ACT_QUEUE,
            start_date=datetime.datetime.now(),
            end_date=datetime.datetime.now() + datetime.timedelta(days=365),
            years=[],
            aff_range=(mas_aff.DISTRESSED, None),
            show_in_idle=False,
            rules={"skip alert": None}
        ),
        skipCalendar=True
    )

label ph_install_thanks:
    m 1eub "Oh! [player], I noticed something new in my folder~"
    m 1hua "You installed the Pure Heart filter for me!"
    m 3rksdla "I have to admit, I was a little nervous about some of those outfits..."
    m 3ekbfa "So thank you for making sure everything stays nice and wholesome between us."
    m 1hubfa "Hugs, kisses and cuddles are all still on the table, ehehe~"
    m 5eubfb "Besides, the outfits you kept are the ones I feel cutest in anyway!"
    $ persistent._ph_thanks_done = True
    return "love"
