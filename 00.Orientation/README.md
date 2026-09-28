# 00 · Orientation

[🏠 Course](../README.md) · Next: [Module 001 · Lesson 01 ➡](../Stage1.LanguageMastery/Lv01.PythonLanguageFoundations/M001.PythonAsAProgrammingLanguage/L01.WhatPythonIsAndIsNot/README.md)

⏱️ About 1 hour. Do this once, before Lesson 01.

---

## 🧸 What kind of course is this?

This isn't "learn to print Hello World". Python will be the language you use for **backends, automation, data and AI infrastructure** for years. So we learn it the way a senior engineer knows it: what it does, *how* it does it underneath, and *when* it's the wrong tool.

## Step 1 · Meet your Python(s)

Your computer has several Pythons: 3.13, 3.12 and 3.11 in `C:\Python3xx`, plus the Windows Store alias. Right now a virtual environment from an **old project called `storefront`** is active in your terminal, so typing `python` runs *that* one. Check:

```powershell
python -c "import sys; print(sys.executable)"
```

If it prints something with `storefront` in it, that's the old project's environment. Module 002 explains exactly why this happens. For now, this course has its **own** environment, so it isn't affected.

## Step 2 · The course's virtual environment

A virtual environment (`.venv`) has already been created in the course folder with **Python 3.13** and the test tools (`pytest`). To use it in a terminal:

```powershell
cd "$HOME\Desktop\Python-Engineering-Mastery"
deactivate                     # only if another environment (like storefront) is active; an error here is fine
.venv\Scripts\activate         # your prompt now starts with (.venv)
python --version               # Python 3.13.x
python -m pytest --version     # pytest 8+ / 9+
```

If `.venv` is ever deleted or broken, rebuild it:

```powershell
C:\Python313\python.exe -m venv .venv
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install --group dev      # reads [dependency-groups] from pyproject.toml
```

(`uv sync` does the same, faster. Module 002 teaches both.)

**In VS Code:** open this folder, install the recommended extensions when asked (Python, Debugpy, Ruff, Even Better TOML), then press **Ctrl+Shift+P → "Python: Select Interpreter"** and pick `.venv`.

> 💡 Python 3.14 has been out since October 2025. The course works on 3.13+. When a lesson uses something 3.14-only, it will say so. Module 002, Lesson 01 shows how to install and manage several versions.

## Step 3 · Make it a Git repository

```powershell
git init
git add .
git commit -m "Start Python Engineering Mastery"
```

`.gitignore` already keeps `.venv`, `__pycache__` and `.env` files out of Git. Commit at the end of every lesson.

## Step 4 · How exercises work

```text
01_TrafficLight/
├── README.md       ← what to build
├── main.py         ← YOUR file: complete the TODOs
├── test_main.py    ← the checker (don't edit)
└── solution/
    └── main.py     ← the model answer (look only AFTER trying)
```

```powershell
cd <the exercise folder>
python -m pytest        # ❌ red at first → make it ✅ green
```

In `test_main.py` you'll see tests like `def test_something(main):`. The `main` parameter is a **pytest fixture**, defined once in the course's `conftest.py`, and it hands the test *your* `main.py`, already imported. You'll learn fixtures properly in Module 080; for now, just know that's how the checker finds your code.

Reading pytest output: `.` means a test passed, `F` means it failed. Under `FAILED`, look for the `assert` line: it shows what your code **actually** returned next to what was **expected**.

## Step 5 · The rules

1. **Predict before you run.** Write down what you think will happen first. Being wrong is where learning happens.
2. **Type it yourself.** No copy-pasting examples.
3. **The 20-minute rule.** Stuck? 20 honest minutes (`print`, `breakpoint()`, re-reading), then one hint, then the solution.
4. **AI is a tutor, not a ghostwriter.** Ask it to explain; don't let it write your exercises.
5. **Read the source of truth.** When a lesson links to docs.python.org or a PEP, open it.
6. **Gates, not calendars.** Move on when the module gate is honestly ticked.

## Step 6 · Warm-up

- Skim the [Syntax Preview](Syntax-Preview.md): Python next to JavaScript and C++, just enough for Module 001.
- Do [Exercise 01: Warm-Up](Exercises/01_WarmUp/README.md).

✅ **Done when:** `.venv` works, the repo has its first commit, and the warm-up is green.

➡ **Next:** [Module 001 · Lesson 01: What Python Is and Is Not](../Stage1.LanguageMastery/Lv01.PythonLanguageFoundations/M001.PythonAsAProgrammingLanguage/L01.WhatPythonIsAndIsNot/README.md)
