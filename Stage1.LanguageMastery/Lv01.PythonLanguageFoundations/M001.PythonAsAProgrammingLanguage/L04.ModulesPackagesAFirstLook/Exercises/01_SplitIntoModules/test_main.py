# Run with:  python -m pytest
# `load("money")` imports money.py from this folder (see the course's conftest.py).


def test_format_money(load):
    money = load("money")
    assert money.format_money(1234) == "$12.34"
    assert money.format_money(5) == "$0.05"
    assert money.format_money(0) == "$0.00"
    assert money.format_money(-500) == "-$5.00"


def test_new_cart_is_new_each_time(load):
    cart = load("cart")
    assert cart.new_cart() == {"items": []}
    assert cart.new_cart() is not cart.new_cart()


def test_add_item_does_not_modify(load):
    cart = load("cart")
    empty = cart.new_cart()
    pen = {"name": "Pen", "price": 125, "quantity": 4}
    assert cart.add_item(empty, pen) == {"items": [pen]}
    assert empty == {"items": []}, "the original cart was modified!"


def test_cart_total(load):
    cart = load("cart")
    assert cart.cart_total({"items": [{"price": 125, "quantity": 4}, {"price": 999, "quantity": 1}]}) == 1499
    assert cart.cart_total({"items": []}) == 0


def test_checkout_end_to_end(main):
    items = [{"name": "Pen", "price": 125, "quantity": 4}, {"name": "Book", "price": 999, "quantity": 1}]
    assert main.checkout(items) == "$14.99"
    assert main.checkout([]) == "$0.00"
