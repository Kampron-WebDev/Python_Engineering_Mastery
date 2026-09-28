# Run with:  python -m pytest
from pathlib import Path

QUIZ_API = """
[project]
name = "quiz-api"
version = "0.3.0"
requires-python = ">=3.12"
dependencies = [
    "SQLAlchemy>=2.0",
    "FastAPI[standard]>=0.115 ; python_version >= '3.12'",
]

[dependency-groups]
dev = ["ruff", "pytest>=8"]
"""

MINIMAL = """
[project]
name = "tiny"
version = "1.0.0"
requires-python = ">=3.13"
dependencies = []
"""


def test_dependency_name(main):
    assert main.dependency_name("FastAPI[standard]>=0.115") == "fastapi"
    assert main.dependency_name("python_dateutil ~= 2.9") == "python-dateutil"
    assert main.dependency_name("ruff") == "ruff"


def test_summarize_full(main):
    assert main.summarize(QUIZ_API) == {
        "name": "quiz-api",
        "version": "0.3.0",
        "requires_python": ">=3.12",
        "dependencies": ["fastapi", "sqlalchemy"],
        "dev": ["pytest", "ruff"],
    }


def test_summarize_minimal(main):
    assert main.summarize(MINIMAL)["dev"] == []
    assert main.summarize(MINIMAL)["dependencies"] == []


def test_summarize_the_real_course_file(main):
    root = Path(__file__).resolve().parents[6]
    summary = main.summarize((root / "pyproject.toml").read_text(encoding="utf-8"))
    assert summary["name"] == "python-engineering-mastery"
    assert "pytest" in summary["dev"]
