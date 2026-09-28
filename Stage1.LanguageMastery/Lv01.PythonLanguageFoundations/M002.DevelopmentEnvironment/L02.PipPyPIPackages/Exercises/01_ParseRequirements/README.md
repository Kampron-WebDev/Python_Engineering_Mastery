# Exercise 01: Parse Requirements

**Goal:** read a `requirements.txt` the way pip does, including name normalisation.

## Your task

`parse_requirements(text)` returns a dict: **normalised name → specifier string** (`""` if there's none).

Rules:

1. Skip blank lines and lines starting with `#`.
2. Remove **inline comments**: anything from ` #` (space + hash) onward.
3. Skip **option lines** starting with `-` (like `-r base.txt`, `--index-url …`).
4. Drop **environment markers**: anything from `;` onward.
5. The name ends where the specifier begins: at the first `<`, `>`, `=`, `!` or `~`. Strip spaces around the name, and remove **all** spaces from the specifier (`~= 2.1` → `~=2.1`).
6. **Normalise** the name (PEP 503): lowercase it, and turn every run of `-`, `_` or `.` into a single `-`.

```python
parse_requirements("""
# web stuff
Requests>=2.32   # http
Django_REST.framework==3.15
pytest ; python_version >= "3.12"
-r base.txt
""")
# → {"requests": ">=2.32", "django-rest-framework": "==3.15", "pytest": ""}
```

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint: normalising</summary>

`import re` then `re.sub(r"[-_.]+", "-", name).lower()`. (Regular expressions get a whole module later; this one line is enough for now.)

</details>

<details><summary>Hint: finding where the specifier starts</summary>

Loop over the characters with `enumerate(line)` and stop at the first one that's `in "<>=!~"`.

</details>
