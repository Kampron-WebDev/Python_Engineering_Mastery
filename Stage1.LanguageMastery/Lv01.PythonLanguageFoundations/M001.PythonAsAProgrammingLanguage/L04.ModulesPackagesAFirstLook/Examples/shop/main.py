# Run me:  python main.py
import money
from cart import cart_total

items = [{"name": "Notebook", "price": 3.5, "quantity": 2}, {"name": "Pen", "price": 1.25, "quantity": 4}]

print("Total:", money.format_money(cart_total(items)))
print("money is a", type(money).__name__, "object from", money.__file__)
print("Its public names:", [n for n in dir(money) if not n.startswith("_")])
