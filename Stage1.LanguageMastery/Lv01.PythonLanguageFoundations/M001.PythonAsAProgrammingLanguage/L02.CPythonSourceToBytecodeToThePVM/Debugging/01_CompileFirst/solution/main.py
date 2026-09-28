def receipt_total(items):
    total = 0
    for item in items:  # Bug 1 (COMPILE time): the colon was missing, so nothing in the file could run
        line = item["price"] * item["quantity"]
        # Bug 2 (RUN time): `totl` was a typo, so NameError: name 'totl' is not defined.
        # It only appears when the loop body runs; an empty receipt hid it!
        total = total + line
    return total
