# A tour of pdb.   Run me:  python pdb_tour.py
# At the (Pdb) prompt try, in order:
#   ll        (see the whole function)
#   n  n  n   (step over lines)
#   p total   (print a variable)
#   s         (on the `add_tax(...)` line: step INTO it)
#   w         (where am I? the call stack)
#   u         (go up to the caller), then  p prices
#   c         (continue to the end)


def add_tax(amount, rate=0.15):
    result = round(amount * (1 + rate), 2)
    return result


def checkout(prices):
    breakpoint()  # ← execution pauses here
    total = 0
    for price in prices:
        total += price
    return add_tax(total)


print("Total with tax:", checkout([10.0, 20.0, 5.5]))
