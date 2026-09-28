# No-Hints Challenge: Python Doctor

Write `diagnose(prefix, base_prefix, version_info, minimum, env)`. It inspects a Python setup and returns a **sorted list of problem codes** (an empty list means healthy).

| Code | When |
|---|---|
| `"NOT_IN_VENV"` | `prefix` equals `base_prefix` |
| `"PYTHON_TOO_OLD"` | `version_info`'s (major, minor) is lower than `minimum` (a string like `"3.12"`) |
| `"VIRTUAL_ENV_MISMATCH"` | `env` has a non-empty `VIRTUAL_ENV` that is **not** the same folder as `prefix` (someone activated a *different* environment, like `storefront`) |
| `"PYTHONPATH_SET"` | `env` has a non-empty `PYTHONPATH` (it silently changes where imports come from) |

- `version_info` is a tuple like `(3, 13, 7)`.
- `env` is a dict (like `os.environ`).
- Compare folders **robustly**: `C:\Proj\.venv`, `c:\proj\.venv\` and `C:/proj/.venv` are the same folder on Windows. Look at `os.path.normcase` and `os.path.normpath`.

```python
diagnose("C:\\proj\\.venv", "C:\\Python313", (3, 13, 7), "3.12", {})
# → []

diagnose("C:\\Python313", "C:\\Python313", (3, 11, 9), "3.12",
         {"VIRTUAL_ENV": "C:\\venvs\\storefront", "PYTHONPATH": "C:\\libs"})
# → ["NOT_IN_VENV", "PYTHONPATH_SET", "PYTHON_TOO_OLD", "VIRTUAL_ENV_MISMATCH"]
```

```powershell
python -m pytest
```

**Afterwards:** run your doctor on the real thing, from the course folder:

```powershell
.venv\Scripts\python -c "import sys, os; sys.path.insert(0, r'<this folder>'); import main; print(main.diagnose(sys.prefix, sys.base_prefix, tuple(sys.version_info), '3.13', dict(os.environ)))"
```
