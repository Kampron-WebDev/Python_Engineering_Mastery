# Run with:  python -m pytest
import os
import sys

import pytest

VENV = "C:\\proj\\.venv"
BASE = "C:\\Python313"


def test_healthy(main):
    assert main.diagnose(VENV, BASE, (3, 13, 7), "3.12", {}) == []


def test_not_in_venv(main):
    assert main.diagnose(BASE, BASE, (3, 13, 7), "3.12", {}) == ["NOT_IN_VENV"]


def test_too_old(main):
    assert main.diagnose(VENV, BASE, (3, 11, 9), "3.12", {}) == ["PYTHON_TOO_OLD"]
    assert main.diagnose(VENV, BASE, (3, 9, 0), "3.13", {}) == ["PYTHON_TOO_OLD"]
    assert main.diagnose(VENV, BASE, (3, 13, 0), "3.13", {}) == []


def test_version_compared_as_numbers(main):
    # "3.9" vs "3.10" is the classic string-comparison trap
    assert main.diagnose(VENV, BASE, (3, 10, 0), "3.9", {}) == []


def test_storefront_scenario(main):
    env = {"VIRTUAL_ENV": "C:\\venvs\\storefront", "PYTHONPATH": "C:\\libs"}
    assert main.diagnose(BASE, BASE, (3, 11, 9), "3.12", env) == [
        "NOT_IN_VENV",
        "PYTHONPATH_SET",
        "PYTHON_TOO_OLD",
        "VIRTUAL_ENV_MISMATCH",
    ]


def test_empty_values_are_not_problems(main):
    assert main.diagnose(VENV, BASE, (3, 13, 7), "3.12", {"VIRTUAL_ENV": "", "PYTHONPATH": ""}) == []


@pytest.mark.skipif(sys.platform != "win32", reason="Windows path rules")
def test_same_folder_spelled_differently(main):
    for spelling in ["c:\\proj\\.venv\\", "C:/proj/.venv", "C:\\PROJ\\.venv"]:
        assert main.diagnose(VENV, BASE, (3, 13, 7), "3.12", {"VIRTUAL_ENV": spelling}) == [], spelling


def test_the_real_course_setup_is_healthy(main):
    env = {k: v for k, v in os.environ.items() if k != "PYTHONPATH"}
    env["VIRTUAL_ENV"] = sys.prefix
    assert main.diagnose(sys.prefix, sys.base_prefix, tuple(sys.version_info), "3.13", env) == []
