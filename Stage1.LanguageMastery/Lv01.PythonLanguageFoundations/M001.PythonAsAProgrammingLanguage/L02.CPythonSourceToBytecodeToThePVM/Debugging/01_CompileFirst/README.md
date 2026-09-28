# Debugging 01: Compile First

`receipt_total(items)` should add up `price * quantity` for every item (each item is a dict):

```python
receipt_total([{"price": 250, "quantity": 2}, {"price": 100, "quantity": 1}])  # → 600
receipt_total([])                                                           # → 0
```

When you run the tests, **nothing** from `main.py` runs at all. There are **2 bugs**, one from each phase:

1. a **compile-time** error (the whole file is rejected), and after fixing that…
2. a **run-time** error.

## Your task

1. `python -m pytest`, then read the error.
2. Run **`python -m py_compile main.py`**. It points at the exact line, like `node --check`. Fix it.
3. Run the tests again. A different error appears, from a different phase. Read the traceback **from the bottom up** and fix it.
4. In MY-NOTES.md: for each bug, which phase found it, and which tool pointed you to it?

<details><summary>Hint 1</summary>

Every `def`, `for`, `if`… line must end with a certain character.

</details>

<details><summary>Hint 2</summary>

A `NameError` means Python looked for a name and found nothing. Read the names letter by letter.

</details>
