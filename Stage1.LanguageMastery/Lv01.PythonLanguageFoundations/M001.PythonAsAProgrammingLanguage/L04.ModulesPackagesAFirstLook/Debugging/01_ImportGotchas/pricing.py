# ✅ Correct. Don't change this file.
TAX_RATE = 0.15


def add_tax(amount):
    return round(amount * (1 + TAX_RATE), 2)
