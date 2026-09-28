import re


def _normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()


# Bug 1: the table was keyed by ONE spelling, so "pyyaml" or "Scikit_Learn" missed.
# Normalise the keys once, and normalise every lookup the same way.
KNOWN = {
    _normalize(dist): module
    for dist, module in {
        "PyYAML": "yaml",
        "beautifulsoup4": "bs4",
        "Pillow": "PIL",
        "scikit-learn": "sklearn",
        "python-dateutil": "dateutil",
        "python-dotenv": "dotenv",
    }.items()
}


def import_name(distribution):
    key = _normalize(distribution)
    if key in KNOWN:
        return KNOWN[key]
    # Bug 2: "my-cool-lib" isn't a valid identifier (`import my-cool-lib` is a SyntaxError).
    # The convention: the import name uses underscores.
    return key.replace("-", "_")
