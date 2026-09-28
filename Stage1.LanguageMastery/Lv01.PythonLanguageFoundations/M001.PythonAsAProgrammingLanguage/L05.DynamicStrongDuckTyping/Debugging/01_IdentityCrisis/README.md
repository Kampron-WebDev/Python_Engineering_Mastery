# Debugging 01: Identity Crisis

A sign-up form validates two fields:

```python
validate_age(30)      # → True
validate_age(True)    # → False   (a checkbox value is NOT an age!)
validate_age(200)     # → False
is_missing(None)      # → True
is_missing(Weird())   # → False   (a real object, not None)
```

There are **2 bugs**, both about the difference between **what an object is** and **what it claims**.

## Your task

1. `python -m pytest`.
2. Fix both. In MY-NOTES.md, explain each: why did `True` pass as an age? Why did a real object look like `None`?

<details><summary>Hint 1</summary>

`isinstance(True, int)` is `True`. How can you say "an int, but not a bool"?

</details>

<details><summary>Hint 2</summary>

Look at the `Weird` class in `test_main.py`. What does its `__eq__` return? Which comparison operator can't be fooled by `__eq__`?

</details>
