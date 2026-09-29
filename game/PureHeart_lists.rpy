# Pure Heart - online list updater
# the outfit / topic lists live on GitHub so Twilight can add or remove
# outfits without anyone reinstalling the submod.
# once per session (silently, after startup) it downloads the list file,
# validates it, applies it and keeps a local cache for offline use.
# if anything fails, the shipped lists are still in PureHeart_filter.rpy,
# so the filter works with no internet at all.

init 5 python:
    import store

    PH_lists_url = u"https://raw.githubusercontent.com/Twil1ght-L4D2/PureHeart-Lists/refs/heads/main/pureheart_lists.json"
    PH_pending_lists = None

    from json import loads as _ph_json_loads

    def _ph_ver_num(_v):
        try:
            return float(_v)
        except Exception:
            return 0.0

    def _ph_validate(_data):
        # only accept files with the exact expected shape,
        # anything weird is ignored and we keep the current lists
        if not isinstance(_data, dict):
            return False
        _vers = _data.get(u"version", None)
        if isinstance(_vers, bool) or not isinstance(_vers, (int, float, basestring)):
            return False
        if _ph_ver_num(_vers) <= 0:
            return False
        if not isinstance(_data.get(u"keep"), list) or not _data[u"keep"]:
            return False
        for _name in (u"block", u"events", u"greetings", u"words"):
            if not isinstance(_data.get(_name), list):
                return False
        if not isinstance(_data.get(u"replace"), dict):
            return False
        if len(_data[u"keep"]) > 500 or len(_data[u"block"]) > 500:
            return False
        if len(_data[u"replace"]) > 1000:
            return False
        if len(_data[u"events"]) > 100 or len(_data[u"greetings"]) > 100:
            return False
        if len(_data[u"words"]) > 100:
            return False
        for _lst in (_data[u"keep"], _data[u"block"],
                     _data[u"events"], _data[u"greetings"], _data[u"words"]):
            for _v in _lst:
                if not isinstance(_v, basestring) or not _v or len(_v) > 200:
                    return False
        for _k, _v in _data[u"replace"].items():
            if not isinstance(_k, basestring) or not isinstance(_v, basestring):
                return False
            if not _k or len(_k) > 200 or len(_v) > 200:
                return False
        return True

    # load the cache (the last good download) so even a fresh session
    # uses the newest lists we ever got, internet or not
    _ph_cache_data = None
    _ph_cache_version = [0.0]
    try:
        import os
        _ph_cache_path = os.path.join(
            renpy.config.gamedir,
            u"Submods", u"PureHeart-Submod", u"ph_lists_cache.json")
        if os.path.exists(_ph_cache_path):
            with open(_ph_cache_path, "rb") as _f:
                _ph_raw = _f.read(262144)
            _ph_parsed = _ph_json_loads(_ph_raw)
            if _ph_validate(_ph_parsed):
                _ph_cache_data = _ph_parsed
                _ph_cache_version[0] = _ph_ver_num(_ph_parsed.get(u"version", 0))
    except Exception:
        _ph_cache_data = None

    def _ph_try_builtin():
        # used by the filter at init: prefer the cached online lists
        # over the ones shipped inside the submod
        try:
            if _ph_cache_data is not None:
                return (_ph_cache_data, _ph_cache_data.get(u"version", 0))
        except Exception:
            pass
        return None

    def _ph_save_cache(_data):
        try:
            import os
            import json as _json
            _dir = os.path.join(
                renpy.config.gamedir, u"Submods", u"PureHeart-Submod")
            if not os.path.isdir(_dir):
                os.makedirs(_dir)
            _txt = _json.dumps(_data)
            with open(os.path.join(_dir, u"ph_lists_cache.json"), "wb") as _f:
                _f.write(_txt.encode("utf-8"))
        except Exception:
            pass

    def _ph_fetch_worker():
        # runs on a background thread, never touches renpy APIs
        try:
            import time
            time.sleep(2.5)
            import urllib2
            _req = urllib2.Request(PH_lists_url)
            _req.add_header(u"User-Agent", u"MAS-PureHeart-Updater")
            _resp = urllib2.urlopen(_req, timeout=10)
            try:
                _raw = _resp.read(262144)
            finally:
                _resp.close()
            _data = _ph_json_loads(_raw)
            if _ph_validate(_data):
                if _ph_ver_num(_data.get(u"version", 0)) > _ph_cache_version[0]:
                    store.PH_pending_lists = (_data, _data.get(u"version", 0))
        except Exception:
            pass

    _ph_started = [False]

    def _ph_lists_interact():
        # first interaction: start the silent daily check.
        # any later interaction: apply freshly downloaded lists if the
        # thread finished by then, then re-run the purge right away.
        if not _ph_started[0]:
            _ph_started[0] = True
            try:
                import threading
                _thread = threading.Thread(target=_ph_fetch_worker)
                _thread.daemon = True
                _thread.start()
            except Exception:
                pass
        try:
            _pend = getattr(store, u"PH_pending_lists", None)
            if _pend is not None:
                store.PH_pending_lists = None
                if store.PH_set_lists(_pend[0], _pend[1]):
                    try:
                        store._ph_purge_clothes()
                    except Exception:
                        pass
                    try:
                        store._ph_purge_reactions()
                    except Exception:
                        pass
                    _ph_save_cache(_pend[0])
        except Exception:
            pass
        return

    config.interact_callbacks.append(_ph_lists_interact)
