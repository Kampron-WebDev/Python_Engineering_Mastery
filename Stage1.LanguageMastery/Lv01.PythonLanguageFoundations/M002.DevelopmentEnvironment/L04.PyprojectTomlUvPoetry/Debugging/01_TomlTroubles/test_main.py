# Run with:  python -m pytest

PYPROJECT = """
[project]
name = "quiz-api"
version = "0.3.0"
requires-python = ">=3.12"
"""


def test_project_info(main, tmp_path):
    path = tmp_path / "pyproject.toml"
    path.write_text(PYPROJECT, encoding="utf-8")
    assert main.project_info(path) == ("quiz-api", ">=3.12")
