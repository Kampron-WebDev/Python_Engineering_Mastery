def _works(operation, value):
    """EAFP helper: True if operation(value) doesn't raise TypeError."""
    try:
        operation(value)
    except TypeError:
        return False
    return True


def inspect_value(value):
    return {
        "type": type(value).__name__,
        "callable": callable(value),
        "iterable": _works(iter, value),
        "sized": _works(len, value),
        "hashable": _works(hash, value),
    }


# Afterwards: a list can change, and a dict key's hash must never change while it's in the
# dict, so mutable containers are unhashable. A tuple is immutable, so it's hashable if
# everything INSIDE it is hashable. ([1],) contains a list, so it isn't.
