# Exercise 01: Timing Lab

**Goal:** settle "which is faster?" with **measurements**, not opinions, and build the tool to do it.

## Your task

### `time_per_call(func, number=1000)`

Return the **average seconds per call** of `func()` over `number` calls, using `timeit.timeit`.

### `fastest(candidates, number=1000)`

`candidates` is a dict `name → zero-argument function`. Return the **name** of the fastest one.

### `build_with_plus(n)` and `build_with_join(n)`

Two ways to build the string `"0,1,2,…,n-1"`:

- `build_with_plus`: start with `""` and use `+=` in a loop.
- `build_with_join`: `",".join(...)` over the numbers converted to strings.

Both must return **exactly** the same text.

```python
build_with_plus(4)   # → "0,1,2,3"
build_with_join(4)   # → "0,1,2,3"
fastest({"plus": lambda: build_with_plus(5000), "join": lambda: build_with_join(5000)}, number=50)
# → probably "join", but MEASURE it!
```

## Check your work

```powershell
python -m pytest
```

Afterwards, run in this folder:

```powershell
python -c "import main; print(main.fastest({'plus': lambda: main.build_with_plus(5000), 'join': lambda: main.build_with_join(5000)}, 50))"
```

In MY-NOTES.md: record the times you measured. Which won, by how much, and *why* (hint: strings are immutable)?

<details><summary>Hint</summary>

`timeit.timeit(func, number=number) / number`. `min(candidates, key=...)` finds the name with the smallest measured time.

</details>
