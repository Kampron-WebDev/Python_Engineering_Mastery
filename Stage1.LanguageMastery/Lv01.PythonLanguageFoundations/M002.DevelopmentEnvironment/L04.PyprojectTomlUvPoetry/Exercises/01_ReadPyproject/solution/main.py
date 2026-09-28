import re
import tomllib


def dependency_name(spec):
    name = spec
    for index, char in enumerate(spec):
        if char in "[<>=!~; ":
            name = spec[:index]
            break
    return re.sub(r"[-_.]+", "-", name).lower()


def summarize(toml_text):
    data = tomllib.loads(toml_text)
    project = data["project"]
    dev = data.get("dependency-groups", {}).get("dev", [])
    return {
        "name": project["name"],
        "version": project["version"],
        "requires_python": project["requires-python"],
        "dependencies": sorted(dependency_name(d) for d in project.get("dependencies", [])),
        "dev": sorted(dependency_name(d) for d in dev),
    }
