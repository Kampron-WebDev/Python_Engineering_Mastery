# Debugging 01: TOML Troubles

`project_info(path)` reads a `pyproject.toml` file and returns `(name, requires_python)`:

```python
project_info("pyproject.toml")   # → ("quiz-api", ">=3.12")
```

It crashes. There are **2 bugs**, the two mistakes almost everyone makes the first time with `tomllib`.

## Your task

1. `python -m pytest` and read the first error carefully: the message tells you exactly what to do.
2. Fix it; a second error appears. Fix that too.
3. In MY-NOTES.md: why does `tomllib` insist on binary mode? Why doesn't Python turn `requires-python` into `requires_python` for you?
