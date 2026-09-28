# ⚠️ 2 bugs: both fight duck typing.


def average_length(words):
    """Average length of the words in ANY iterable of strings; 0.0 when there are none."""
    if type(words) != list:
        raise TypeError("words must be a list")

    total = 0
    for word in words:
        total += len(word)

    count = len(words)
    return total / count if count else 0.0
