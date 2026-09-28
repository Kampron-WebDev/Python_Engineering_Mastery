# No-Hints Challenge: Value Inspector

Complete `inspect_value(value)`. It returns a dict describing what the value **can do**:

| Key | Value |
|---|---|
| `"type"` | the type's name, e.g. `"list"` |
| `"callable"` | can it be called like a function? |
| `"iterable"` | does `iter(value)` work? |
| `"sized"` | does `len(value)` work? |
| `"hashable"` | does `hash(value)` work? (Could it be a dict key?) |

```python
inspect_value([1, 2])
# → {"type": "list", "callable": False, "iterable": True, "sized": True, "hashable": False}

inspect_value(len)
# → {"type": "builtin_function_or_method", "callable": True, "iterable": False, "sized": False, "hashable": True}
```

Rules:

- Use **EAFP** for `iterable`, `sized` and `hashable`: try the operation, catch the exception.
- `callable` has a built-in function of the same name.
- It must work for **any** object, including your own classes.

```powershell
python -m pytest
```

**Afterwards, in MY-NOTES.md:** why is a list not hashable, but a tuple of numbers is?
