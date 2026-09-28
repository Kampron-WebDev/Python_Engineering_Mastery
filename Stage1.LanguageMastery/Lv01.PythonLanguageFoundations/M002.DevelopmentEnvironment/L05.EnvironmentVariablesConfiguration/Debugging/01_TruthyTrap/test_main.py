# Run with:  python -m pytest
import pytest


@pytest.mark.parametrize(("value", "expected"), [("false", False), ("0", False), ("no", False), ("true", True), ("ON", True), ("1", True)])
def test_get_debug(main, value, expected):
    assert main.get_debug({"DEBUG": value}) is expected


def test_get_debug_missing(main):
    assert main.get_debug({}) is False


def test_get_port_is_always_an_int(main):
    assert main.get_port({"PORT": "8080"}) == 8080
    assert isinstance(main.get_port({"PORT": "8080"}), int)
    assert main.get_port({}) == 8000
