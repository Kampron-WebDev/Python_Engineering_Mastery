# Run with:  python -m pytest
import os
import subprocess
import sys
from pathlib import Path

FOLDER = Path(__file__).parent / ("solution" if os.environ.get("CHECK_SOLUTION") else "")


def test_import_is_silent(load, capsys):
    load("main")
    assert capsys.readouterr().out == ""


def test_countdown_returns_text(load, capsys):
    module = load("main")
    capsys.readouterr()  # ignore anything printed during import
    assert module.countdown(3) == "3... 2... 1... Liftoff!"
    assert module.countdown(1) == "1... Liftoff!"


def test_running_directly_still_launches():
    # PYTHONUTF8=1: on Windows, output sent to a pipe otherwise uses a legacy code page that can't encode 🚀
    result = subprocess.run(
        [sys.executable, str(FOLDER / "main.py")],
        capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONUTF8": "1"},
    )
    assert "Launch sequence starting" in result.stdout
    assert "10... 9..." in result.stdout and "Liftoff!" in result.stdout
