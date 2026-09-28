# ⚠️ 2 bugs. pricing.py is correct; statistics.py is someone's leftover experiment.
import statistics

from pricing import TAX_RATE, add_tax


def average_price(prices):
    """Mean price, using the standard library's statistics.mean."""
    return statistics.mean(prices)


def set_tax_rate(rate):
    """Change the tax rate used by pricing.add_tax."""
    global TAX_RATE
    TAX_RATE = rate


def price_with_tax(amount):
    return add_tax(amount)
