# Exercise 02: What Happens?

**Goal:** *feel* what "dynamically and strongly typed" means, by predicting and then checking.

## Step 1: Predict (MY-NOTES.md, before coding!)

For each expression, write the **type of the result**, or the **exception** it raises:

```text
3 + 3.5          '3' + 3          '3' * 3          True + 1
[1] + [2]        [1] + (2,)       1 / 0            7 // 2
'5' == 5         int('3') + 3     None + 1         'ab' < 'b'
```

## Step 2: Build the checker

Complete `what_happens(expression)`. It evaluates the expression string and returns:

- the **type name** of the result (e.g. `'float'`, `'str'`, `'bool'`), or
- the **name of the exception** it raised (e.g. `'TypeError'`, `'ZeroDivisionError'`).

```python
what_happens("3 + 3.5")    # → 'float'
what_happens("'3' + 3")    # → 'TypeError'
what_happens("1 / 0")      # → 'ZeroDivisionError'
```

Use the built-in `eval(expression)` inside a `try` / `except Exception as err:`.
`type(value).__name__` gives a type's name; `type(err).__name__` gives an exception's name.

⚠️ `eval` runs any code in a string. It's fine for a learning tool you control, but **never** use it on user input in real software.

## Step 3: Compare

Run the tests. Which predictions were wrong? Explain each surprise in MY-NOTES.md, and compare with what JavaScript would do.

```powershell
python -m pytest
```
