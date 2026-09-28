import os


def which(command, path_value):
    # Bug 1: PATH entries are separated by os.pathsep: ';' on Windows, ':' on Linux/macOS.
    # Splitting "C:\Python313;…" on ':' chops drive letters off ("C", "\Python313;…").
    for folder in path_value.split(os.pathsep):
        candidate = os.path.join(folder, command)
        if os.path.isfile(candidate):
            # Bug 2: the FIRST match wins (that's how shells search PATH), so return immediately.
            # The old code kept looping and returned the LAST match.
            return candidate
    return None
