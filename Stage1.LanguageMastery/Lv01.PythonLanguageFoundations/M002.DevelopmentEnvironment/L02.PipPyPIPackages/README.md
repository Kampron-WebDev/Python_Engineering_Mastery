# Lesson 02: pip, PyPI & Packages

[🏠 Course](../../../../README.md) · [Module 002](../README.md) · [⬅ Previous](../L01.InstallingPythonManagingVersions/README.md) · [Next ➡](../L03.VirtualEnvironmentsVenv/README.md)

**Module 002 · Lesson 02** · ⏱️ about 1.5 hours · Needs: Lesson 01

---

## 1. Concept

🧸 **Simple version:**
**PyPI** (the Python Package Index) is a giant public **library of code** with over half a million packages. **pip** is the **librarian**: you ask for a package by name, and it fetches it (and everything *that* package needs) and puts it on the shelf of **one specific Python**.

🎓 **Precise version:**

- A **distribution package** (e.g. `requests`) is what you install; an **import package** (e.g. `import requests`) is what you use in code. **Their names can differ**: install `beautifulsoup4`, import `bs4`; install `Pillow`, import `PIL`.
- `pip` installs distributions into the **`site-packages`** folder of the interpreter that runs it.
- **Version specifiers** (PEP 440): `==2.32.3` exact, `>=2.30` at least, `~=2.32` compatible release, `!=2.31.0` exclude one.
- Names are **normalised** (PEP 503): case-insensitive, and `-`, `_`, `.` are treated alike. `Django_REST.framework` = `django-rest-framework`.

## 2. Why it exists

Nobody should write their own HTTP client, date parser or web framework. Packages let the whole community share work, and a package manager resolves the **dependency tree** (A needs B ≥ 2, which needs C…) so you don't have to.

## 3. Internal mechanics

### Always `python -m pip`

```powershell
pip install requests              # ❓ which Python's pip is this? the first pip on PATH
python -m pip install requests    # ✅ the pip belonging to THIS python, always
```

With several Pythons (and your old `storefront` environment on PATH), bare `pip` can install into the **wrong** interpreter. `python -m pip` removes the doubt.

### Everyday commands

```powershell
python -m pip install "requests>=2.32"       # install (quote specifiers in PowerShell!)
python -m pip install -r requirements.txt    # install a list
python -m pip list                           # what's installed here
python -m pip show requests                  # details: version, location, dependencies
python -m pip freeze > requirements.txt      # exact versions of EVERYTHING installed
python -m pip uninstall requests
```

### Where do packages go?

```powershell
python -c "import site; print(site.getsitepackages())"
```

Each interpreter (and each virtual environment, Lesson 03) has its **own** `site-packages`. That's why "I installed it but `import` fails" usually means *installed into a different Python*.

### requirements.txt

```text
# a comment
requests>=2.32          # a specifier
Django==5.2.*
pytest ; python_version >= "3.12"   # an environment marker
-r base.txt             # include another file (an option line)
```

### Security

- **Typosquatting:** malicious packages named `reqeusts` or `python-dateutils` exist. Check spelling, download counts and project pages.
- **Don't `pip install` into your system Python.** Many Linux distros now block it (PEP 668, "externally managed"). Use virtual environments (next lesson).

## 4. Simple examples

```powershell
cd Examples
python site_info.py             # where do this Python's packages live? what's installed?
python -m pip show pytest       # details of a package in the course venv
```

## 5. Real-world examples

- **Supply-chain attacks** (malicious packages, hijacked maintainer accounts) are why companies pin versions, use lockfiles (Lesson 04) and scan dependencies (Level XXX).
- **Private indexes** (company-internal PyPI mirrors) let teams share internal packages and control what gets installed.
- **Name ≠ import** trips up everyone once: `pip install python-dotenv` → `import dotenv`; `pip install PyYAML` → `import yaml`; `pip install scikit-learn` → `import sklearn`.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [Parse Requirements](Exercises/01_ParseRequirements/README.md) | Reading requirements files like pip does |
| 2 | [Installed Version](Exercises/02_InstalledVersion/README.md) | `importlib.metadata`: asking Python what's installed |

## 7. Debugging challenge

[Import Names](Debugging/01_ImportNames/README.md): "I installed it, why can't I import it?", in code. **2 bugs**.

## 8. Design question

> Your team adds dependencies freely. A security scan finds a package with a critical vulnerability three levels deep in your dependency tree.

In MY-NOTES.md: how would you find **why** it's installed (who depends on it)? How do you update it safely? What process would you add so new dependencies get reviewed?

## 9. Short assessment

1. Distribution name vs import name: give two examples where they differ.
2. Why `python -m pip` instead of `pip`?
3. What does `~=2.32` mean?
4. Where does pip install packages?
5. What is typosquatting?

<details><summary>Answers</summary>

1. `beautifulsoup4` → `bs4`; `Pillow` → `PIL` (also `PyYAML` → `yaml`, `scikit-learn` → `sklearn`).
2. It guarantees pip installs into the interpreter you name, not whichever `pip` comes first on PATH.
3. "Compatible release": `>=2.32, ==2.*`. At least 2.32, but below 3.
4. Into the `site-packages` folder of the interpreter (or virtual environment) running pip.
5. Publishing malicious packages with names that are easy misspellings of popular ones.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain PyPI and pip to a 10-year-old.
- Compare with npm from your JS course: what's the same, what's different?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| PyPI | The Python Package Index |
| pip | Python's package installer |
| Distribution vs import package | What you install vs what you `import` |
| `site-packages` | Where an interpreter's installed packages live |
| Specifier | A version constraint like `>=2.32` |
| Name normalisation | Treating `-`, `_`, `.` and case alike in package names |

## ✅ Done when

- [ ] I ran `site_info.py` and `pip show pytest`
- [ ] Both exercises are green
- [ ] Both import-name bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
