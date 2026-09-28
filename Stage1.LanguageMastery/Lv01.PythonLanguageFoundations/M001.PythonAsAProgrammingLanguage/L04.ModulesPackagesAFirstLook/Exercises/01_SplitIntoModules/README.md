# Exercise 01: Split into Modules

**Goal:** write two modules so that a finished `main.py` works *without changing it*.

```text
01_SplitIntoModules/
├── main.py    ← DONE. Don't edit it: its imports are your specification!
├── money.py   ← TODO
└── cart.py    ← TODO
```

`main.py` starts with:

```python
from cart import add_item, cart_total, new_cart
from money import format_money
```

## What each function does

### `money.py`

- `format_money(cents)` → `"$12.34"`. Negative amounts: `format_money(-500)` → `"-$5.00"`.

### `cart.py`

- `new_cart()` → a new, empty cart: `{"items": []}`. Each call returns a **new** dict.
- `add_item(cart, item)` → a **new** cart with `item` appended. It must **not** modify the cart it receives.
- `cart_total(cart)` → the sum of `item["price"] * item["quantity"]` (prices are already in cents).

Then `checkout` in `main.py` works:

```python
checkout([{"name": "Pen", "price": 125, "quantity": 4}, {"name": "Book", "price": 999, "quantity": 1}])
# → "$14.99"
```

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint: a new cart without changing the old one</summary>

```python
return {**cart, "items": [*cart["items"], item]}
```

`**` unpacks a dict's key/value pairs into a new dict; `*` unpacks a list's items into a new list. (Deep dive: Modules 009–010 and 059–060.)

</details>
