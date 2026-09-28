# Lesson 06: Module 001 Review

[🏠 Course](../../../../README.md) · [Module 001](../README.md) · [⬅ Previous](../L05.DynamicStrongDuckTyping/README.md) · Next: [Module 002 ➡](../../M002.DevelopmentEnvironment/README.md)

**Module 001 · Review** · ⏱️ about 2 hours

---

## 1 · The module in one picture

Draw it from memory in MY-NOTES.md first, then compare.

```text
  your .py ─► tokens ─► AST ─► code object (bytecode) ─► PVM (stack machine, in C) = CPython
                                     │ cached as __pycache__/*.pyc for imported modules
  run directly  → __name__ == "__main__"     imported → runs ONCE, cached in sys.modules
  search order  → script folder (shadowing!) → stdlib → site-packages
  names are LABELS on objects · objects carry their TYPE (dynamic) · no silent conversions (strong)
  behaviour over identity (duck typing) · try it, catch it (EAFP) · `is` for identity, `==` for value
```

## 2 · Quiz (no notes, 25 minutes, 15 points)

1. Python vs CPython vs PyPy.
2. Order these: bytecode, source, AST, PVM, tokens.
3. What kind of machine is the PVM?
4. What's in `__pycache__`, and why isn't the script you run directly cached?
5. What does `python -m py_compile f.py` do?
6. The value of `__name__` when a file is run directly, and when imported?
7. Why should `main()` return an exit code instead of exiting?
8. What happens on the second `import x`?
9. Why can a local `json.py` break your program?
10. After `from cfg import DEBUG` and `DEBUG = True`, is `cfg.DEBUG` changed? Why?
11. Dynamic + strong: explain with `x = 1; x = "a"` and `"a" + 1`.
12. Why is `isinstance(True, int)` true?
13. EAFP vs LBYL: which is Pythonic, and why?
14. Why `x is None` rather than `x == None`?
15. Does `def f(n: int)` stop `f("hi")`?

<details><summary>✅ Answers</summary>

1. Python is the language; CPython is the reference implementation in C; PyPy is an alternative implementation with a JIT.
2. source → tokens → AST → bytecode → PVM.
3. A stack machine.
4. Cached bytecode for imported modules. The directly-run script is recompiled each time (only imports are cached).
5. It compiles the file (reporting syntax errors) without running it.
6. `"__main__"`; the module's own name.
7. So tests (and other code) can call it and check the result without the process exiting.
8. The cached module from `sys.modules` is returned; the file doesn't run again.
9. The script's folder is searched first, so the local file shadows the standard-library `json`.
10. No. `from … import` created a new binding in the importing module; rebinding it doesn't affect `cfg`.
11. Dynamic: the name `x` can refer to an int, then a str. Strong: `"a" + 1` raises `TypeError` instead of converting.
12. `bool` is a subclass of `int`.
13. EAFP is Pythonic: it's simpler, avoids race conditions between check and use, and fits duck typing.
14. `==` can be overridden by `__eq__`; `is` checks identity and can't be fooled.
15. No. Type hints aren't enforced at runtime.

</details>

**Score:** ___ / 15.

## 3 · No-hints challenge: Value Inspector

[Value Inspector](Exercises/01_ValueInspector/README.md): describe *any* object by what it can **do**.

## 4 · Explain it back (Feynman)

Record 60-second explanations for an imaginary 12-year-old:

1. What happens between typing `python app.py` and the first line running?
2. Why does a file sometimes need `if __name__ == "__main__":`?
3. What does "Python is dynamically but strongly typed" mean?
4. Why is duck typing useful?

## 5 · Mastery gate

Tick the [Module 001 gate](../README.md#-mastery-gate) honestly and record it in [PROGRESS.md](../../../../PROGRESS.md).

- ✅ **Ticked, and the quiz ≥ 11/15?** Commit and start [Module 002: Development Environment](../../M002.DevelopmentEnvironment/README.md).
- 🔁 **Not yet?** Redo your weakest lesson's exercises from scratch, and retake the quiz in two days.
