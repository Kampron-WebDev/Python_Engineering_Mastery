# Exercise 01: Venv Info

**Goal:** understand a virtual environment from the *inside*: detect it, read its config, find its interpreter.

## Your task

### `in_virtualenv(prefix, base_prefix)`

True if the two prefixes differ. (Real use: `in_virtualenv(sys.prefix, sys.base_prefix)`. Taking them as parameters makes it testable.)

### `read_pyvenv_cfg(text)`

Parse the text of a `pyvenv.cfg` into a dict:

- Each line is `key = value`. Split on the **first** `=` only (values may contain `=`).
- Strip spaces around keys and values.
- Skip blank lines and lines without `=`.

```python
read_pyvenv_cfg("home = C:\\Python313\ninclude-system-site-packages = false\nversion = 3.13.7\n")
# → {"home": "C:\\Python313", "include-system-site-packages": "false", "version": "3.13.7"}
```

### `venv_python(venv_dir, platform)`

The path (a `pathlib.Path`) to a venv's interpreter:

- `platform == "win32"` → `venv_dir / "Scripts" / "python.exe"`
- anything else → `venv_dir / "bin" / "python"`

## Check your work

```powershell
python -m pytest
```

The last test reads the **real** `pyvenv.cfg` of the course's own `.venv`. Your parser must handle it.

<details><summary>Hint</summary>

`line.partition("=")` returns `(before, "=", after)`, splitting on the first `=` only.

</details>
