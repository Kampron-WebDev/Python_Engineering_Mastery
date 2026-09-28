# Run with:  python -m pytest
from importlib import metadata

PYTEST = metadata.version("pytest")  # the tests themselves run on pytest, so it's installed


def test_installed(main):
    assert main.installed_version("pytest") == PYTEST


def test_not_installed(main):
    assert main.installed_version("definitely-not-a-real-package-xyz") is None


def test_report(main):
    assert main.report(["pytest", "nope-xyz"]) == {"pytest": PYTEST, "nope-xyz": None}


def test_missing(main):
    assert main.missing(["pytest", "nope-b", "nope-a"]) == ["nope-a", "nope-b"]
    assert main.missing([]) == []
