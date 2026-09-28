# Debugging 01: Use the Debugger

`find_duplicates(items)` returns a **sorted** list of the items that appear **more than once**, each listed **once**:

```python
find_duplicates([3, 1, 3, 2, 1])   # → [1, 3]
find_duplicates(["a", "a", "a"])   # → ["a"]
find_duplicates([5, 5])            # → [5]
find_duplicates([1, 2, 3])         # → []
```

There are **3 bugs**.

## The rules for this one

Don't fix anything until you've written this in MY-NOTES.md for **each** bug:

```text
Bug #:
  Observation: (failing test, expected vs actual)
  Hypothesis:  "I think … because …"
  Experiment:  (breakpoint / pdb command you used, and what you saw)
  Fix:
```

## How to debug a test

- **VS Code:** set a breakpoint inside the loop in `main.py`, open `test_main.py`, **F5 → "Debug this exercise's tests"**.
- **Terminal:** add `breakpoint()` inside the loop and run `python -m pytest -s --timeout=0` (`-s` lets pdb talk to you; `--timeout=0` stops the test timeout interrupting your session).
