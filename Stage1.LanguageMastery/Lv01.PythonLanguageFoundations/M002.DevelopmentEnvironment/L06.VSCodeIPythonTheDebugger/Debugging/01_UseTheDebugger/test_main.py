# Run with:  python -m pytest


def test_typical(main):
    assert main.find_duplicates([3, 1, 3, 2, 1]) == [1, 3]


def test_many_repeats_listed_once(main):
    assert main.find_duplicates(["a", "a", "a"]) == ["a"]


def test_first_item_counts(main):
    assert main.find_duplicates([5, 5]) == [5]


def test_no_duplicates(main):
    assert main.find_duplicates([1, 2, 3]) == []
    assert main.find_duplicates([]) == []
