# Pure Heart
# Outfit and topic filter. Runs at init 15, and re-applies on every launch.

init 15 python:
    # >>> PH_BUILTIN_LISTS
    _ph_keep = [
        u'def', u'blazerless', u'blackdress', u'marisa', u'rin', u'santa',
        u'nou_shirt', u'clothes_otter_keqing_outfit',
        u'finale_and_otter_hoodie_purple', u'briaryoung_button_up_flowered',
        u'briaryoung_shuchiin_academy_uniform',
        u'briaryoung_sleeveless_turtleneck_black',
        u'briaryoung_tshirt_jurassic_park',
        u'briaryoung_tshirt_jurassic_world', u'finale_jacket_brown',
        u'finale_putonahappyface_shirt', u'finale_shirt_blue',
        u'finale_shirt_resthere', u'finale_sweatervest_blue',
        u'finale_turtleneck_sweater_beige', u'mayjay_pink_kimono',
        u'mocca_bun_blackandwhitestripedpullover',
        u'orcaramelo_sakuya_izayoi', u'orcaramelo_sweater_shoulderless',
        u'orcaramelo_sweater_shoulderless_edit_brown',
        u'orcaramelo_sweater_shoulderless_white_edit',
        u'mj_darkywgreen_dress_recolor', u'mj_lightywgreen_dress_recolor',
        u'mj_regywgreen_dress_recolor', u'delicake_blanket',
        u'pink_polkadot_pajama', u'birthday2026_blue_dress',
    ]
    _ph_block = [
        u'bath_towel_white', u'blackpink_dress', u'dress_newyears',
        u'santa_lingerie', u'spider_lingerie', u'sundress_white',
        u'vday_lingerie', u'briaryoung_bralette_red_ruffles',
        u'briaryoung_heart_cut_bikini_black',
        u'briaryoung_heart_cut_bikini_green',
        u'briaryoung_heart_cut_bikini_pink',
        u'briaryoung_heart_cut_bikini_purple',
        u'briaryoung_heart_cut_bikini_white',
        u'briaryoung_heart_cut_bikini_yellow',
        u'briaryoung_vcut_crossed_straps_tanktop_white', u'finale_tanktop',
        u'orcaramelo_bikini_shell', u'clothes_otter_blacktanktop',
        u'clothes_otter_lisa_outfit', u'clothes_otter_fishnets',
        u'briaryoung_dress_dark_blue_sparkle', u'finale_green_dress',
        u'finale_hoodie_green', u'hatana_2b',
        u'multimokia_wine_asymmetrical_pullover', u'orcaramelo_hatsune_miku',
        u'velius94_dress_whitenavyblue', u'velius94_shirt_pink',
        u'mj_rose_valentines_dress_red',
    ]
    _ph_replace = {
        u'dress_newyears': u'blackdress',
        u'blackpink_dress': u'blackdress',
        u'sundress_white': u'blackdress',
        u'santa_lingerie': u'santa',
        u'spider_lingerie': u'blackdress',
        u'vday_lingerie': u'blackdress',
        u'bath_towel_white': u'blazerless',
        u'briaryoung_bralette_red_ruffles': u'finale_shirt_blue',
        u'briaryoung_vcut_crossed_straps_tanktop_white': u'finale_shirt_blue',
        u'finale_tanktop': u'finale_shirt_blue',
        u'orcaramelo_bikini_shell': u'finale_shirt_blue',
        u'clothes_otter_blacktanktop': u'finale_shirt_blue',
        u'clothes_otter_lisa_outfit': u'clothes_otter_keqing_outfit',
        u'clothes_otter_fishnets': u'clothes_otter_keqing_outfit',
        u'briaryoung_dress_dark_blue_sparkle': u'blackdress',
        u'finale_green_dress': u'blackdress',
        u'hatana_2b': u'finale_jacket_brown',
        u'multimokia_wine_asymmetrical_pullover': u'mocca_bun_blackandwhitestripedpullover',
        u'orcaramelo_hatsune_miku': u'orcaramelo_sakuya_izayoi',
        u'velius94_dress_whitenavyblue': u'blackdress',
        u'velius94_shirt_pink': u'finale_shirt_blue',
        u'mj_rose_valentines_dress_red': u'blackdress',
        u'finale_hoodie_green': u'finale_jacket_brown',
    }
    _ph_events = [
        u'monika_nsfw', u'monika_panties', u'monika_idle_shower',
        u'mas_o31_lingerie', u'mas_d25_monika_lingerie_reveal',
        u'mas_after_bath_cleanup', u'monika_pleasure', u'mas_wrs_r34m',
        u'mas_nye_monika_nye_dress_intro', u'mas_nye_monika_nyd',
    ]
    _ph_greetings = [
        u'greeting_o31_lingerie', u'greeting_after_bath',
    ]
    _ph_words = [
        u'lingerie', u'nude', u'nudes', u'naked', u'nsfw', u'lewd',
        u'hentai', u'porn', u'r18', u'sexy', u'erotic', u'bikini',
        u'bralette', u'swimsuit', u'underwear', u'towel', u'topless',
        u'panties', u'bra_',
    ]
    # <<< PH_BUILTIN_LISTS

    # list/dict/set are shadowed in some store namespaces, so stick to
    # comprehensions and literals.
    _ph_active = {
        u"keep": [_v for _v in _ph_keep],
        u"block": [_v for _v in _ph_block],
        u"replace": {_k: _v for _k, _v in _ph_replace.items()},
        u"events": [_v for _v in _ph_events],
        u"greetings": [_v for _v in _ph_greetings],
        u"words": [_v for _v in _ph_words],
    }
    _ph_list_version = u"1"

    def PH_set_lists(_data, _version):
        global _ph_active, _ph_list_version
        _old_ev = {}
        for _e in _ph_active[u"events"]:
            _old_ev[_e] = True
        _old_gr = {}
        for _g in _ph_active[u"greetings"]:
            _old_gr[_g] = True
        _ph_active = {
            u"keep": [_v for _v in (_data.get(u"keep") or [])],
            u"block": [_v for _v in (_data.get(u"block") or [])],
            u"replace": {_k: _v for _k, _v in (_data.get(u"replace") or {}).items()},
            u"events": [_v for _v in (_data.get(u"events") or [])],
            u"greetings": [_v for _v in (_data.get(u"greetings") or [])],
            u"words": [_v for _v in (_data.get(u"words") or [])],
        }
        if not _ph_active[u"keep"]:
            _ph_active[u"keep"] = [_v for _v in _ph_keep]
        if not _ph_active[u"block"]:
            _ph_active[u"block"] = [_v for _v in _ph_block]
        if not _ph_active[u"words"]:
            _ph_active[u"words"] = [_v for _v in _ph_words]
        _ph_list_version = str(_version)
        for _lbl in _ph_active[u"events"]:
            if _lbl not in _old_ev:
                _ph_lock_ev(_lbl, 'EVE')
        for _lbl in _ph_active[u"greetings"]:
            if _lbl not in _old_gr:
                _ph_lock_ev(_lbl, 'GRE')
        return True

    def _ph_bad(text):
        text = (text or '').lower()
        for _w in _ph_active[u"words"]:
            if _w in text:
                return True
        return False

    def _ph_blocked_label(_lab):
        if _lab is None:
            return False
        _lab = str(_lab)
        if _ph_bad(_lab):
            return True
        for _cid in _ph_active[u"block"]:
            if _cid in _lab:
                return True
        return False

    def _ph_purge_reactions():
        import store
        try:
            _mfr = store.mas_filereacts
        except Exception:
            return
        try:
            for _lab in list(_mfr.filereact_db.keys()):
                if _ph_blocked_label(_lab):
                    _mfr.filereact_db.pop(_lab, None)
        except Exception:
            pass
        try:
            for _fname in list(_mfr.filereact_map.keys()):
                if _ph_blocked_label(_mfr.filereact_map.get(_fname)):
                    _mfr.filereact_map.pop(_fname, None)
        except Exception:
            pass
        try:
            for _fname in list(_mfr.foundreact_map.keys()):
                if _ph_blocked_label(_mfr.foundreact_map.get(_fname)):
                    _mfr.foundreact_map.pop(_fname, None)
        except Exception:
            pass

    def _ph_purge_clothes():
        import store
        _sprites = store.mas_sprites
        _selspr = store.mas_selspr
        _removed = []
        try:
            for _cid in list(_sprites.CLOTH_MAP.keys()):
                if _cid in _ph_active[u"block"] or _cid not in _ph_active[u"keep"] or _ph_bad(_cid):
                    _removed.append(_cid)
        except Exception:
            pass
        for _cid in _removed:
            _cloth = _sprites.CLOTH_MAP.get(_cid, None)
            try:
                if _cloth is not None and store.monika_chr is not None and store.monika_chr.clothes is _cloth:
                    _repl_id = _ph_active[u"replace"].get(_cid, u'def')
                    _repl = _sprites.CLOTH_MAP.get(_repl_id, None)
                    if _repl is None:
                        _repl = _sprites.mas_clothes_def
                    store.monika_chr.change_clothes(_repl, by_user=False)
            except Exception:
                pass
            try:
                _sprites.CLOTH_MAP.pop(_cid, None)
            except Exception:
                pass
            try:
                _sel = _selspr.CLOTH_SEL_MAP.pop(_cid, None)
                if _sel is not None:
                    if _sel in _selspr.CLOTH_SEL_SL:
                        _selspr.CLOTH_SEL_SL.remove(_sel)
                    _sel.unlocked = False
                    _sel.visible_when_locked = False
            except Exception:
                pass
        try:
            _gifted = store.persistent._mas_sprites_json_gifted_sprites
            if _gifted:
                for _key in list(_gifted.keys()):
                    if _ph_bad(_key) or _key in _ph_active[u"block"] or _key not in _ph_active[u"keep"]:
                        _gifted.pop(_key, None)
        except Exception:
            pass
        try:
            if store.persistent._mas_force_clothes:
                store.persistent._mas_force_clothes = False
        except Exception:
            pass
        # MAS looks these ids up directly, so a purged one needs a replacement.
        try:
            _emap = store.persistent._mas_event_clothes_map
            if _emap:
                for _key in list(_emap.keys()):
                    _val = _emap.get(_key, None)
                    if _val is None or _ph_bad(_val) or _val in _ph_active[u"block"] or _val not in _ph_active[u"keep"]:
                        _emap[_key] = _ph_active[u"replace"].get(_val, u'blackdress')
        except Exception:
            pass
        return _removed

    def _ph_lock_ev(_lbl, _code):
        import store
        try:
            store.mas_stripEVL(_lbl)
        except Exception:
            pass
        try:
            store.mas_lockEVL(_lbl, _code)
        except Exception:
            pass
        try:
            store.mas_hideEVL(_lbl, _code, lock=True, derandom=True, depool=True, decond=True)
        except Exception:
            pass

    try:
        import store
        _builtin = store._ph_try_builtin()
        if _builtin is not None:
            PH_set_lists(_builtin[0], _builtin[1])
    except Exception:
        pass

    _ph_removed = _ph_purge_clothes()
    _ph_purge_reactions()
    for _lbl in _ph_active[u"events"]:
        _ph_lock_ev(_lbl, 'EVE')
    for _lbl in _ph_active[u"greetings"]:
        _ph_lock_ev(_lbl, 'GRE')

    _ph_checked_once = [False]

    def _ph_first_interact():
        try:
            import store
            if getattr(store, "PH_pending_lists", None) is not None:
                _pend = store.PH_pending_lists
                store.PH_pending_lists = None
                PH_set_lists(_pend[0], _pend[1])
                _ph_purge_clothes()
                _ph_purge_reactions()
        except Exception:
            pass
        if _ph_checked_once[0]:
            return
        _ph_checked_once[0] = True
        _ph_purge_clothes()
        _ph_purge_reactions()
        return

    config.interact_callbacks.append(_ph_first_interact)
