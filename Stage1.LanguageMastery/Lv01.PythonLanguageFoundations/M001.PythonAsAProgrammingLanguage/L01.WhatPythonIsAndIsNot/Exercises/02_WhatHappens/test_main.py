# Run with:  python -m pytest
# Write your predictions in MY-NOTES.md BEFORE running!
import pytest

CASES = [
    ("3 + 3.5", "float"),
    ("'3' + 3", "TypeError"),
    ("'3' * 3", "str"),
    ("True + 1", "int"),
    ("[1] + [2]", "list"),
    ("[1] + (2,)", "TypeError"),
    ("1 / 0", "ZeroDivisionError"),
    ("7 // 2", "int"),
    ("'5' == 5", "bool"),
    ("int('3') + 3", "int"),
    ("None + 1", "TypeError"),
    ("'ab' < 'b'", "bool"),
    ("int('three')", "ValueError"),
    ("undefined_name", "NameError"),
]


@pytest.mark.parametrize(("expression", "expected"), CASES)
def test_what_happens(main, expression, expected):
    assert main.what_happens(expression) == expected
