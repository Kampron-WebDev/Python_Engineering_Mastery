# Lesson 03: The REPL, Scripts & `__name__`

[🏠 Course](../../../../README.md) · [Module 001](../README.md) · [⬅ Previous](../L02.CPythonSourceToBytecodeToThePVM/README.md) · [Next ➡](../L04.ModulesPackagesAFirstLook/README.md)

**Module 001 · Lesson 03** · ⏱️ about 1.5–2 hours · Needs: Lesson 02

---

## 1. Concept

🧸 **Simple version:**
A Python file can play **two roles**, like a person who is sometimes the **main actor** on stage and sometimes a **helper** backstage.

- Run it directly (`python tool.py`): it's the star. It should *do its job*.
- Import it from another file (`import tool`): it's a helper. It should just *offer its functions* and stay quiet.

A file finds out which role it's playing by checking a special variable, `__name__`.

🎓 **Precise version:**

| Way to run Python | Example | Good for |
|---|---|---|
| **REPL** (Read–Eval–Print Loop) | `python` | Experiments, exploring objects |
| **Script** | `python report.py` | Running a program |
| **Module as script** | `python -m http.server` | Running a module found on the import path |
| **One-liner** | `python -c "print(2 ** 100)"` | Tiny checks |
| **Interactive after a script** | `python -i report.py` | Poking at the program's variables after it runs |

Every module has a `__name__`. When the file is **run directly**, Python sets it to `"__main__"`; when it's **imported**, it's the module's name (`"tool"`). That gives us the famous idiom:

```python
def main():
    ...

if __name__ == "__main__":   # only when run directly, not when imported
    main()
```

## 2. Why it exists

Importing a module **runs** its top-level code (Lesson 04). Without the guard, importing `tool.py` to reuse one function would also *run the whole tool*: printing, deleting files, sending emails, whatever it does. Tests would trigger it too.
The `__name__` guard lets one file be both a reusable **library** and a runnable **program**.

## 3. Internal mechanics

### The modern REPL (Python 3.13+)

```text
>>> 2 ** 100
1267650600228229401496703205376      ← expressions: the REPL prints the value
>>> _ + 1                             ← `_` is the last result
>>> words = ["to", "be"]              ← statements print nothing
>>> help(str.split)                   ← documentation for anything
>>> dir(words)                        ← every attribute an object has
>>> type(words), id(words)
>>> exit                              ← 3.13+: no parentheses needed
```

The 3.13 REPL has colours, **multi-line editing** (arrow up brings back a whole `def`), **F1** help browsing, **F2** history, and **F3** paste mode for pasting blocks of code.

### `python -m`: run a module by name

`-m` finds a module on the import path and runs it as `__main__`. The standard library is full of useful ones:

```powershell
python -m http.server 8000     # serve the current folder over HTTP
python -m json.tool data.json  # pretty-print JSON
python -m timeit "sum(range(1000))"
python -m venv .venv           # (Module 002)
python -m pip install …        # always prefer this to plain `pip` (Module 002)
```

### A well-behaved script's shape

```python
import sys

def summarize(numbers):          # pure logic: easy to import and test
    ...

def main(argv):                  # glue: reads arguments, prints, returns an exit code
    ...
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))  # 0 = success, anything else = failure
```

## 4. Simple examples

```powershell
cd Examples
python whoami.py              # run directly:   __name__ is '__main__'
python import_whoami.py       # imported:       __name__ is 'whoami'
python -i whoami.py           # stay in the REPL afterwards and inspect its variables
python -c "import sys; print(sys.version)"
```

## 5. Real-world examples

- Every serious CLI tool is structured as `main(argv) → exit code`, so it can be **tested** without spawning processes.
- `python -m pytest`, `python -m pip`, `python -m uvicorn app:app`: modern tooling is run with `-m`, which guarantees it uses the *current* interpreter.
- Project entry points (`[project.scripts]` in `pyproject.toml`, Level VII) point at a `main()` function, not at the whole file.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [Main Guard](Exercises/01_MainGuard/README.md) | A file that's both a library and a program |
| 2 | [Explorer](Exercises/02_Explorer/README.md) | `dir()` and `type()`: exploring objects like in the REPL |

## 7. Debugging challenge

[Noisy Import](Debugging/01_NoisyImport/README.md): importing a helper file launches rockets. **2 bugs**.

## 8. Design question

> A teammate writes a 400-line `backup.py` with all its logic at top level. Now another script wants to reuse just its `compress_folder` part.

In MY-NOTES.md: sketch how you'd restructure `backup.py` so it's importable, testable **and** still runnable as `python backup.py`. What goes in `main()`? What stays out of it?

## 9. Short assessment

1. What's the value of `__name__` when a file is run directly? When imported?
2. Why does importing a module run its top-level code?
3. What does `python -m json.tool` do, compared with `python json/tool.py`?
4. What does `_` hold in the REPL?
5. Why should `main()` *return* an exit code instead of calling `exit` inside?

<details><summary>Answers</summary>

1. `"__main__"`; the module's name (e.g. `"whoami"`).
2. Importing *executes* the module once to create its functions, classes and variables, and caches the result.
3. `-m` finds `json.tool` on the import path and runs it as `__main__`, so you don't need to know where the file lives.
4. The result of the last expression evaluated.
5. So tests can call `main([...])` and check the returned code without the whole test process exiting.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain the `__name__` guard to a 10-year-old (the actor analogy, or your own).
- Compare with your JS course: what plays the role of `__name__ == "__main__"` in Node ES modules?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| REPL | Interactive Read–Eval–Print Loop |
| Script | A file run directly by the interpreter |
| `__name__` | A module's name; `"__main__"` when run directly |
| `python -m` | Run a module found on the import path as a script |
| Exit code | A number a process returns (0 = success) |

## ✅ Done when

- [ ] I tried every REPL line in section 3 and ran all four examples
- [ ] Both exercises are green
- [ ] Both noisy-import bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
