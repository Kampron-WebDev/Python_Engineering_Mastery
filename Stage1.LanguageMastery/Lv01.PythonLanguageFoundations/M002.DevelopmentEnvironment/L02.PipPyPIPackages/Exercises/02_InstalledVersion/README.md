# Exercise 02: Installed Version

**Goal:** ask Python itself what's installed, the programmatic version of `pip show`.

## Your task

| Function | Behaviour |
|---|---|
| `installed_version(name)` | The installed version string of distribution `name`, or `None` if it isn't installed |
| `report(names)` | A dict `name → version or None` for every name in the list |
| `missing(names)` | A sorted list of the names that are **not** installed |

```python
installed_version("pytest")          # → "9.1.1" (or whatever version the course venv has)
installed_version("no-such-package") # → None
missing(["pytest", "nope", "also-nope"])  # → ["also-nope", "nope"]
```

## Useful tools

`from importlib import metadata`, then `metadata.version("pytest")`. It raises `metadata.PackageNotFoundError` for packages that aren't installed. **Catch that specific exception**, not every exception.

## Check your work

```powershell
python -m pytest
```

**Think (MY-NOTES.md):** run this exercise with the `storefront` Python instead of the course's. Would `installed_version("pytest")` give the same answer? Why?
