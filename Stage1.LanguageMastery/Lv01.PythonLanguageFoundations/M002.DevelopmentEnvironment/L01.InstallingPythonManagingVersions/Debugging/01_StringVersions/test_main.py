# Run with:  python -m pytest
import sys


def test_meets_minimum(main):
    assert main.meets_minimum("3.13", "3.11") is True
    assert main.meets_minimum("3.11", "3.11") is True
    assert main.meets_minimum("3.9", "3.11") is False
    assert main.meets_minimum("3.10", "3.9") is True


def test_current_version(main):
    assert main.current_version() == f"{sys.version_info.major}.{sys.version_info.minor}"
