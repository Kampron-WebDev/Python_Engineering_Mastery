# Exercise 02: Dotenv Parser

**Goal:** understand exactly what a `.env` loader does, by writing one.

## Your task

`parse_dotenv(text)` returns a dict of the variables in `.env`-style text:

1. Skip blank lines and lines starting with `#` (after stripping spaces).
2. An optional leading `export ` is ignored: `export KEY=value` works.
3. Split each line on the **first** `=`. Strip spaces around the key and the value.
4. If the value is wrapped in **matching** quotes (`"…"` or `'…'`), remove them. The inside is kept exactly (including `#` and spaces).
5. Otherwise, an **inline comment** starting with ` #` (space + hash) is removed.
6. Lines without `=` are ignored.

```python
parse_dotenv('''
# local dev settings
DATABASE_URL=postgresql://localhost/quiz   # the local db
export SECRET_KEY="dev #not-a-comment"
EMPTY=
TOKEN=abc=def
''')
# → {"DATABASE_URL": "postgresql://localhost/quiz", "SECRET_KEY": "dev #not-a-comment",
#    "EMPTY": "", "TOKEN": "abc=def"}
```

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint: quotes</summary>

`len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'"`

</details>
