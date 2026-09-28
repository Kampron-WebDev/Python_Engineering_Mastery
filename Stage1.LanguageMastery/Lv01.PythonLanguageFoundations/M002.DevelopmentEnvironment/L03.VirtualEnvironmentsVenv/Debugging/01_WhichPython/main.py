# ⚠️ 2 bugs.
import os


def which(command, path_value):
    """Full path of `command` in the FIRST folder of path_value that contains it, or None."""
    found = None
    for folder in path_value.split(":"):
        candidate = os.path.join(folder, command)
        if os.path.isfile(candidate):
            found = candidate
    return found
