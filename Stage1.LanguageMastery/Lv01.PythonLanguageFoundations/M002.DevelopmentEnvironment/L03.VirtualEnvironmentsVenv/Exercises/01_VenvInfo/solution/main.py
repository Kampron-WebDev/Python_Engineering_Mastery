from pathlib import Path


def in_virtualenv(prefix, base_prefix):
    return prefix != base_prefix


def read_pyvenv_cfg(text):
    config = {}
    for line in text.splitlines():
        key, sep, value = line.partition("=")  # split on the FIRST '=' only
        if sep and key.strip():
            config[key.strip()] = value.strip()
    return config


def venv_python(venv_dir, platform):
    venv_dir = Path(venv_dir)
    if platform == "win32":
        return venv_dir / "Scripts" / "python.exe"
    return venv_dir / "bin" / "python"
