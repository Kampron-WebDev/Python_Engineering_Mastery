# Exercise 02: Lock Check

**Goal:** catch the classic mistake "someone edited `pyproject.toml` but forgot to update the lockfile".

A (simplified) lockfile in the style of `uv.lock` lists every resolved package:

```toml
version = 1

[[package]]
name = "fastapi"
version = "0.115.6"

[[package]]
name = "starlette"
version = "0.41.3"
```

(`[[package]]` is TOML for "an array of tables": `tomllib` gives you `data["package"]` as a **list of dicts**.)

## Your task

| Function | Returns |
|---|---|
| `locked_versions(lock_text)` | dict: normalised name → version |
| `missing_from_lock(declared, lock_text)` | **sorted** list of declared names (normalise them!) that aren't in the lock |

```python
missing_from_lock(["FastAPI", "sqlalchemy"], LOCK)   # → ["sqlalchemy"]
```

Normalise names the usual way (lowercase; runs of `-_.` → `-`) on **both** sides.

## Check your work

```powershell
python -m pytest
```

**Think (MY-NOTES.md):** `starlette` is in the lock but wasn't declared. Is that a problem? (Direct vs transitive dependencies.)
