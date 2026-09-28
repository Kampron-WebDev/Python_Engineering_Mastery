# Run with:  python -m pytest


def test_adds_every_line(main):
    items = [{"price": 250, "quantity": 2}, {"price": 100, "quantity": 1}]
    assert main.receipt_total(items) == 600


def test_empty_receipt(main):
    assert main.receipt_total([]) == 0
