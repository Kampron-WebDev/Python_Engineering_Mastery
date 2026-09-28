# Debugging 01: Import Names

A helper tells developers which name to **import** after installing a distribution:

```python
import_name("PyYAML")           # → "yaml"
import_name("pyyaml")           # → "yaml"      (distribution names are case-insensitive!)
import_name("scikit-learn")     # → "sklearn"
import_name("Scikit_Learn")     # → "sklearn"   (and - _ . are equivalent)
import_name("my-cool-lib")      # → "my_cool_lib"   (default: a valid Python identifier)
```

There are **2 bugs**.

## Your task

1. `python -m pytest`.
2. Fix both. In MY-NOTES.md: why can't the default just return the distribution name unchanged? (Try `import my-cool-lib` in the REPL.)

<details><summary>Hint 1</summary>

The table is keyed by one spelling. How should *both* the table keys and the lookup be written so every spelling matches? (Lesson 02: name normalisation.)

</details>

<details><summary>Hint 2</summary>

A Python identifier can't contain `-` or `.`.

</details>
