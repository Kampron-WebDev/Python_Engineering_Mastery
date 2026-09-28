# ⚠️ 2 bugs.
import tomllib


def project_info(path):
    """(name, requires_python) from a pyproject.toml file."""
    with open(path, encoding="utf-8") as f:
        data = tomllib.load(f)
    project = data["project"]
    return project["name"], project["requires_python"]
