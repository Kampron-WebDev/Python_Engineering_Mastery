# Run with:  python -m pytest


class Weird:
    """An object whose == claims to equal everything."""

    def __eq__(self, other):
        return True

    __hash__ = object.__hash__


def test_valid_ages(main):
    assert main.validate_age(30) is True
    assert main.validate_age(0) is True
    assert main.validate_age(150) is True


def test_invalid_ages(main):
    assert main.validate_age(200) is False
    assert main.validate_age(-1) is False
    assert main.validate_age(30.5) is False
    assert main.validate_age("30") is False


def test_booleans_are_not_ages(main):
    assert main.validate_age(True) is False
    assert main.validate_age(False) is False


def test_is_missing(main):
    assert main.is_missing(None) is True
    assert main.is_missing(0) is False
    assert main.is_missing("") is False


def test_is_missing_cannot_be_fooled(main):
    assert main.is_missing(Weird()) is False
