def parse_version(text):
    parts = text.split(".")
    if not 1 <= len(parts) <= 3 or not all(part.isdigit() for part in parts):
        raise ValueError(f"not a version: {text!r}")
    numbers = [int(part) for part in parts]
    return tuple(numbers + [0] * (3 - len(numbers)))


def compare_versions(a, b):
    va, vb = parse_version(a), parse_version(b)
    return (va > vb) - (va < vb)  # True/False are 1/0, a classic trick


def newest(versions):
    return max(versions, key=parse_version)
