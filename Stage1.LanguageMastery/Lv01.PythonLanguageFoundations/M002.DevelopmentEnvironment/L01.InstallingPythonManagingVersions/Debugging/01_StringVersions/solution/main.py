import sys


def _as_tuple(version):
    return tuple(int(part) for part in version.split("."))


def meets_minimum(version, minimum):
    # Bug 1: string comparison goes character by character, and '9' > '1', so "3.9" >= "3.11".
    return _as_tuple(version) >= _as_tuple(minimum)


def current_version():
    # Bug 2: sys.version is display text like "3.13.7 (tags/…)"; [:3] gives "3.1" on 3.13!
    return f"{sys.version_info.major}.{sys.version_info.minor}"
