def result_type(a, b):
    try:
        return type(a + b).__name__
    except Exception as err:
        return type(err).__name__


# JavaScript, for comparison: "a" + 1 → "a1", [1] + [2] → "12" (!), null + 1 → 1.
# Python refuses to guess: mixing unrelated types is almost always a bug.
