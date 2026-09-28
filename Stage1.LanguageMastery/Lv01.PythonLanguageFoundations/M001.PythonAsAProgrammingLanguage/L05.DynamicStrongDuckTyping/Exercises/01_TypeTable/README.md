# Exercise 01: Type Table

**Goal:** know exactly what `a + b` does across Python's types (strong typing, numeric promotion, and operators defined per type).

## Step 1: Predict (MY-NOTES.md)

For each pair, predict the **type name** of `a + b`, or the **exception**:

```text
(1, 2.0)    (True, 1)    ("a", "b")    ("a", 1)     ([1], [2])
([1], (2,)) (1, 1j)      (None, 1)     ((1,), (2,)) (b"a", "a")
```

## Step 2: Build it

`result_type(a, b)` returns `type(a + b).__name__`, or the exception's class name if `a + b` raises.

```python
result_type(1, 2.0)   # → 'float'
result_type("a", 1)   # → 'TypeError'
```

This time, use **no `eval`**: just do `a + b` inside a `try`.

## Step 3: Compare with JavaScript

In MY-NOTES.md, write what JavaScript gives for `"a" + 1`, `[1] + [2]` and `null + 1`. Why does Python refuse where JS guesses?

```powershell
python -m pytest
```
