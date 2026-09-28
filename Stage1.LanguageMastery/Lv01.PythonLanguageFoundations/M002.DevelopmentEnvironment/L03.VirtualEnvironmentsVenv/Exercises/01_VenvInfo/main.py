from pathlib import Path


def in_virtualenv(prefix, base_prefix):
    """True when running inside a virtual environment (the prefixes differ)."""
    # TODO
    pass


def read_pyvenv_cfg(text):
    """Parse 'key = value' lines into a dict (split on the FIRST '=')."""
    # TODO
    pass


def venv_python(venv_dir, platform):
    """Path to the venv's interpreter: Scripts/python.exe on win32, bin/python elsewhere."""
    # TODO
    pass
