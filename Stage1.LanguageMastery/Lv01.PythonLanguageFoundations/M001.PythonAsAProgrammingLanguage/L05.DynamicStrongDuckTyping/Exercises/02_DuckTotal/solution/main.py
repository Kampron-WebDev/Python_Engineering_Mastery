def total_length(things):
    total = 0
    skipped = 0
    for item in things:
        try:
            total += len(item)
        except TypeError:
            skipped += 1
    return total, skipped


# Think-about-it: define __len__ on your class and len() works on it. Duck typing in action.
