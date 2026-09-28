TRUE_WORDS = {"1", "true", "yes", "on"}


def get_debug(env):
    # Bug 1: environment values are strings, and ANY non-empty string is truthy,
    # so bool("false") is True. Parse the word explicitly.
    return env.get("DEBUG", "").strip().lower() in TRUE_WORDS


def get_port(env):
    # Bug 2: the default was an int (8000) but a SET value is a str ("8080"), so the return
    # type depended on the environment. Always convert: one type, every time.
    return int(env.get("PORT", "8000"))
