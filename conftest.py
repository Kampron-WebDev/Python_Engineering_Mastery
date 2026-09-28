"""Shared test helpers for the whole course (pytest finds this file automatically).

Every exercise test can ask for:

    main   → the exercise's main.py, already imported
    load   → a function: load("money") imports money.py from the exercise folder

When the environment variable CHECK_SOLUTION=1 is set (tools/check-exercises.ps1 does
this), the same tests run against solution/main.py instead, so the course can prove
every model answer passes.
"""

import importlib
import os
import sys
from pathlib import Path

import pytest


def _code_folder(test_file: Path) -> Path:
    folder = test_file.parent
    return folder / "solution" if os.environ.get("CHECK_SOLUTION") else folder


@pytest.fixture
def load(request):
    folder = _code_folder(Path(request.path))

    def _load(name: str = "main"):
        # Forget same-named modules from other exercises, then import fresh from this folder.
        for py in folder.glob("*.py"):
            sys.modules.pop(py.stem, None)
        sys.path.insert(0, str(folder))
        try:
            return importlib.import_module(name)
        finally:
            sys.path.remove(str(folder))

    return _load


@pytest.fixture
def main(load):
    return load("main")
