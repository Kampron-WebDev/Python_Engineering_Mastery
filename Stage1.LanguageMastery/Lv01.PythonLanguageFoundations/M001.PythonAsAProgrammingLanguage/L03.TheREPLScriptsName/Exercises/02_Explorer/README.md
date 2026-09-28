# Exercise 02: Explorer

**Goal:** turn the REPL habits `dir()` and `type()` into a small tool, so you can explore *any* object.

## Your task

### `public_names(obj)`

Return a **sorted list** of the object's attribute names that **don't start with an underscore**. Underscore names are Python's internal "dunder" machinery (`__init__`, `__len__`…) or private helpers.

```python
public_names([])        # → ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

### `describe(obj)`

Return `"<type name> with <n> public attributes"`.

```python
describe([])         # → 'list with 11 public attributes'
describe(42)         # → 'int with … public attributes'
```

## Check your work

```powershell
python -m pytest
```

Then try it in the REPL on things you're curious about: `str`, `"text"`, a module like `math`, even the `describe` function itself. Functions are objects too!

<details><summary>Hint</summary>

`dir(obj)` lists attribute names. `name.startswith("_")` checks the prefix. `type(obj).__name__` is the type's name.

</details>
