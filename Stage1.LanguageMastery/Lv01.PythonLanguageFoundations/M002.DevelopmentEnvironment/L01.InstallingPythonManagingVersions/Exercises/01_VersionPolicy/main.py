def release_year(version):
    """'3.13' → 2024. ValueError for anything that isn't '3.<minor>' with minor >= 8."""
    # TODO
    pass


def end_of_life(version):
    """'3.13' → '2029-10'"""
    # TODO
    pass


def is_supported(version, today):
    """True if today ('YYYY-MM') is on or before the version's EOL month."""
    # TODO
    pass
