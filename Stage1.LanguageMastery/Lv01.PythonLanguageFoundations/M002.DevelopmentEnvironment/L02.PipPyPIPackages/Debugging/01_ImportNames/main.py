# ⚠️ 2 bugs.

KNOWN = {
    "PyYAML": "yaml",
    "beautifulsoup4": "bs4",
    "Pillow": "PIL",
    "scikit-learn": "sklearn",
    "python-dateutil": "dateutil",
    "python-dotenv": "dotenv",
}


def import_name(distribution):
    """The name you `import` after `pip install <distribution>`."""
    if distribution in KNOWN:
        return KNOWN[distribution]
    return distribution
