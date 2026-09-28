import tomllib


def project_info(path):
    # Bug 1: TypeError: "File must be opened in binary mode". TOML is defined as UTF-8 BYTES,
    # and tomllib decodes them itself, so it won't accept an already-decoded text file.
    with open(path, "rb") as f:
        data = tomllib.load(f)
    project = data["project"]
    # Bug 2: KeyError: 'requires_python'. TOML keys are plain strings: the file says
    # requires-python (with a dash), and that's exactly the dict key. No automatic renaming.
    return project["name"], project["requires-python"]
