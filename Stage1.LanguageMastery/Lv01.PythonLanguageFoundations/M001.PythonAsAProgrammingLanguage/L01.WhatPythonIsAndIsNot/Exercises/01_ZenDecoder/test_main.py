# Run with:  python -m pytest
import contextlib
import io
import string
from pathlib import Path

with contextlib.redirect_stdout(io.StringIO()):
    import this


def test_rot13_basics(main):
    assert main.rot13("Hello") == "Uryyb"
    assert main.rot13("Uryyb") == "Hello"
    assert main.rot13("abcxyz") == "nopklm"
    assert main.rot13("Hi, 42!") == "Uv, 42!"
    assert main.rot13("") == ""


def test_rot13_twice_is_the_original(main):
    text = string.ascii_letters + string.digits + " .,!?"
    assert main.rot13(main.rot13(text)) == text


def test_rot13_matches_pythons_own_table(main):
    expected = "".join(this.d.get(c, c) for c in this.s)
    assert main.rot13(this.s) == expected


def test_zen_lines(main):
    lines = main.zen_lines()
    assert len(lines) == 19
    assert lines[0] == "Beautiful is better than ugly."
    assert lines[-1] == "Namespaces are one honking great idea -- let's do more of those!"
    assert all(line.strip() for line in lines)


def test_no_shortcuts(main):
    code = Path(main.__file__).read_text(encoding="utf-8")
    code = "\n".join(line.split("#")[0] for line in code.splitlines())  # ignore comments
    assert "codecs" not in code and "this.d" not in code
