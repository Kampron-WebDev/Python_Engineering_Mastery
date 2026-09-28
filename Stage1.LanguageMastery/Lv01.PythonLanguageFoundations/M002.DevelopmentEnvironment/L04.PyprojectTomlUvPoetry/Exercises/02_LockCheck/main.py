import re
import tomllib


def locked_versions(lock_text):
    """{normalised name: version} for every [[package]] in the lock."""
    # TODO
    pass


def missing_from_lock(declared, lock_text):
    """Sorted, normalised names from `declared` that the lock doesn't contain."""
    # TODO
    pass
