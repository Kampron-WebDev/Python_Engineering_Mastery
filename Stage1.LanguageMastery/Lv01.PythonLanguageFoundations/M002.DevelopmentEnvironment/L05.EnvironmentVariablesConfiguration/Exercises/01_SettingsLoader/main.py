class ConfigError(Exception):
    """Raised when configuration is missing or invalid. The message lists every problem."""


def load_settings(env):
    """Convert and validate settings from a str → str mapping. See README.md."""
    # TODO: collect ALL problems, then raise ConfigError once if there are any
    pass
