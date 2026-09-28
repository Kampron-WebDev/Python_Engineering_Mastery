# Lesson 01: Installing Python & Managing Versions

[🏠 Course](../../../../README.md) · [Module 002](../README.md) · [Next ➡](../L02.PipPyPIPackages/README.md)

**Module 002 · Lesson 01** · ⏱️ about 1.5 hours · Needs: Module 001

---

## 1. Concept

🧸 **Simple version:**
Your computer can have **several Pythons installed at once**, like several versions of the same app. When you type `python`, the computer walks along a list of folders (the **PATH**) and runs the **first** `python` it finds. If you don't know which one that is, you don't know what's running your code.

🎓 **Precise version:**

- Each Python install is a separate interpreter with its own standard library and its own installed packages.
- **`PATH`** is an environment variable: an ordered list of folders the shell searches for commands. **First match wins.**
- On Windows, the **Python launcher `py`** picks a version explicitly: `py -3.13 app.py`, `py --list`.
- **`sys.executable`** tells you, from inside Python, exactly which interpreter is running.
- Tools like **uv** (`uv python install 3.14`) download and manage interpreters for you.

## 2. Why it exists

Python versions differ: new syntax (`match` in 3.10), new features (`tomllib` in 3.11, the new REPL in 3.13), removed modules, and different bytecode. Projects **declare** which versions they support (`requires-python = ">=3.12"`), and you must be able to run exactly that version.
Knowing *which* Python runs is the #1 fix for "but I installed it!" problems, like your old `storefront` environment silently answering to `python`.

## 3. Internal mechanics

### The support calendar (PEP 602)

```text
3.X released every October (3.13 → Oct 2024, 3.14 → Oct 2025, 3.15 → Oct 2026)
│
├── ~2 years: full bug-fix releases (3.14.0, 3.14.1, …)
└── ~3 more years: security fixes only
    → end of life ≈ 5 years after release   (3.9 died Oct 2025; 3.10 dies Oct 2026)
```

For 3.8 and later: **release year = 2011 + minor version**, and **end of life ≈ October, five years later**. You'll code this today.

### Version numbers are not decimals

`3.9 < 3.13` as *versions*, but as **strings**, `"3.9" > "3.13"`, because `'9' > '1'`. Always compare versions as **tuples of numbers**: `(3, 9) < (3, 13)` ✅. Python gives you one: `sys.version_info`.

```python
import sys
sys.version_info            # sys.version_info(major=3, minor=13, micro=7, …)
sys.version_info >= (3, 11) # True: the correct way to check a minimum version
sys.executable              # the exact interpreter running this code
```

### Finding out what's on your PATH

```powershell
where.exe python                             # every python on PATH, in search order
py --list                                    # every Python the launcher knows
python -c "import sys; print(sys.executable)"
$env:VIRTUAL_ENV                             # set if a virtual environment is active
```

## 4. Simple examples

```powershell
cd Examples
python which_python.py        # who am I, and which version?
py -3.12 which_python.py      # the same script under another installed version
```

## 5. Real-world examples

- **CI pipelines** run tests across a *matrix* of versions (3.12, 3.13, 3.14) to prove a library supports them all.
- **Docker images** pin an exact version: `FROM python:3.13-slim`.
- **Upgrading** a production service to a new Python is a planned project: dependencies must support it first.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [Version Policy](Exercises/01_VersionPolicy/README.md) | Encoding the release/EOL calendar |
| 2 | [Version Compare](Exercises/02_VersionCompare/README.md) | Comparing versions correctly (tuples, not strings) |

## 7. Debugging challenge

[String Versions](Debugging/01_StringVersions/README.md): **2 bugs** that think `3.9` is newer than `3.13`.

## 8. Design question

> Your company runs 40 Python services on versions 3.9 to 3.13. Python 3.10 reaches end of life next month.

In MY-NOTES.md: how do you find out which services run which version? In what order would you upgrade them, and what must be true before each upgrade? How do you stop this from happening again?

## 9. Short assessment

1. What decides which `python` runs when you type `python`?
2. What does `py -3.12 app.py` do?
3. Roughly how long is a Python version supported? When did 3.9 reach end of life?
4. Why is `"3.9" > "3.13"` True, and what's the correct comparison?
5. How do you check, inside Python, that you're on at least 3.11?

<details><summary>Answers</summary>

1. The first matching executable in the folders listed in `PATH` (or an active virtual environment, which puts itself first).
2. The Windows Python launcher runs `app.py` with the installed Python 3.12.
3. About 5 years (≈2 years of bug fixes, then security fixes). 3.9 reached end of life in October 2025.
4. Strings compare character by character, and `'9' > '1'`. Compare tuples of ints instead: `(3, 9) < (3, 13)`.
5. `sys.version_info >= (3, 11)`.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain PATH to a 10-year-old.
- Run `where.exe python` and `py --list`. What did you find? Why is `storefront` first?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| Interpreter | A specific installed Python that runs code |
| PATH | The ordered list of folders searched for commands |
| `py` launcher | Windows tool to pick a Python version |
| `sys.executable` / `sys.version_info` | Which interpreter is running / its version as numbers |
| End of life (EOL) | When a version stops getting any fixes |

## ✅ Done when

- [ ] I ran `where.exe python` and `py --list`, and understand the output
- [ ] Both exercises are green
- [ ] Both string-version bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
