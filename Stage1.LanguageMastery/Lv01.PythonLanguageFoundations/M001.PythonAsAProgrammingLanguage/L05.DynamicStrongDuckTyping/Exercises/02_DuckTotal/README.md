# Exercise 02: Duck Total

**Goal:** write a function that works with **anything that has a length**, EAFP style, without a single `isinstance` check.

## Your task

`total_length(things)` goes through `things` (any iterable) and:

- adds up `len(item)` for every item that **has** a length,
- counts the items that **don't** (for which `len()` raises `TypeError`),
- returns a tuple `(total, skipped)`.

```python
total_length(["abc", [1, 2], {"k": 1}, 42, None])   # → (6, 2)
total_length(x for x in ["hi", "there"])            # → (7, 0)
total_length([])                                    # → (0, 0)
```

🚫 Don't use `isinstance`, `type()` or `hasattr`: **ask forgiveness**, not permission.

```powershell
python -m pytest
```

**Think (MY-NOTES.md):** a class you write yourself will work here if it defines one special method. Which one? (Module 025 is all about these.)
