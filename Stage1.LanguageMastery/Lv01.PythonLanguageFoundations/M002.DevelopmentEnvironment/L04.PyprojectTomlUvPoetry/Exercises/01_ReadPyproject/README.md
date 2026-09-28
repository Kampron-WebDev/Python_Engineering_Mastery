# Exercise 01: Read pyproject

**Goal:** extract the important facts from a `pyproject.toml`, like a dependency-audit tool would.

## Your task

`summarize(toml_text)` parses the TOML **text** and returns:

```python
{
    "name": "quiz-api",
    "version": "0.3.0",
    "requires_python": ">=3.12",
    "dependencies": ["fastapi", "sqlalchemy"],     # just the NAMES, normalised, sorted
    "dev": ["pytest", "ruff"],                     # names from [dependency-groups].dev, sorted ([] if none)
}
```

To get a name from a dependency string like `"FastAPI[standard]>=0.115 ; python_version >= '3.12'"`, cut it at the **first** character that's one of `[<>=!~; ` (space), then normalise it (lowercase, runs of `-_.` → `-`).

## Useful tools

- `tomllib.loads(text)` parses TOML from a **string** (`load` is for binary files).
- `.get(key, default)` for optional sections: a project might have no `[dependency-groups]`.

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint: cutting a name</summary>

```python
for i, ch in enumerate(spec):
    if ch in "[<>=!~; ":
        return spec[:i]
return spec
```

</details>
