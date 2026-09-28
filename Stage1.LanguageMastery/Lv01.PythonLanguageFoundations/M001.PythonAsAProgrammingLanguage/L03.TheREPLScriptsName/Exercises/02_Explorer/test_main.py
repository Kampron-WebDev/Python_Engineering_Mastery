# Run with:  python -m pytest


class Robot:
    model = "R2"

    def __init__(self):
        self.battery = 100
        self._secret = "hidden"

    def beep(self):
        return "beep"


def test_public_names_of_a_list(main):
    assert main.public_names([]) == [
        "append", "clear", "copy", "count", "extend", "index", "insert", "pop", "remove", "reverse", "sort",
    ]


def test_public_names_hide_underscores(main):
    assert main.public_names(Robot()) == ["battery", "beep", "model"]


def test_describe(main):
    assert main.describe([]) == "list with 11 public attributes"
    assert main.describe(Robot()) == "Robot with 3 public attributes"


def test_functions_are_objects_too(main):
    assert main.describe(main.describe).startswith("function with ")
