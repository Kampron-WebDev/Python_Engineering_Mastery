# Exercise 02: Version Compare

**Goal:** compare version numbers **correctly**, a small skill that prevents real production bugs.

## Your task

| Function | Behaviour | Example |
|---|---|---|
| `parse_version(text)` | Tuple of ints, **padded to 3 parts** | `"3.13"` → `(3, 13, 0)`, `"3.13.7"` → `(3, 13, 7)` |
| `compare_versions(a, b)` | `-1` if a < b, `0` if equal, `1` if a > b | `compare_versions("3.9", "3.13")` → `-1` |
| `newest(versions)` | The newest version **string** from a list | `newest(["3.9", "3.13.1", "3.13"])` → `"3.13.1"` |

- Invalid text (`"3.x"`, `""`, `"1.2.3.4"`) → `ValueError`.
- `"3.13"` and `"3.13.0"` are **equal**.

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint</summary>

Tuples compare element by element, exactly like versions should. `max(versions, key=parse_version)` finds the newest without writing a loop.

</details>
