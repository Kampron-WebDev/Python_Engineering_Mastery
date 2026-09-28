# ⚠️ 2 bugs.


def validate_age(age):
    """True for whole-number ages 0..150. Booleans are NOT ages."""
    return isinstance(age, int) and 0 <= age <= 150


def is_missing(value):
    """True only when value is None."""
    return value == None  # noqa: E711
