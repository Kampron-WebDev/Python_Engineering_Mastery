import re
import tomllib


def dependency_name(spec):
    """'FastAPI[standard]>=0.115' → 'fastapi' (cut at the first of '[<>=!~; ', then normalise)."""
    # TODO
    pass


def summarize(toml_text):
    """{'name', 'version', 'requires_python', 'dependencies', 'dev'}. See README.md."""
    # TODO
    pass
