def public_names(obj):
    return sorted(name for name in dir(obj) if not name.startswith("_"))


def describe(obj):
    return f"{type(obj).__name__} with {len(public_names(obj))} public attributes"
