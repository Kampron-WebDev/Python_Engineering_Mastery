# Lesson 07: Module 002 Review

[🏠 Course](../../../../README.md) · [Module 002](../README.md) · [⬅ Previous](../L06.VSCodeIPythonTheDebugger/README.md) · Next: [Module 003 ➡](../../M003.SyntaxAndProgramStructure/README.md)

**Module 002 · Review** · ⏱️ about 2 hours

---

## 1 · The module in one picture

Draw it from memory in MY-NOTES.md first, then compare.

```text
 PATH (first match wins) ─► which python?  (sys.executable · py --list · where.exe)
         │
   base Python 3.13 ──► .venv (own site-packages; sys.prefix ≠ sys.base_prefix; activate = PATH trick)
         │                     ▲
   pyproject.toml ──(uv/Poetry resolve)──► lockfile ──(uv sync)──┘   python -m pip · names normalised
         │
   config from the ENVIRONMENT (strings! convert + validate + fail fast) · .env never committed
         │
   debug with breakpoints (pdb / VS Code) · measure with timeit
```

## 2 · Quiz (no notes, 25 minutes, 15 points)

1. What decides which `python` runs?
2. Why `sys.version_info >= (3, 11)` and not `sys.version >= "3.11"`?
3. When did Python 3.9 reach end of life? Why does it matter?
4. Why `python -m pip` instead of `pip`?
5. Distribution name vs import name: two examples.
6. Normalise `Django_REST.framework`.
7. What does activating a venv actually do?
8. How does code detect it's inside a venv?
9. Shopping list vs receipt: `pyproject.toml` vs lockfile.
10. What does `uv sync` guarantee?
11. Why does `tomllib.load` need binary mode?
12. What type are environment variable values?
13. Why is `bool(os.getenv("DEBUG"))` a bug?
14. pdb: `n` vs `s` vs `c`.
15. Why measure with `timeit` rather than one run?

<details><summary>✅ Answers</summary>

1. The first match in `PATH` (an activated venv puts itself first).
2. Tuples compare numerically part by part; strings compare character by character (`"3.9" > "3.11"`).
3. October 2025. After EOL there are no security fixes, so it's unsafe for production.
4. It guarantees you install into the interpreter you name.
5. `beautifulsoup4` → `bs4`, `Pillow` → `PIL` (or `PyYAML` → `yaml`, `scikit-learn` → `sklearn`).
6. `django-rest-framework`.
7. Puts the venv's `Scripts`/`bin` first on `PATH` and sets `VIRTUAL_ENV`.
8. `sys.prefix != sys.base_prefix`.
9. `pyproject.toml` declares what you want (ranges); the lockfile records exactly what was resolved (versions and hashes).
10. The venv exactly matches the lockfile.
11. TOML is defined as UTF-8 bytes; `tomllib` decodes it itself.
12. `str`, always.
13. Any non-empty string, including `"false"`, is truthy.
14. `n` steps over the current line; `s` steps into a call; `c` continues to the next breakpoint.
15. Single runs of fast code are dominated by noise; many repetitions give a stable average.

</details>

**Score:** ___ / 15.

## 3 · No-hints challenge: Python Doctor

[Python Doctor](Exercises/01_PythonDoctor/README.md) diagnoses a Python setup. It would have caught your `storefront` problem on day one.

## 4 · Explain it back (Feynman)

Record 60-second explanations for an imaginary 12-year-old:

1. Why does every project get its own virtual environment?
2. What's the difference between `pyproject.toml` and a lockfile?
3. Why shouldn't secrets be written in code?
4. How would you find a bug you can't understand, using a debugger?

## 5 · Mastery gate

Tick the [Module 002 gate](../README.md#-mastery-gate) and record it in [PROGRESS.md](../../../../PROGRESS.md).

- ✅ **Modules 001 and 002 both ticked, quiz ≥ 11/15?** You're ready for Module 003. Tell Claude, and the Module 003–005 lessons and the **Level I exam** will be written for you.
- 🔁 **Not yet?** Redo your weakest lesson's exercises from scratch, and retake the quiz in two days.
