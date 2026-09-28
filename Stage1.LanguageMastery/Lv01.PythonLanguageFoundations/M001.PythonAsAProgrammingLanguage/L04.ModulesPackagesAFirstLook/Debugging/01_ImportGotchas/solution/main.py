# Bug 1: a local statistics.py SHADOWED the standard library (the script's folder is searched
# first). Fix: rename/delete the local file (the solution folder simply doesn't have it).
import statistics

# Bug 2: `from pricing import TAX_RATE` made a separate name in THIS module. Rebinding it never
# changed pricing.TAX_RATE, which is what add_tax reads. Fix: change the value ON the module.
import pricing


def average_price(prices):
    return statistics.mean(prices)


def set_tax_rate(rate):
    pricing.TAX_RATE = rate  # (even better long-term: pass the rate as a parameter)


def price_with_tax(amount):
    return pricing.add_tax(amount)
