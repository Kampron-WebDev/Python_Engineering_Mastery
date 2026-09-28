# Run with:  python -m pytest
import os
import subprocess
import sys
from pathlib import Path

FOLDER = Path(__file__).parent / ("solution" if os.environ.get("CHECK_SOLUTION") else "")


def test_summarize(main):
    assert main.summarize([1, 2, 3]) == "count=3 total=6 mean=2.0"
    assert main.summarize([2.5, 2.5]) == "count=2 total=5.0 mean=2.5"


def test_importing_prints_nothing(load, capsys):
    load("main")
    captured = capsys.readouterr()
    assert captured.out == "" and captured.err == ""


def test_main_success(main, capsys):
    assert main.main(["1", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "count=3 total=6 mean=2.0"


def test_main_no_arguments(main, capsys):
    assert main.main([]) == 1
    assert "error: give me some numbers" in capsys.readouterr().err


def test_main_bad_argument(main, capsys):
    assert main.main(["1", "abc"]) == 1
    assert "error: not a number: abc" in capsys.readouterr().err


def test_runs_as_a_real_script():
    result = subprocess.run(
        [sys.executable, str(FOLDER / "main.py"), "1", "2", "3"], capture_output=True, text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "count=3 total=6 mean=2.0"

    failing = subprocess.run([sys.executable, str(FOLDER / "main.py")], capture_output=True, text=True)
    assert failing.returncode == 1
