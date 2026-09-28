# Debugging 01: Too Strict Type Check

`average_length(words)` should return the average length of the words in **any iterable**: a list, a tuple, a set, even a generator.

```python
average_length(["hi", "hello"])            # → 3.5
average_length(("a", "bb", "ccc"))         # → 2.0
average_length(w for w in ["ab", "cdef"])  # → 3.0   (a generator!)
average_length([])                         # → 0.0
```

A developer coming from Java "made it safe" with a type check. Now it rejects perfectly good input. There are **2 bugs**, and both fight Python's **duck typing**: *"if it walks like a duck and quacks like a duck, it's a duck."* The function only needs something it can **loop over**.

## Your task

1. `python -m pytest`, then read which inputs fail and why.
2. Fix both bugs, so the function works for **any** iterable of strings.
3. In MY-NOTES.md: what does "duck typing" mean, and why is checking `type(x) == list` usually un-Pythonic?

<details><summary>Hint 1</summary>

Do you need the type check at all? What happens if someone passes a number? (`for w in 42` raises a `TypeError` by itself, with a clear message.)

</details>

<details><summary>Hint 2</summary>

A generator has no `len()`. Count the words **while** you loop instead.

</details>
