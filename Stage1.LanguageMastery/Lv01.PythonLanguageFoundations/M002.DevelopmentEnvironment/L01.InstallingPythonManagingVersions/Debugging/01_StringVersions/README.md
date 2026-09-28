# Debugging 01: String Versions

A deployment script refuses to run on Python that's too old:

```python
meets_minimum("3.13", "3.11")   # → True
meets_minimum("3.9", "3.11")    # → False   (but the script says True!)
current_version()               # → "3.13" on Python 3.13
```

There are **2 bugs**. Both come from treating versions as **text**.

## Your task

1. `python -m pytest`.
2. Fix both. In MY-NOTES.md: why is `"3.9" >= "3.11"` True? What does `sys.version[:3]` give on Python 3.13, and why?

<details><summary>Hint</summary>

Convert versions to tuples of ints before comparing. For the current version, use `sys.version_info`, not the display string `sys.version`.

</details>
