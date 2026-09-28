# Run with:  python -m pytest
import json


def test_top_words(main):
    assert main.top_words("the cat and the hat and the bat", 2) == [("the", 3), ("and", 2)]
    assert main.top_words("Go go GO stop", 1) == [("go", 3)]
    assert main.top_words("", 3) == []


def test_days_between(main):
    assert main.days_between("2026-01-01", "2026-03-01") == 59
    assert main.days_between("2024-02-28", "2024-03-01") == 2  # leap year!
    assert main.days_between("2026-01-10", "2026-01-01") == -9


def test_pretty_json(main):
    text = main.pretty_json({"b": 1, "a": [1, 2]})
    assert text == '{\n  "a": [\n    1,\n    2\n  ],\n  "b": 1\n}'
    assert json.loads(text) == {"a": [1, 2], "b": 1}
