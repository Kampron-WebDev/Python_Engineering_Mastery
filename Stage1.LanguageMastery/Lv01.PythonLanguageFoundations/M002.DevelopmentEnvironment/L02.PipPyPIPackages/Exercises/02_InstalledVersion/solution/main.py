from importlib import metadata


def installed_version(name):
    try:
        return metadata.version(name)
    except metadata.PackageNotFoundError:  # catch ONLY the error we expect
        return None


def report(names):
    return {name: installed_version(name) for name in names}


def missing(names):
    return sorted(name for name in names if installed_version(name) is None)


# Think-about-it: each interpreter/venv has its own site-packages. The storefront environment
# may not have pytest at all, or may have a different version. "Installed" always means
# "installed for THIS Python".
