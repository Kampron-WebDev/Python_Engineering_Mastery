# Exercise 01: Settings Loader

**Goal:** load configuration the professional way: convert, validate, and fail fast with **every** problem listed at once.

## Your task

`load_settings(env)` takes a mapping of strings (like `os.environ`; tests pass plain dicts) and returns a dict:

| Key | From variable | Rules |
|---|---|---|
| `"app_name"` | `APP_NAME` | Optional, default `"app"` |
| `"port"` | `PORT` | Optional, default `8000`. Must be a whole number from 1 to 65535 |
| `"debug"` | `DEBUG` | Optional, default `False`. True words: `1 true yes on`. False words: `0 false no off` and `""`. Any capitalisation, surrounding spaces ignored. Anything else is an error |
| `"database_url"` | `DATABASE_URL` | **Required** |

If **anything** is wrong, raise `ConfigError` (already defined in `main.py`) whose message lists **every** problem, one per line, like:

```text
DATABASE_URL is required
PORT must be a whole number from 1 to 65535, got 'eighty'
DEBUG must be a boolean word, got 'maybe'
```

The order of the lines doesn't matter, but **all** of them must be there.

```python
load_settings({"DATABASE_URL": "postgresql://db", "PORT": "8080", "DEBUG": "Yes"})
# → {"app_name": "app", "port": 8080, "debug": True, "database_url": "postgresql://db"}
```

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint</summary>

Collect problems in a list (`errors.append(...)`) instead of raising at the first one. At the end: `if errors: raise ConfigError("\n".join(errors))`.

</details>
