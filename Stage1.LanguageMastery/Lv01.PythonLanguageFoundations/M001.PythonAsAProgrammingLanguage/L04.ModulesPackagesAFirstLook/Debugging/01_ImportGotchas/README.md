# Debugging 01: Import Gotchas

```python
average_price([10, 20, 30])   # → 20        (uses the standard library's statistics.mean)
price_with_tax(100)           # → 115.0     (15% tax)
set_tax_rate(0.2)
price_with_tax(100)           # → 120.0     (the new rate must take effect)
```

`pricing.py` is correct, so **don't change it**. There are **2 bugs**, one for each "consequence that bites" in the lesson (section 3).

## Your task

1. `python -m pytest` and read the errors carefully. `module 'statistics' has no attribute 'mean'`: which `statistics` got imported?
2. Fix both bugs. For the first, the fix is not in `main.py`'s code at all.
3. In MY-NOTES.md: explain *why* each happened, using the words **sys.path** and **binding**.

<details><summary>Hint 1</summary>

Look at the files in this folder. Try `python -c "import statistics; print(statistics.__file__)"` from this folder.

</details>

<details><summary>Hint 2</summary>

`set_tax_rate` changes *main's* `TAX_RATE`. Which module's `TAX_RATE` does `add_tax` read?

</details>
