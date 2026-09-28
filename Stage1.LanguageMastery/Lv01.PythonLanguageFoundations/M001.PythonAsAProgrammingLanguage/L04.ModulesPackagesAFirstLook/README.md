# Lesson 04: Modules & Packages: A First Look

[🏠 Course](../../../../README.md) · [Module 001](../README.md) · [⬅ Previous](../L03.TheREPLScriptsName/README.md) · [Next ➡](../L05.DynamicStrongDuckTyping/README.md)

**Module 001 · Lesson 04** · ⏱️ about 2 hours · Needs: Lesson 03

> A **first look**. Level VII (Modules 037–042) goes deep: the import system, packaging, `pyproject.toml`, publishing.

---

## 1. Concept

🧸 **Simple version:**
A **module** is one toolbox (one `.py` file). A **package** is a cupboard of toolboxes (a folder of modules). `import` fetches a toolbox so you can use its tools.
The first time you fetch a toolbox, Python **builds** it (runs the file). After that, anyone who asks gets **the same toolbox**; it's never built twice.

🎓 **Precise version:**

- A **module** is a `.py` file; importing it **executes** it once, producing a **module object** whose attributes are the file's top-level names.
- Imported modules are cached in **`sys.modules`**; later imports return the cached object.
- A **package** is a directory of modules, usually with an `__init__.py` (which runs when the package is imported).
- Python searches for modules along **`sys.path`**: **the script's own folder first**, then the standard library, then installed packages (`site-packages`).

```python
import math                      # bind the NAME math to the module object
from math import sqrt            # bind the name sqrt to the module's sqrt object
from math import sqrt as root    # …under a different local name
import json.decoder              # a module inside a package
```

## 2. Why it exists

One giant file is impossible to navigate, test or share. Modules give each part of a program its own **namespace**, so `cart.total` and `invoice.total` don't collide, and let you reuse code across projects.
Python's standard library is **"batteries included"**: `json`, `csv`, `datetime`, `pathlib`, `collections`, `http`, `sqlite3`, `unittest`, `asyncio`… You'll import far more code than you write.

## 3. Internal mechanics

### What `import money` actually does

```text
1. Is "money" already in sys.modules?  → yes: just bind the name to it. Done.
2. Otherwise search sys.path, in order: the script's folder, then the stdlib, then site-packages…
3. Found money.py → create an empty module object → put it in sys.modules
4. EXECUTE money.py's code inside that module object (functions and variables are created)
5. Bind the name `money` in the importing file to the module object
```

### Two consequences that bite

**① Your files can shadow the standard library.** Because the script's folder is searched **first**, a file named `random.py`, `statistics.py` or `json.py` next to your script *replaces* the real module for that script. The error message is confusing: `module 'random' has no attribute 'randint'`.

**② `from x import NAME` copies a binding, not a live link.**

```python
# pricing.py
TAX_RATE = 0.15
def add_tax(amount):
    return amount * (1 + TAX_RATE)     # reads pricing.TAX_RATE

# main.py
from pricing import TAX_RATE, add_tax  # main gets its OWN name TAX_RATE → the object 0.15
TAX_RATE = 0.2                         # rebinds main's name only; pricing.TAX_RATE is still 0.15!
add_tax(100)                           # → 115.0, not 120.0
```

To change a module's global, change it *on the module*: `import pricing; pricing.TAX_RATE = 0.2`. (Better still, pass the rate as a parameter. Global state is a trap.)

Remember from your JS course: ES modules have **live bindings**, so this exact bug *can't* happen in JavaScript. Different languages, different module semantics.

### Packages and `python -m`

```text
shop/
├── __init__.py        ← runs on `import shop`; often re-exports the public API
├── money.py
└── cart.py
```

`python -m shop.cart` runs `cart.py` *as part of the package*, which is how you run modules that use package imports.

## 4. Simple examples

```powershell
cd Examples\shop;       python main.py
cd ..\run_once;         python main.py      # how many times does counter.py run?
cd ..\shadowing;        python main.py      # a local random.py breaks the real one
cd ..\package_demo;     python -m greetings.hello
```

## 5. Real-world examples

- Every Python project (Django, FastAPI apps, data pipelines) is a **package** of modules. Level VII teaches the professional `src/` layout.
- The **shadowing bug** is so common that recent Python versions add hints to the error message when a local file shadows a standard-library module.
- **Import time is startup time.** Big apps measure it with `python -X importtime app.py`.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [Split into Modules](Exercises/01_SplitIntoModules/README.md) | Three files working together |
| 2 | [Batteries Included](Exercises/02_BatteriesIncluded/README.md) | Using the standard library instead of reinventing it |

## 7. Debugging challenge

[Import Gotchas](Debugging/01_ImportGotchas/README.md): **2 bugs**, one from each "consequence that bites" above.

## 8. Design question

> A data team's project has 30 scripts in one folder, each with copy-pasted helper functions (`load_csv`, `clean_names`, `send_report`).

In MY-NOTES.md: propose a package structure (folder and module names). Which modules would be shared? What would each script look like afterwards? How would you stop someone creating a `csv.py` helper file by accident?

## 9. Short assessment

1. What happens the *second* time a module is imported?
2. In what order does Python search for modules?
3. Why does a local `random.py` break `import random`?
4. After `from pricing import TAX_RATE` and `TAX_RATE = 0.2`, what is `pricing.TAX_RATE`? Why?
5. Module vs package?

<details><summary>Answers</summary>

1. Nothing is executed again; the cached module object from `sys.modules` is returned.
2. Along `sys.path`: the script's own folder first, then the standard library, then installed packages (`site-packages`).
3. The script's folder is searched first, so the local file is imported *instead of* the standard-library module.
4. Still `0.15`. `from … import` bound a new name in `main` to the same object; reassigning that name doesn't touch `pricing`'s global.
5. A module is a single `.py` file; a package is a directory of modules (usually with `__init__.py`).

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain "import runs the file once and caches it" to a 10-year-old (the toolbox, or your own analogy).
- Compare Python's `from x import y` with JavaScript's live ES-module bindings. Which do you prefer, and why?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| Module | A `.py` file; a namespace of names |
| Package | A folder of modules (with `__init__.py`) |
| `sys.modules` | The cache of already-imported modules |
| `sys.path` | The list of places Python searches for modules |
| Shadowing | A local file hiding a module with the same name |
| Binding | The link between a name and an object |

## ✅ Done when

- [ ] I ran all four examples and explained each result
- [ ] Both exercises are green
- [ ] Both import gotchas fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
