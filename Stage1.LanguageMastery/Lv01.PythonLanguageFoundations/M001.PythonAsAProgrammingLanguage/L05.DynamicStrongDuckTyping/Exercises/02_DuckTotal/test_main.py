# Run with:  python -m pytest
from pathlib import Path


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


def test_mixed_things(main):
    assert main.total_length(["abc", [1, 2], {"k": 1}, 42, None]) == (6, 2)


def test_any_iterable(main):
    assert main.total_length(x for x in ["hi", "there"]) == (7, 0)
    assert main.total_length(("a", "bb")) == (3, 0)


def test_your_own_duck(main):
    assert main.total_length([Playlist(["a", "b", "c"]), 3.14]) == (3, 1)


def test_empty(main):
    assert main.total_length([]) == (0, 0)


def test_no_permission_asking(main):
    code = Path(main.__file__).read_text(encoding="utf-8")
    code = "\n".join(line.split("#")[0] for line in code.splitlines())
    for banned in ("isinstance", "type(", "hasattr"):
        assert banned not in code, f"don't use {banned}: ask forgiveness, not permission"
