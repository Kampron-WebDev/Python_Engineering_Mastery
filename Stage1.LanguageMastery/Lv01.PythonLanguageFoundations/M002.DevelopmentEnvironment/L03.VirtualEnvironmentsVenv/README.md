# Lesson 03: Virtual Environments (venv)

[🏠 Course](../../../../README.md) · [Module 002](../README.md) · [⬅ Previous](../L02.PipPyPIPackages/README.md) · [Next ➡](../L04.PyprojectTomlUvPoetry/README.md)

**Module 002 · Lesson 03** · ⏱️ about 1.5–2 hours · Needs: Lessons 01–02

---

## 1. Concept

🧸 **Simple version:**
Imagine every project had to share **one toy box**. Project A needs the *old* version of a toy; project B needs the *new* one. They fight forever.
A **virtual environment** gives every project its **own toy box**. Same Python underneath, but each project has its own private shelf of packages.

🎓 **Precise version:**
A **virtual environment** (venv) is a folder containing:

- a small **launcher** for an existing ("base") Python interpreter,
- its **own `site-packages`**, isolated from the base Python and from other environments,
- a config file, **`pyvenv.cfg`**, pointing back to the base interpreter.

```text
.venv/
├── pyvenv.cfg                 home = C:\Python313, version = 3.13.7, …
├── Scripts/                   (bin/ on Linux and macOS)
│   ├── python.exe             ← use THIS python, and you're "in" the venv
│   ├── pip.exe
│   └── activate / Activate.ps1
└── Lib/site-packages/         ← this environment's own packages
```

## 2. Why it exists

- **Conflicts:** project A needs `Django 4`, project B needs `Django 5`. One site-packages can't hold both.
- **Reproducibility:** a fresh venv plus a lockfile gives *exactly* the same packages on every machine and in CI.
- **Safety:** you never break the system Python or other projects.

## 3. Internal mechanics

### Creating and using one

```powershell
python -m venv .venv                   # create (uses whichever python you ran)
.venv\Scripts\Activate.ps1             # PowerShell: activate
.venv\Scripts\activate.bat             # cmd.exe
source .venv/bin/activate              # Linux / macOS
deactivate                             # leave
```

**What "activate" really does:** it puts `.venv\Scripts` at the **front of PATH** (Lesson 01) and sets `VIRTUAL_ENV`. That's all. You never *need* to activate: running `.venv\Scripts\python.exe` directly uses the venv. That's what the course's VS Code tasks do.

> PowerShell may refuse to run `Activate.ps1` ("running scripts is disabled"). Fix once, for your user: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

### How Python knows it's in a venv

On start-up, Python notices the `pyvenv.cfg` next to its launcher and sets:

```python
sys.prefix        # the VENV folder
sys.base_prefix   # the BASE install (C:\Python313)
sys.prefix != sys.base_prefix   # → True means "I'm running inside a virtual environment"
```

### Your `storefront` mystery, solved

When a terminal starts with an old environment **already activated** (from a tool like pipenv, or your shell profile), its `Scripts` folder sits at the front of `PATH`, so `python` means *that* environment everywhere. Check with:

```powershell
$env:VIRTUAL_ENV                       # which environment claims to be active?
where.exe python                       # the first line is what `python` runs
```

Fix it by running `deactivate`, or by removing the activation from your PowerShell profile (`notepad $PROFILE`). Either way, **always know which interpreter runs your code.**

### Rules

- One venv **per project**, usually named `.venv` in the project folder.
- **Never commit** `.venv` to Git (it's in `.gitignore`); commit the *dependency list* instead.
- A venv is **disposable**: delete it and recreate it from the dependency list at any time.
- A venv is tied to its base Python. If you uninstall `C:\Python313`, venvs made from it break.

## 4. Simple examples

```powershell
cd Examples
python where_am_i.py                                   # with whatever `python` means right now
..\..\..\..\..\.venv\Scripts\python.exe where_am_i.py  # explicitly with the course venv
python -m venv demo-env ; demo-env\Scripts\python.exe where_am_i.py ; Remove-Item -Recurse demo-env
```

## 5. Real-world examples

- **CI pipelines** create a fresh environment on every run, which guarantees the dependency list is complete.
- **Docker images** often skip venvs (the container *is* the isolation), but many teams still use one inside for consistency with local development.
- **Tools** like uv and Poetry (next lesson) create and manage venvs for you automatically.

## 6. Coding exercise

| # | Exercise | Skill |
|---|---|---|
| 1 | [Venv Info](Exercises/01_VenvInfo/README.md) | Detecting a venv; reading `pyvenv.cfg`; finding a venv's interpreter |

## 7. Debugging challenge

[Which Python?](Debugging/01_WhichPython/README.md): a PATH search that picks the wrong interpreter. **2 bugs**.

## 8. Design question

> A new developer joins and spends a day on "works on my machine" errors. Their laptop has three Pythons and global packages everywhere.

In MY-NOTES.md, write a **5-step onboarding checklist** that gets any new developer from a fresh clone to a green test run in under 10 minutes. What must live in the repository to make that possible?

## 9. Short assessment

1. What's inside a venv folder?
2. What does "activating" actually change?
3. How can code tell if it's running inside a venv?
4. Should `.venv` be committed to Git? Why?
5. Why did `python` in your terminal point at `storefront`?

<details><summary>Answers</summary>

1. A launcher for the base Python, its own `site-packages`, activation scripts and `pyvenv.cfg`.
2. It prepends the venv's `Scripts` (or `bin`) folder to `PATH` and sets `VIRTUAL_ENV`. Nothing else.
3. `sys.prefix != sys.base_prefix`.
4. No. It's large, machine-specific and reproducible from the dependency list; commit that instead.
5. That environment was activated at shell start-up, so its `Scripts` folder is first on `PATH`.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain virtual environments to a 10-year-old (the toy boxes, or your own).
- Compare with `node_modules` in your JS course: what does Node do instead of venvs?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| Virtual environment | An isolated set of packages on top of a base Python |
| `pyvenv.cfg` | The venv's config file, pointing to the base interpreter |
| Activate | Put the venv first on PATH (a convenience, not a requirement) |
| `sys.prefix` / `sys.base_prefix` | The venv folder / the base installation |
| `VIRTUAL_ENV` | Environment variable naming the active venv |

## ✅ Done when

- [ ] I ran `where_am_i.py` three ways and explained the differences
- [ ] I found out why `storefront` was active, and decided what to do about it
- [ ] Venv Info is green
- [ ] Both PATH bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
