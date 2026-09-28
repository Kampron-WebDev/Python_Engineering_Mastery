# Run with:  python -m pytest
import pytest


class Box:
    """A plain class: callable? no. iterable? no. hashable? yes (by identity)."""


class Deck:
    def __init__(self):
        self.cards = ["A", "K"]

    def __iter__(self):
        return iter(self.cards)

    def __len__(self):
        return len(self.cards)

    def __call__(self):
        return self.cards[0]


def gen():
    yield 1


CASES = [
    (42, {"type": "int", "callable": False, "iterable": False, "sized": False, "hashable": True}),
    ("hi", {"type": "str", "callable": False, "iterable": True, "sized": True, "hashable": True}),
    ([1, 2], {"type": "list", "callable": False, "iterable": True, "sized": True, "hashable": False}),
    ((1, 2), {"type": "tuple", "callable": False, "iterable": True, "sized": True, "hashable": True}),
    (([1],), {"type": "tuple", "callable": False, "iterable": True, "sized": True, "hashable": False}),
    ({"a": 1}, {"type": "dict", "callable": False, "iterable": True, "sized": True, "hashable": False}),
    (len, {"type": "builtin_function_or_method", "callable": True, "iterable": False, "sized": False, "hashable": True}),
    (None, {"type": "NoneType", "callable": False, "iterable": False, "sized": False, "hashable": True}),
]


@pytest.mark.parametrize(("value", "expected"), CASES)
def test_builtins(main, value, expected):
    assert main.inspect_value(value) == expected


def test_generator(main):
    assert main.inspect_value(gen()) == {
        "type": "generator", "callable": False, "iterable": True, "sized": False, "hashable": True,
    }


def test_classes_and_instances(main):
    assert main.inspect_value(Box()) == {
        "type": "Box", "callable": False, "iterable": False, "sized": False, "hashable": True,
    }
    assert main.inspect_value(Deck()) == {
        "type": "Deck", "callable": True, "iterable": True, "sized": True, "hashable": True,
    }
    assert main.inspect_value(Box)["callable"] is True  # classes are callable: that's how you make instances
