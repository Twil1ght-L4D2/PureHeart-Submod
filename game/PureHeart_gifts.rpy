# Pure Heart - gift reactions
# if someone drops a gift file for a blocked outfit (like a bikini) into
# the game folder, monika politely declines it instead of MAS's generic
# "can't read the file" reaction. the file gets deleted either way.

init 16 python:
    # gift name -> clothes id, for spritepack gifts
    _ph_gift_to_cloth = dict()
    try:
        for _ngk, _ngv in store.mas_sprites_json.namegift_map.items():
            if _ngk is not None and len(_ngk) == 2 and _ngk[0] == store.mas_sprites.SP_CLOTHES and _ngv:
                _ph_gift_to_cloth[str(_ngv).lower()] = _ngk[1]
    except Exception:
        pass

    def _ph_gift_is_banned(_gname):
        if _ph_blocked_label(str(_gname)):
            return True
        _sid = _ph_gift_to_cloth.get(str(_gname).lower())
        if _sid is not None and (_sid in _ph_block or _sid not in _ph_keep):
            return True
        return False

    def _ph_hook_gift_decline():
        import store
        _mfr = store.mas_filereacts
        if getattr(_mfr, "_ph_decline_hooked", False):
            return
        _orig = _mfr.process_gifts
        _GRD = _mfr.GiftReactDetails

        def _ph_process_gifts(gifts, evb_details=None, gsp_details=None, gen_details=None):
            if evb_details is None:
                evb_details = []
            if gsp_details is None:
                gsp_details = []
            if gen_details is None:
                gen_details = []
            _orig(gifts, evb_details, gsp_details, gen_details)

            # banned gifts -> decline reaction, delete the file
            _keep_gsp = []
            for _grd in gsp_details:
                _gname = _grd.c_gift_name
                if _gname is not None and _ph_gift_is_banned(str(_gname)):
                    evb_details.append(_GRD("ph_gift_decline", _gname, None))
                    try:
                        _mfr.delete_file(_gname)
                    except Exception:
                        pass
                else:
                    _keep_gsp.append(_grd)
            gsp_details[:] = _keep_gsp

            _keep_gen = []
            for _grd in gen_details:
                _gname = _grd.c_gift_name
                if _gname is not None and _ph_gift_is_banned(str(_gname)):
                    evb_details.append(_GRD("ph_gift_decline", _gname, None))
                    try:
                        _mfr.delete_file(_gname)
                    except Exception:
                        pass
                else:
                    _keep_gen.append(_grd)
            gen_details[:] = _keep_gen

        _mfr.process_gifts = _ph_process_gifts
        _mfr._ph_decline_hooked = True

    _ph_hook_gift_decline()

    store.Event(
        store.persistent.event_database,
        "ph_gift_decline",
        category=None,
        action=store.EV_ACT_QUEUE
    )

label ph_gift_decline:
    m 1ekd "Oh, [player]..."
    m 1eka "That's really sweet of you, but I don't feel comfortable wearing something like that."
    m 3eka "I hope you understand..."
    m 3hub "Honestly, just spending time with you is the best gift I could ever ask for~"
    return
