# Pure Heart
# Gift reactions. A blocked outfit gets a polite decline instead of MAS's
# "can't read the file" message.

init 16 python:
    _ph_gift_to_cloth = {}
    try:
        for _ngk, _ngv in store.mas_sprites_json.namegift_map.items():
            if _ngk is not None and len(_ngk) == 2 and _ngk[0] == store.mas_sprites.SP_CLOTHES and _ngv:
                _ph_gift_to_cloth[str(_ngv).lower()] = _ngk[1]
    except Exception:
        pass

    def _ph_gift_debug(_why):
        try:
            import os
            import time as _time
            _dir = os.path.join(
                renpy.config.gamedir, u"Submods", u"PureHeart-Submod")
            if not os.path.isdir(_dir):
                os.makedirs(_dir)
            _path = os.path.join(_dir, u"ph_gifts_debug.txt")
            try:
                if os.path.getsize(_path) > 65536:
                    return
            except Exception:
                pass
            _line = u"{0} | {1}\n".format(
                _time.strftime(u"%Y-%m-%d %H:%M:%S"), _why)
            with open(_path, "ab") as _f:
                _f.write(_line.encode("utf-8", "replace"))
        except Exception:
            pass

    def _ph_gift_is_banned(_gname):
        if _ph_blocked_label(str(_gname)):
            return True
        _sid = _ph_gift_to_cloth.get(str(_gname).lower())
        if _sid is not None and (_sid in _ph_block or _sid not in _ph_keep):
            return True
        return False

    def _ph_gift_why(_gname):
        try:
            if _ph_blocked_label(str(_gname)):
                return u"blocked by a banned word or outfit id"
            _sid = _ph_gift_to_cloth.get(str(_gname).lower())
            if _sid is None:
                return u"unknown sprite gift, allowed"
            if _sid in _ph_block:
                return u"outfit on the block list (" + str(_sid) + u")"
            if _sid not in _ph_keep:
                return u"outfit not on the keep list (" + str(_sid) + u")"
            return u"outfit approved (" + str(_sid) + u")"
        except Exception as _e:
            return u"reason check failed: " + repr(_e)

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
            try:
                _names = [str(_g) for _g in gifts] if gifts else []
                _ph_gift_debug(u"gifts seen: {0} ({1})".format(
                    u", ".join(_names) if _names else u"none", len(_names)))
            except Exception:
                pass
            try:
                _orig(gifts, evb_details, gsp_details, gen_details)
            except Exception as _e:
                _ph_gift_debug(u"mas process_gifts error: " + repr(_e))
                return
            try:
                _keep_gsp = []
                for _grd in gsp_details:
                    _gname = _grd.c_gift_name
                    _ban = _gname is not None and _ph_gift_is_banned(str(_gname))
                    if _gname is not None:
                        _ph_gift_debug(u"sprite gift {0}: {1}{2}".format(
                            _gname,
                            u"banned, " if _ban else u"", _ph_gift_why(_gname)))
                    if _ban:
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
                    _ban = _gname is not None and _ph_gift_is_banned(str(_gname))
                    if _gname is not None:
                        _ph_gift_debug(u"generic gift {0}: {1}{2}".format(
                            _gname,
                            u"banned, " if _ban else u"", _ph_gift_why(_gname)))
                    if _ban:
                        evb_details.append(_GRD("ph_gift_decline", _gname, None))
                        try:
                            _mfr.delete_file(_gname)
                        except Exception:
                            pass
                    else:
                        _keep_gen.append(_grd)
                gen_details[:] = _keep_gen

                _ph_gift_debug(u"kept sprite={0} generic={1} events={2}".format(
                    len(gsp_details), len(gen_details), len(evb_details)))
            except Exception as _e:
                _ph_gift_debug(u"filter error: " + repr(_e))

        _mfr.process_gifts = _ph_process_gifts
        _mfr._ph_decline_hooked = True
        _ph_gift_debug(u"gift hook installed, {0} sprite gifts known".format(
            len(_ph_gift_to_cloth)))

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
