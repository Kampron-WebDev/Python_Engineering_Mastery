import re
import tomllib


def _normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def locked_versions(lock_text):
    packages = tomllib.loads(lock_text).get("package", [])
    return {_normalize(p["name"]): p["version"] for p in packages}


def missing_from_lock(declared, lock_text):
    locked = locked_versions(lock_text)
    return sorted({_normalize(name) for name in declared} - locked.keys())


# Think-about-it: no. starlette is a TRANSITIVE dependency (fastapi needs it). The lock
# records the whole tree; pyproject.toml only lists what YOU asked for directly.
