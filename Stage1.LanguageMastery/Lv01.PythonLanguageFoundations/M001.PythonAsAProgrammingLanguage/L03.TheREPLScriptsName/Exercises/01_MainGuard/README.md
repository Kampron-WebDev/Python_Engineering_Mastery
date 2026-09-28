# Exercise 01: Main Guard

**Goal:** write one file that is both an importable **library** and a runnable **program**.

## Your task

### `summarize(numbers)` (pure logic)

Takes a list of numbers; returns the text `count=<n> total=<t> mean=<m>`, where `mean` has one decimal place.

```python
summarize([1, 2, 3])        # → "count=3 total=6 mean=2.0"
summarize([2.5, 2.5])       # → "count=2 total=5.0 mean=2.5"
```

### `main(argv)` (the glue)

`argv` is a list of strings (the command-line arguments, *without* the script name).

- Convert each argument to a `float` **if it has a decimal point**, otherwise to an `int`.
- Print `summarize(...)` of them, and **return `0`**.
- No arguments → print `error: give me some numbers` to **stderr** and return `1`.
- An argument that isn't a number → print `error: not a number: <arg>` to **stderr** and return `1`.

### The guard

At the bottom, add the `if __name__ == "__main__":` guard that calls `sys.exit(main(sys.argv[1:]))`.

Importing the file must print **nothing**. Running it must work:

```powershell
python main.py 1 2 3      # count=3 total=6 mean=2.0
python main.py            # error: give me some numbers   (exit code 1)
```

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint: printing to stderr</summary>

`print("error: …", file=sys.stderr)`

</details>

<details><summary>Hint: int or float?</summary>

`float(arg) if "." in arg else int(arg)`. Both raise `ValueError` for text like `"abc"`: catch it with `try` / `except ValueError`.

</details>
