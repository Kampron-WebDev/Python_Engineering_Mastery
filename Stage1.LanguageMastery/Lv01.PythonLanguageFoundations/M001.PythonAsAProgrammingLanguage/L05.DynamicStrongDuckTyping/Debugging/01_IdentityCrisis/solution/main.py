def validate_age(age):
    # Bug 1: bool is a subclass of int, so isinstance(True, int) is True.
    # Exclude bools explicitly (or use `type(age) is int`).
    return isinstance(age, int) and not isinstance(age, bool) and 0 <= age <= 150


def is_missing(value):
    # Bug 2: `==` asks the OBJECT (its __eq__), which can claim anything.
    # `is` checks identity: there's exactly one None object, and nothing can fake being it.
    return value is None
