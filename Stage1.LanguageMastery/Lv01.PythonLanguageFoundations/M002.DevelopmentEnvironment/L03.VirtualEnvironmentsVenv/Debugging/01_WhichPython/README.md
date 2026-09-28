# Debugging 01: Which Python?

`which(command, path_value)` should behave like `where.exe` / `which`: search the folders in a PATH string **in order** and return the full path of the **first** folder that contains the command, or `None`.

```python
which("python.exe", r"C:\venvs\storefront\Scripts;C:\Python313;C:\Windows")
# → "C:\venvs\storefront\Scripts\python.exe"   (if both folders contain python.exe, the FIRST wins)
```

The tests build real temporary folders with fake `python.exe` files. There are **2 bugs**, and one of them only shows up on Windows-style paths.

## Your task

1. `python -m pytest`.
2. Fix both. In MY-NOTES.md: what's the PATH separator on Windows vs Linux? Why does the search order matter so much (hint: `storefront`)?

<details><summary>Hint 1</summary>

`"C:\Python313;C:\Windows".split(":")`: what does that produce? `os.pathsep` is the right separator for the current OS.

</details>

<details><summary>Hint 2</summary>

Does the loop stop at the first match, or keep going and remember the last one?

</details>
