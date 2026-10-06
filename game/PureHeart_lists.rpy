# Pure Heart
# Online list updater. Downloads the GitHub lists once per session, applies
# them, and caches them so the filter still works offline.

init 5 python:
    import store

    PH_lists_url = u"https://raw.githubusercontent.com/Twil1ght-L4D2/PureHeart-Lists/refs/heads/main/pureheart_lists.json"
    PH_pending_lists = None
    _ph_submod_version = u"1.20"

    from json import loads as _ph_json_loads

    # Some installs shadow dict inside the store, which makes isinstance on a
    # real dict answer False. Capture the real builtins once.
    try:
        import __builtin__ as _ph_builtins
    except Exception:
        import builtins as _ph_builtins
    _ph_dict_type = _ph_builtins.dict
    _ph_list_type = _ph_builtins.list
    _ph_str_type = getattr(_ph_builtins, u"basestring", None)
    if _ph_str_type is None:
        _ph_str_type = (type(b""), type(u""))

    def _ph_type_name(_x):
        try:
            return u"{0}".format(type(_x).__name__)
        except Exception:
            return u"?"

    def _ph_is_str(_x):
        try:
            return isinstance(_x, _ph_str_type)
        except Exception:
            return False

    def _ph_is_map(_x):
        try:
            return isinstance(_x, _ph_dict_type) or (
                hasattr(_x, u"keys") and hasattr(_x, u"get")
                and hasattr(_x, u"__getitem__"))
        except Exception:
            return False

    def _ph_is_seq(_x):
        try:
            if _ph_is_str(_x):
                return False
            if isinstance(_x, _ph_list_type):
                return True
            return hasattr(_x, u"__iter__") and not hasattr(_x, u"keys")
        except Exception:
            return False

    def _ph_reload_from_disk(_raw):
        try:
            import os
            _tmp_path = os.path.join(
                renpy.config.gamedir, u"ph_lists_staging.json")
            with open(_tmp_path, "wb") as _f:
                _f.write(_raw)
            with open(_tmp_path, "rb") as _f:
                _from_disk = _ph_json_loads(_f.read())
            try:
                os.remove(_tmp_path)
            except Exception:
                pass
            return _from_disk
        except Exception:
            return None

    def _ph_parse(_raw):
        _d = None
        try:
            _d = _ph_json_loads(_raw)
        except Exception:
            _d = None
        _guard = 0
        while _ph_is_str(_d) and _guard < 3:
            _guard += 1
            try:
                _d = _ph_json_loads(_d)
            except Exception:
                _d = None
                break
        if not _ph_is_map(_d):
            _d2 = _ph_reload_from_disk(_raw)
            if _ph_is_map(_d2):
                _d = _d2
        if not _ph_is_map(_d):
            return None
        return _d

    def ph_submod_version():
        return _ph_submod_version

    def _ph_debug_note(_why, _raw=None):
        try:
            import os
            import time as _time
            _dir = os.path.join(
                renpy.config.gamedir,
                u"Submods", u"PureHeart-Submod")
            if not os.path.isdir(_dir):
                os.makedirs(_dir)
            _path = os.path.join(_dir, u"ph_lists_debug.txt")
            try:
                if os.path.getsize(_path) > 65536:
                    return
            except Exception:
                pass
            _head = u""
            if _raw is not None:
                try:
                    _head = repr(_raw[:200])
                except Exception:
                    _head = u"(unprintable)"
            _txt = u"{0} | v{1} | {2} | {3}\n".format(
                _time.strftime(u"%Y-%m-%d %H:%M:%S"),
                _ph_submod_version, _why, _head)
            with open(_path, "ab") as _f:
                _f.write(_txt.encode("utf-8", "replace"))
        except Exception:
            pass

    def _ph_ver_num(_v):
        try:
            return float(_v)
        except Exception:
            return 0.0

    def _ph_validate_detail(_data):
        try:
            if not _ph_is_map(_data):
                return (False, u"not a map (" + _ph_type_name(_data) + u")")
            _vers = _data.get(u"version", None)
            if _vers is None:
                return (False, u"no version")
            if _ph_ver_num(_vers) <= 0:
                return (False, u"version not positive")
            _keep = _data.get(u"keep", None)
            if not _ph_is_seq(_keep) or len(_keep) < 1:
                return (False, u"no keep list (" + _ph_type_name(_keep) + u")")
            for _k in (u"block", u"events", u"greetings", u"words"):
                if not _ph_is_seq(_data.get(_k)):
                    _data[_k] = []
            if not _ph_is_map(_data.get(u"replace")):
                _data[u"replace"] = {}
            for _k in (u"keep", u"block", u"events", u"greetings", u"words"):
                _data[_k] = [
                    _v for _v in _data[_k]
                    if _ph_is_str(_v) and len(_v) <= 200]
            _newrep = {}
            for _k, _v in _data[u"replace"].items():
                if (_ph_is_str(_k) and _ph_is_str(_v)
                        and len(_k) <= 200 and len(_v) <= 200):
                    _newrep[_k] = _v
            _data[u"replace"] = _newrep
            return (True, u"ok")
        except Exception as _e:
            return (False, u"check error: " + repr(_e))

    def _ph_validate(_data):
        return _ph_validate_detail(_data)[0]

    def _ph_content_differs(_new, _old):
        try:
            if not _ph_is_map(_old):
                return True
            for _k in (u"keep", u"block", u"events", u"greetings", u"words"):
                _o = _old.get(_k) or []
                _n = _new.get(_k) or []
                if len(_o) != len(_n):
                    return True
                _map_o = {}
                for _v in _o:
                    _map_o[_v] = True
                for _v in _n:
                    if _v not in _map_o:
                        return True
            if (_old.get(u"replace") or {}) != (_new.get(u"replace") or {}):
                return True
            return False
        except Exception:
            return True

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
            _ph_parsed = _ph_parse(_ph_raw)
            if _ph_parsed is not None and _ph_validate(_ph_parsed):
                _ph_cache_data = _ph_parsed
                _ph_cache_version[0] = _ph_ver_num(_ph_parsed.get(u"version", 0))
    except Exception:
        _ph_cache_data = None

    if _ph_cache_data is None:
        try:
            _ph_saved = getattr(persistent, u"_ph_lists_saved", None)
            if _ph_saved is not None and _ph_validate(_ph_saved):
                _ph_cache_data = _ph_saved
                _ph_cache_version[0] = _ph_ver_num(_ph_saved.get(u"version", 0))
        except Exception:
            pass

    def _ph_try_builtin():
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
        # Cached lists live in the submod folder, so keep a copy in the save
        # data too.
        try:
            persistent._ph_lists_saved = _data
        except Exception:
            pass

    def _ph_fetch_worker():
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
            _data = _ph_parse(_raw)
            _ok = False
            if _data is not None:
                _ok = _ph_validate(_data)
            if _ok:
                _cur = getattr(store, u"_ph_active", None)
                if (_ph_ver_num(_data.get(u"version", 0)) > _ph_cache_version[0]
                        or _ph_content_differs(_data, _cur)):
                    store.PH_pending_lists = (_data, _data.get(u"version", 0))
            elif _data is None:
                _ph_debug_note(u"auto check: could not read the file", _raw)
            else:
                _ok2, _why = _ph_validate_detail(_data)
                _ph_debug_note(u"auto check: rejected (" + _why + u")", _raw)
        except Exception as _e:
            _ph_debug_note(u"auto check: download error: " + repr(_e))

    _ph_manual_state = [u"idle"]
    _ph_manual_data = [None]
    _ph_manual_reason = [u""]

    def _ph_manual_worker():
        _saw_bad = False
        _saw_fail = False
        for _attempt in (1, 2):
            if _attempt == 2:
                try:
                    import time as _t
                    _t.sleep(1.5)
                except Exception:
                    pass
            try:
                import urllib2
                _req = urllib2.Request(PH_lists_url)
                _req.add_header(u"User-Agent", u"MAS-PureHeart-Updater")
                _resp = urllib2.urlopen(_req, timeout=6)
                try:
                    _raw = _resp.read(262144)
                finally:
                    _resp.close()
                _data = _ph_parse(_raw)
                _ok = False
                if _data is not None:
                    _ok = _ph_validate(_data)
                if _ok:
                    _ph_manual_data[0] = _data
                    _ph_manual_state[0] = u"ok"
                    _ph_manual_reason[0] = u"ok"
                    return
                if _data is None:
                    _saw_fail = True
                    _ph_manual_reason[0] = u"could not read the file"
                    _ph_debug_note(u"manual check: could not read the file")
                else:
                    _saw_bad = True
                    _ok2, _why = _ph_validate_detail(_data)
                    _ph_manual_reason[0] = _why
                    _ph_debug_note(u"manual check: rejected (" + _why + u")", _raw)
            except Exception as _e:
                _saw_fail = True
                _ph_debug_note(u"manual check: download error: " + repr(_e))
        if _saw_bad:
            _ph_manual_state[0] = u"bad"
        else:
            _ph_manual_state[0] = u"fail"

    def ph_lists_start_check():
        """Begin a manual list check. False if one is already running."""
        if _ph_manual_state[0] == u"running":
            return False
        _ph_manual_state[0] = u"running"
        _ph_manual_data[0] = None
        try:
            import threading
            _thread = threading.Thread(target=_ph_manual_worker)
            _thread.daemon = True
            _thread.start()
            return True
        except Exception:
            _ph_manual_state[0] = u"fail"
            return False

    def ph_lists_poll():
        """None while checking, else (status, data or None).
        status is one of: ok, bad, fail."""
        if _ph_manual_state[0] == u"running":
            return None
        return (_ph_manual_state[0], _ph_manual_data[0])

    def ph_lists_diff(_data):
        """Compare candidate lists to the active ones.
        Returns a dict: each list key maps to (added, removed) counts,
        replace maps to changed-pair count, total sums everything."""
        _changes = {}
        _old = getattr(store, u"_ph_active", None)
        if not _ph_is_map(_old):
            _changes[u"unknown"] = True
            _changes[u"total"] = 1
            return _changes
        _total = 0
        for _key in (u"keep", u"block", u"events", u"greetings", u"words"):
            try:
                _o = _old.get(_key) or []
                _n = _data.get(_key) or []
                _map_o = {}
                for _v in _o:
                    _map_o[_v] = True
                _map_n = {}
                for _v in _n:
                    _map_n[_v] = True
                _a = len([_v for _v in _n if _v not in _map_o])
                _r = len([_v for _v in _o if _v not in _map_n])
                _changes[_key] = (_a, _r)
                _total += _a + _r
            except Exception:
                _changes[_key] = (0, 0)
        try:
            _old_r = _old.get(u"replace") or {}
            _new_r = _data.get(u"replace") or {}
            _keys = {}
            for _k in _old_r:
                _keys[_k] = True
            for _k in _new_r:
                _keys[_k] = True
            _ch = 0
            for _k in _keys:
                if _old_r.get(_k) != _new_r.get(_k):
                    _ch += 1
            _changes[u"replace"] = _ch
            _total += _ch
        except Exception:
            _changes[u"replace"] = 0
        _changes[u"total"] = _total
        return _changes

    def ph_lists_apply(_data):
        """Apply checked lists right now. Returns {'applied': bool}."""
        _res = {u"applied": False}
        try:
            if store.PH_set_lists(_data, _data.get(u"version", 0)):
                try:
                    store._ph_purge_clothes()
                except Exception:
                    pass
                try:
                    store._ph_purge_reactions()
                except Exception:
                    pass
                _ph_save_cache(_data)
                try:
                    _ph_cache_version[0] = _ph_ver_num(_data.get(u"version", 0))
                except Exception:
                    pass
                _res[u"applied"] = True
        except Exception:
            pass
        return _res

    def ph_lists_reason():
        """Short reason the last manual check was rejected (empty if fine)."""
        return _ph_manual_reason[0]

    _ph_started = [False]

    def _ph_lists_interact():
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
