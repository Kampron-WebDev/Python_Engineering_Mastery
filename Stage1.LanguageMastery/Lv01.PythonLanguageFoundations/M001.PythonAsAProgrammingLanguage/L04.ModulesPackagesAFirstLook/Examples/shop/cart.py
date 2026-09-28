"""cart.py: depends on money.py."""

from money import to_cents


def line_total(item):
    return to_cents(item["price"]) * item["quantity"]


def cart_total(items):
    return sum(line_total(item) for item in items)
