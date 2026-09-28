# ⚠️ 2 bugs (both caused a production incident).


def get_debug(env):
    """True only for DEBUG in {1, true, yes, on} (any case)."""
    return bool(env.get("DEBUG"))


def get_port(env):
    """PORT as an int, default 8000."""
    return env.get("PORT", 8000)
