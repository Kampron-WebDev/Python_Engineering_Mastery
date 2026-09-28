# Run with:  python -m pytest

LOCK = """
version = 1

[[package]]
name = "fastapi"
version = "0.115.6"

[[package]]
name = "Starlette"
version = "0.41.3"

[[package]]
name = "python_dateutil"
version = "2.9.0"
"""


def test_locked_versions(main):
    assert main.locked_versions(LOCK) == {
        "fastapi": "0.115.6",
        "starlette": "0.41.3",
        "python-dateutil": "2.9.0",
    }


def test_missing_from_lock(main):
    assert main.missing_from_lock(["FastAPI", "sqlalchemy"], LOCK) == ["sqlalchemy"]
    assert main.missing_from_lock(["Python.DateUtil"], LOCK) == []
    assert main.missing_from_lock(["zeta", "alpha", "fastapi"], LOCK) == ["alpha", "zeta"]


def test_empty_lock(main):
    assert main.locked_versions("version = 1\n") == {}
    assert main.missing_from_lock(["a"], "version = 1\n") == ["a"]
