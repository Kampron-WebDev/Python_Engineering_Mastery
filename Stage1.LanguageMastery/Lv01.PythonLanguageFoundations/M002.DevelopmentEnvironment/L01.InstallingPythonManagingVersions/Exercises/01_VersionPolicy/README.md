# Exercise 01: Version Policy

**Goal:** encode Python's release calendar as code, so a tool can answer "is this version still supported?".

For Python **3.8 and later**:

- release year = **2011 + minor** (3.13 → 2024)
- end of life = **October, 5 years after release** (3.13 → `"2029-10"`)

## Your task

| Function | Returns | Example |
|---|---|---|
| `release_year(version)` | int | `release_year("3.13")` → `2024` |
| `end_of_life(version)` | `"YYYY-10"` | `end_of_life("3.9")` → `"2025-10"` |
| `is_supported(version, today)` | bool | `is_supported("3.9", "2026-09")` → `False` |

- `version` is `"3.<minor>"`. Anything else (like `"2.7"`, `"3.7"`, `"banana"`) → `ValueError`.
- `today` is `"YYYY-MM"`. A version is supported **up to and including** its EOL month.

```python
is_supported("3.10", "2026-10")   # → True   (last month!)
is_supported("3.10", "2026-11")   # → False
```

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint</summary>

`"3.13".split(".")` → `["3", "13"]`. And `"YYYY-MM"` strings with zero-padded months compare correctly as strings, because every part has the same width. (Versions don't: that's the next exercise!)

</details>
