# ✅ This file is finished. Don't edit it: its imports are the specification for your modules.
from cart import add_item, cart_total, new_cart
from money import format_money


def checkout(items):
    cart = new_cart()
    for item in items:
        cart = add_item(cart, item)
    return format_money(cart_total(cart))
