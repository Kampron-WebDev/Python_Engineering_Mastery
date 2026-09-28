# Run with:  python -m pytest
import pytest


def test_parse_version(main):
    assert main.parse_version("3.13") == (3, 13, 0)
    assert main.parse_version("3.13.7") == (3, 13, 7)
    assert main.parse_version("3") == (3, 0, 0)


@pytest.mark.parametrize("bad", ["3.x", "", "1.2.3.4", "3..1", "v3.13"])
def test_invalid(main, bad):
    with pytest.raises(ValueError):
        main.parse_version(bad)


def test_compare_versions(main):
    assert main.compare_versions("3.9", "3.13") == -1
    assert main.compare_versions("3.13", "3.9") == 1
    assert main.compare_versions("3.13", "3.13.0") == 0
    assert main.compare_versions("3.13.10", "3.13.9") == 1


def test_newest(main):
    assert main.newest(["3.9", "3.13.1", "3.13"]) == "3.13.1"
    assert main.newest(["3.10", "3.9", "3.2"]) == "3.10"
