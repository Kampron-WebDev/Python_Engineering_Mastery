# Run with:  python -m pytest
import pytest


def test_minimal_config_uses_defaults(main):
    assert main.load_settings({"DATABASE_URL": "postgresql://db"}) == {
        "app_name": "app",
        "port": 8000,
        "debug": False,
        "database_url": "postgresql://db",
    }


def test_everything_set(main):
    env = {"APP_NAME": "quiz", "PORT": "8080", "DEBUG": " Yes ", "DATABASE_URL": "postgresql://db"}
    assert main.load_settings(env) == {
        "app_name": "quiz",
        "port": 8080,
        "debug": True,
        "database_url": "postgresql://db",
    }


@pytest.mark.parametrize(("word", "expected"), [("1", True), ("TRUE", True), ("on", True), ("0", False), ("false", False), ("Off", False), ("", False)])
def test_debug_words(main, word, expected):
    assert main.load_settings({"DATABASE_URL": "x", "DEBUG": word})["debug"] is expected


def test_all_problems_reported_at_once(main):
    with pytest.raises(main.ConfigError) as info:
        main.load_settings({"PORT": "eighty", "DEBUG": "maybe"})
    message = str(info.value)
    assert "DATABASE_URL" in message
    assert "PORT" in message and "eighty" in message
    assert "DEBUG" in message and "maybe" in message


@pytest.mark.parametrize("port", ["0", "70000", "-5", "80.5"])
def test_port_range(main, port):
    with pytest.raises(main.ConfigError, match="PORT"):
        main.load_settings({"DATABASE_URL": "x", "PORT": port})


def test_config_error_is_an_exception(main):
    assert issubclass(main.ConfigError, Exception)
