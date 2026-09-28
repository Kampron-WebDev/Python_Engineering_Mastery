# Lesson 02: CPython: Source to Bytecode to the PVM

[🏠 Course](../../../../README.md) · [Module 001](../README.md) · [⬅ Previous](../L01.WhatPythonIsAndIsNot/README.md) · [Next ➡](../L03.TheREPLScriptsName/README.md)

**Module 001 · Lesson 02** · ⏱️ about 2 hours · Needs: Lesson 01

---

## 1. Concept

🧸 **Simple version: a translator and a very simple robot**

Your `.py` file is written in *human* Python. The computer can't run that directly. So CPython works in two steps:

1. A **translator** reads your whole file and rewrites it as a list of tiny, simple instructions called **bytecode**: "load x", "load 2", "multiply", "store in total".
2. A very simple **robot** (the **Python Virtual Machine**, PVM) reads those instructions one by one and does them, using a **stack** like a pile of plates: push values on, pop them off, combine them.

🎓 **Precise version:**

```text
source text ─► tokenizer ─► parser ─► AST ─► compiler ─► code object (bytecode) ─► PVM evaluation loop
 (your .py)     tokens      (PEG)     tree              + constants + names       (a stack machine in C)
```

- **CPython** is the reference implementation of Python, written in C. It's what `python` usually means.
- The result of compiling is a **code object**: bytecode plus the constants and names it uses.
- The **PVM** is a loop in C (`ceval.c`) that executes bytecode on a **value stack**.
- For imported modules, the bytecode is cached as `.pyc` files in `__pycache__/`, so the translation step is skipped next time.

## 2. Why it exists

Why not translate straight to machine code like C++? Bytecode is **portable** (the same `.pyc` idea works on any CPU with CPython), **fast to produce** (no long build step), and keeps Python **dynamic**: the PVM checks types while running, which is what lets names change type freely.
The price is speed: executing bytecode one instruction at a time is slower than native machine code. Modern CPython fights back:

- **3.11+:** the *specializing adaptive interpreter* (PEP 659) rewrites hot instructions into faster, type-specialised versions while running. That's why 3.11 was about 25% faster than 3.10.
- **3.13+:** an *experimental JIT compiler* (PEP 744), off by default.

## 3. Internal mechanics

### Step by step for `total = price * 2`

```text
1. Tokens:   NAME 'total'  OP '='  NAME 'price'  OP '*'  NUMBER '2'
2. AST:      Assign(targets=[Name('total')], value=BinOp(Name('price'), Mult(), Constant(2)))
3. Bytecode (what the PVM runs):
     LOAD_NAME    price     ← push the value of price onto the stack
     LOAD_CONST   2         ← push 2
     BINARY_OP    * (5)     ← pop both, multiply, push the result
     STORE_NAME   total     ← pop it into the name total
```

The exact instruction names change a little between Python versions. The *idea* (a stack machine) doesn't.

### Syntax errors happen at compile time

The **whole file is compiled before any of it runs**. A syntax error on line 90 means line 1 never runs. You can compile without running:

```powershell
python -m py_compile my_file.py     # like `node --check`
```

### Python implementations

| Implementation | Written in | Notes |
|---|---|---|
| **CPython** | C | The reference; what you'll use 99% of the time |
| **PyPy** | RPython | A JIT compiler; often much faster for pure-Python loops |
| **MicroPython** | C | For microcontrollers |
| **GraalPy** | Java | Runs on the GraalVM |

"Python" is the *language*; these are *programs that run it*. (Just like ECMAScript vs V8 in your JS course.)

## 4. Simple examples

```powershell
cd Examples
python pipeline.py            # tokens → AST → code object → bytecode, for one line
python -m dis pipeline.py     # disassemble a whole file
cd pyc_demo
python main.py                # then look inside pyc_demo\__pycache__\
```

## 5. Real-world examples

- **Docker images** for Python services often pre-compile `.pyc` files (`python -m compileall`) so containers start faster.
- **Performance work** (Level XIX) starts with understanding what bytecode your hot loop produces, for example why local variables are faster than globals (`LOAD_FAST` vs `LOAD_GLOBAL`).
- **Linters and formatters** (Ruff, Black) work on the token stream and the AST, the same first steps the compiler uses.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [AST Counter](Exercises/01_ASTCounter/README.md) | Using the `ast` module: how Python *sees* your code |
| 2 | [Bytecode Inspector](Exercises/02_BytecodeInspector/README.md) | Using `dis`: what the PVM actually runs |

## 7. Debugging challenge

[Compile First](Debugging/01_CompileFirst/README.md): **2 bugs**, one found at compile time and one at run time.

## 8. Design question

> Your team's Python API container takes **12 seconds** to start, and the autoscaler needs new containers ready faster.

In MY-NOTES.md: using today's pipeline diagram, which steps happen at every start? Which could be done **once, at build time**? What else (outside this lesson) might make startup slow, and how would you *measure* it before changing anything?

## 9. Short assessment

1. Put these in order: AST, bytecode, tokens, source, PVM.
2. What is a code object?
3. What is the PVM, and what kind of machine is it?
4. What's inside `__pycache__`, and why does it exist?
5. What does `python -m py_compile file.py` do?
6. Python vs CPython vs PyPy?

<details><summary>Answers</summary>

1. source → tokens → AST → bytecode → PVM.
2. The compiled form of a module or function: bytecode plus its constants, names and other metadata.
3. The Python Virtual Machine: CPython's evaluation loop, which executes bytecode. It's a **stack machine**.
4. Cached compiled bytecode (`.pyc`) of imported modules, so they don't have to be recompiled on every run.
5. It compiles the file (reporting syntax errors) without running it.
6. Python is the language; CPython is the reference implementation (in C); PyPy is an alternative implementation with a JIT.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain source → bytecode → PVM to a 10-year-old.
- Compare CPython with V8 (JS course) and g++ (C++ course): what's similar, what's different?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| Token | The smallest meaningful piece of source text |
| AST | Abstract Syntax Tree: the structure of your code |
| Bytecode | Simple instructions for the Python Virtual Machine |
| Code object | Compiled bytecode + constants + names |
| PVM | CPython's bytecode-executing stack machine |
| `.pyc` / `__pycache__` | Cached bytecode for imported modules |
| `dis` | The standard-library disassembler |

## ✅ Done when

- [ ] I ran `pipeline.py`, `python -m dis` and the `.pyc` demo
- [ ] Both exercises are green
- [ ] Both Compile-First bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
