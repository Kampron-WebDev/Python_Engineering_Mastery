# Run with:  python -m pytest
# (The `main` fixture re-imports main.py AND pricing.py fresh for every test, so tax-rate
#  changes in one test can't leak into the next.)


def test_average_price_uses_the_real_statistics_module(main):
    assert main.average_price([10, 20, 30]) == 20


def test_default_tax(main):
    assert main.price_with_tax(100) == 115.0


def test_changing_the_tax_rate_really_changes_it(main):
    main.set_tax_rate(0.2)
    assert main.price_with_tax(100) == 120.0
