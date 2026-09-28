# Exercise 02: Batteries Included

**Goal:** solve three everyday tasks by **importing** the right standard-library module instead of writing it yourself. A senior habit: *check the standard library first.*

## Your task

| Function | Behaviour | Module to use |
|---|---|---|
| `top_words(text, n)` | The `n` most common words (lowercased, split on whitespace), as `(word, count)` pairs, most common first | `collections.Counter` |
| `days_between(start, end)` | Whole days between two ISO dates like `"2026-01-01"` (negative if `end` is earlier) | `datetime.date` |
| `pretty_json(data)` | JSON text with 2-space indentation and **sorted** keys | `json` |

```python
top_words("the cat and the hat and the bat", 2)   # → [("the", 3), ("and", 2)]
days_between("2026-01-01", "2026-03-01")          # → 59
pretty_json({"b": 1, "a": [1, 2]})
# → '{\n  "a": [\n    1,\n    2\n  ],\n  "b": 1\n}'
```

Use a **different import style** for each, to practise all three:

- `import json`
- `from datetime import date`
- `from collections import Counter`

## Check your work

```powershell
python -m pytest
```

<details><summary>Hints</summary>

- `Counter(words).most_common(n)`
- `date.fromisoformat("2026-01-01")`; subtracting two dates gives a `timedelta`, which has `.days`
- `json.dumps(data, indent=2, sort_keys=True)`

</details>
