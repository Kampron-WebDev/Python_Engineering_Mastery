# Read the course's real pyproject.toml.   Run me:  python read_course_pyproject.py
import tomllib
from pathlib import Path

course_root = Path(__file__).resolve().parents[5]
path = course_root / "pyproject.toml"

with open(path, "rb") as f:  # binary mode: tomllib decodes the UTF-8 itself
    data = tomllib.load(f)

print("File            :", path)
print("Project name    :", data["project"]["name"])
print("Requires Python :", data["project"]["requires-python"])
print("Dependencies    :", data["project"]["dependencies"] or "(none)")
print("Dev group       :", data["dependency-groups"]["dev"])
print("Tools configured:", list(data["tool"]))
print("pytest options  :", data["tool"]["pytest"]["ini_options"]["addopts"])
