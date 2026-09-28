def _minor(version):
    parts = version.split(".")
    if len(parts) != 2 or parts[0] != "3" or not parts[1].isdigit() or int(parts[1]) < 8:
        raise ValueError(f"expected a Python version like '3.13' (3.8+), got {version!r}")
    return int(parts[1])


def release_year(version):
    return 2011 + _minor(version)


def end_of_life(version):
    return f"{release_year(version) + 5}-10"


def is_supported(version, today):
    # Same-width "YYYY-MM" strings compare correctly character by character.
    return today <= end_of_life(version)
