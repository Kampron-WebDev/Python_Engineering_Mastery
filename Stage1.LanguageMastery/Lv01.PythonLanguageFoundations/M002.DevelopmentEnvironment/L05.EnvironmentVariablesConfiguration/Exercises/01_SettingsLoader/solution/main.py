class ConfigError(Exception):
    """Raised when configuration is missing or invalid. The message lists every problem."""


TRUE_WORDS = {"1", "true", "yes", "on"}
FALSE_WORDS = {"0", "false", "no", "off", ""}


def load_settings(env):
    errors = []

    database_url = env.get("DATABASE_URL")
    if not database_url:
        errors.append("DATABASE_URL is required")

    raw_port = env.get("PORT", "8000")
    port = None
    if raw_port.strip().isdigit() and 1 <= int(raw_port) <= 65535:
        port = int(raw_port)
    else:
        errors.append(f"PORT must be a whole number from 1 to 65535, got {raw_port!r}")

    raw_debug = env.get("DEBUG", "")
    word = raw_debug.strip().lower()
    debug = word in TRUE_WORDS
    if word not in TRUE_WORDS | FALSE_WORDS:
        errors.append(f"DEBUG must be a boolean word, got {raw_debug!r}")

    if errors:
        raise ConfigError("\n".join(errors))  # fail fast, but report EVERYTHING at once

    return {
        "app_name": env.get("APP_NAME", "app"),
        "port": port,
        "debug": debug,
        "database_url": database_url,
    }
