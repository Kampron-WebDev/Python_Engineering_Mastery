def find_duplicates(items):
    seen = set()
    duplicates = set()  # Bug 2: a list collected "a" twice for ["a", "a", "a"]; a set keeps each once
    for item in items:  # Bug 1: range(1, …) skipped the first item. Loop over the items directly
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    return sorted(duplicates)  # Bug 3: the result must be sorted
