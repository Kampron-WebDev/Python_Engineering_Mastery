def average_length(words):
    # Bug 1: `type(words) != list` rejected tuples, sets and generators, which can all be
    # looped over. Duck typing: don't ask what it IS, just use what it CAN DO.
    # A non-iterable (like 42) still raises TypeError on its own, in the for loop.
    total = 0
    count = 0
    for word in words:
        total += len(word)
        count += 1  # Bug 2: generators have no len(), so count while looping
    return total / count if count else 0.0
