# Run with:  python -m pytest
import pytest


def test_release_year(main):
    assert main.release_year("3.8") == 2019
    assert main.release_year("3.13") == 2024
    assert main.release_year("3.14") == 2025


def test_end_of_life(main):
    assert main.end_of_life("3.9") == "2025-10"
    assert main.end_of_life("3.13") == "2029-10"


def test_is_supported(main):
    assert main.is_supported("3.13", "2026-09") is True
    assert main.is_supported("3.9", "2026-09") is False
    assert main.is_supported("3.10", "2026-10") is True
    assert main.is_supported("3.10", "2026-11") is False


@pytest.mark.parametrize("bad", ["2.7", "3.7", "banana", "3", "3.x", "4.0"])
def test_invalid_versions(main, bad):
    with pytest.raises(ValueError):
        main.release_year(bad)
