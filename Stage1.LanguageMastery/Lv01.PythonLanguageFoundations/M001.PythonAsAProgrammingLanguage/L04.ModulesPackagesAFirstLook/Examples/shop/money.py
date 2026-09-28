"""money.py: everything about money."""

_SYMBOL = "$"  # leading underscore = "private by convention" (Python doesn't enforce it)


def format_money(cents):
    return f"{_SYMBOL}{cents / 100:.2f}"


def to_cents(amount):
    return round(amount * 100)
