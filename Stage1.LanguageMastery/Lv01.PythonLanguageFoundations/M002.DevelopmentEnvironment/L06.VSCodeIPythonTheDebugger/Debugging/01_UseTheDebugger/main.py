# ⚠️ 3 bugs. Hypothesis first, then the debugger, then the fix.


def find_duplicates(items):
    """Sorted list of items that appear more than once, each listed once."""
    seen = set()
    duplicates = []
    for i in range(1, len(items)):
        item = items[i]
        if item in seen:
            duplicates.append(item)
        seen.add(item)
    return duplicates
