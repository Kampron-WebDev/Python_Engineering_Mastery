def new_cart():
    return {"items": []}


def add_item(cart, item):
    # A new dict and a new list: the caller's cart is never touched.
    return {**cart, "items": [*cart["items"], item]}


def cart_total(cart):
    return sum(item["price"] * item["quantity"] for item in cart["items"])
