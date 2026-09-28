# Run with:  python -m pytest
import sys
from pathlib import Path


def test_in_virtualenv(main):
    assert main.in_virtualenv("C:\\proj\\.venv", "C:\\Python313") is True
    assert main.in_virtualenv("C:\\Python313", "C:\\Python313") is False


def test_this_process_runs_in_the_course_venv(main):
    assert main.in_virtualenv(sys.prefix, sys.base_prefix) is True


def test_read_pyvenv_cfg(main):
    text = "home = C:\\Python313\ninclude-system-site-packages = false\n\nversion = 3.13.7\n"
    assert main.read_pyvenv_cfg(text) == {
        "home": "C:\\Python313",
        "include-system-site-packages": "false",
        "version": "3.13.7",
    }


def test_values_may_contain_equals(main):
    assert main.read_pyvenv_cfg("command = python -m venv --prompt=x .venv") == {
        "command": "python -m venv --prompt=x .venv"
    }


def test_ignores_junk_lines(main):
    assert main.read_pyvenv_cfg("no equals here\n  \nkey=value") == {"key": "value"}


def test_venv_python(main):
    assert main.venv_python(Path("proj/.venv"), "win32") == Path("proj/.venv/Scripts/python.exe")
    assert main.venv_python(Path("proj/.venv"), "linux") == Path("proj/.venv/bin/python")


def test_reads_the_real_course_venv_config(main):
    cfg = Path(sys.prefix) / "pyvenv.cfg"
    data = main.read_pyvenv_cfg(cfg.read_text(encoding="utf-8"))
    assert "home" in data and "version" in data
    assert data["version"].startswith(f"{sys.version_info.major}.{sys.version_info.minor}")
