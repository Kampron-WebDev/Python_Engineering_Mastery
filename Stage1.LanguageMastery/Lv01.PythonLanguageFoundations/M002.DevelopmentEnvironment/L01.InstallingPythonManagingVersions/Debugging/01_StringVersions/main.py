# ⚠️ 2 bugs: versions treated as text.
import sys


def meets_minimum(version, minimum):
    """True if version ('3.13') is at least minimum ('3.11')."""
    return version >= minimum


def current_version():
    """The running interpreter as 'MAJOR.MINOR', e.g. '3.13'."""
    return sys.version[:3]
