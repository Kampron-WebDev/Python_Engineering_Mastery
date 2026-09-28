# Run with:  python -m pytest
import pytest


def test_list(main):
    assert main.average_length(["hi", "hello"]) == 3.5


def test_tuple_and_set(main):
    assert main.average_length(("a", "bb", "ccc")) == 2.0
    assert main.average_length({"abcd"}) == 4.0


def test_generator(main):
    assert main.average_length(w for w in ["ab", "cdef"]) == 3.0


def test_empty(main):
    assert main.average_length([]) == 0.0
    assert main.average_length(iter([])) == 0.0


def test_non_iterable_still_fails_clearly(main):
    with pytest.raises(TypeError):
        main.average_length(42)
