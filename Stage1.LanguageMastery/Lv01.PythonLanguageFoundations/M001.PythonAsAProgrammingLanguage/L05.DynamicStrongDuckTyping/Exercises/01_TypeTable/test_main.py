# Run with:  python -m pytest   (predict first!)
import pytest

CASES = [
    ((1, 2.0), "float"),
    ((True, 1), "int"),
    (("a", "b"), "str"),
    (("a", 1), "TypeError"),
    (([1], [2]), "list"),
    (([1], (2,)), "TypeError"),
    ((1, 1j), "complex"),
    ((None, 1), "TypeError"),
    (((1,), (2,)), "tuple"),
    ((b"a", "a"), "TypeError"),
    ((True, True), "int"),
    ((1.5, True), "float"),
]


@pytest.mark.parametrize(("pair", "expected"), CASES)
def test_result_type(main, pair, expected):
    assert main.result_type(*pair) == expected
