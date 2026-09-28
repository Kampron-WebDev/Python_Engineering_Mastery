import os


def _same_folder(a, b):
    def clean(path):
        return os.path.normcase(os.path.normpath(path))

    return clean(a) == clean(b)


def _version_tuple(text):
    return tuple(int(part) for part in text.split("."))


def diagnose(prefix, base_prefix, version_info, minimum, env):
    problems = []

    if _same_folder(prefix, base_prefix):
        problems.append("NOT_IN_VENV")

    if tuple(version_info[:2]) < _version_tuple(minimum):
        problems.append("PYTHON_TOO_OLD")

    active = env.get("VIRTUAL_ENV", "")
    if active and not _same_folder(active, prefix):
        problems.append("VIRTUAL_ENV_MISMATCH")

    if env.get("PYTHONPATH", ""):
        problems.append("PYTHONPATH_SET")

    return sorted(problems)
