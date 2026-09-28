# Lesson 01: What Python Is and Is Not

[🏠 Course](../../../../README.md) · [Module 001](../README.md) · [Next ➡](../L02.CPythonSourceToBytecodeToThePVM/README.md)

**Module 001 · Lesson 01** · ⏱️ about 1.5 hours · Needs: [Orientation](../../../../00.Orientation/README.md)

---

## 1. Concept

🧸 **Simple version:**
If C++ is a racing car (very fast, but you control every gear and have to maintain the engine yourself), Python is a **comfortable, reliable van**. It's not the fastest thing on the road, but it carries almost anything, anyone can drive it, and there's a huge garage of ready-made parts (libraries) for every job.
And when you *do* need racing speed, the van can tow a racing car. That's how NumPy and PyTorch work: Python on top, C/C++ underneath.

🎓 **Precise version:**
Python is a **high-level, general-purpose, dynamically and strongly typed** language that emphasises readability. Programs are executed by an **interpreter**, usually **CPython** (the reference implementation, written in C), which compiles source code to **bytecode** and runs it on a **virtual machine**.

| Property | Meaning |
|---|---|
| High-level | You think about data and logic, not memory addresses |
| General-purpose | Web, data, AI, automation, scripting, science… |
| **Dynamically** typed | *Names* have no types; *objects* do. Types are checked while running |
| **Strongly** typed | No silent conversions between unrelated types: `"3" + 3` is an error, not `"33"` |
| Interpreted (via bytecode) | No separate build step; `python app.py` runs it |
| Batteries included | A huge standard library: files, JSON, HTTP, CSV, dates, testing, async… |

## 2. Why it exists

In the late 1980s, **Guido van Rossum** wanted a language that sat between shell scripts (too limited) and C (too much ceremony for everyday tasks). Python was first released in **1991**, and named after *Monty Python's Flying Circus*, not the snake.

Its design is summarised in **The Zen of Python** (type `import this` in the REPL):

> *Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex… Readability counts.*

Code is read far more often than it is written. Python optimises for the **reader**, and that's why it became the language of scientists, data engineers and AI researchers: people whose main job isn't programming.

## 3. Internal mechanics: strengths and honest weaknesses

| Python is great at… | …but watch out for |
|---|---|
| Backends & APIs (Django, FastAPI) | **Speed of pure-Python loops**: often 10–100× slower than C/C++ for tight number crunching |
| Data & AI (NumPy, pandas, PyTorch) | The **GIL** limits CPU-parallel threads (Level XVI; free-threaded Python is arriving) |
| Automation, scripting, DevOps tools | Mobile apps and browsers: not Python's home |
| Gluing systems together | Dynamic typing can hide bugs in big codebases (so: type hints, Level VIII) |
| Teaching & prototyping | Packaging used to be messy (modern tools fix most of it: Module 002) |

The trick everyone uses: **Python for orchestration, C/C++ for the heavy maths.** `numpy.dot` is Python calling optimised C. You'll build exactly this in Module 139 (Python + C++).

### A living language

- Python 3.0 (2008) broke compatibility with Python 2 to fix design mistakes. Python 2 died on **1 January 2020**.
- Since 3.9, a new version ships **every October** (3.13 in 2024, 3.14 in 2025…), and each version gets about **5 years** of support.
- Changes are proposed as **PEPs** (Python Enhancement Proposals) and decided by the elected **Steering Council**. PEP 8 is the style guide; PEP 20 is the Zen.

## 4. Simple examples

```powershell
cd Examples
python zen.py            # the Zen of Python… and its secret encoding
python typing_tour.py    # dynamic + strong typing in action
```

Then in the REPL (`python`): try `import this`, then `this.s`. The Zen is stored **scrambled** inside the `this` module. Today's exercise unscrambles it.

## 5. Real-world examples

- **Instagram** runs one of the world's largest Django (Python) deployments.
- **PyTorch** (most modern AI research, and many production models) is a Python API over C++/CUDA.
- **Ansible**, much of **AWS's CLI**, countless CI scripts: Python automation everywhere.
- Your future stack: TypeScript for the web platform, **Python for AI services, data pipelines and workers**, C++ for hot paths.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [Zen Decoder](Exercises/01_ZenDecoder/README.md) | Strings, loops, `ord`/`chr`: decode the Zen yourself |
| 2 | [What Happens?](Exercises/02_WhatHappens/README.md) | Feeling "dynamic but strong" typing, by predicting first |

## 7. Debugging challenge

[Too Strict Type Check](Debugging/01_TooStrictType/README.md): **2 bugs** that fight Python's duck typing.

## 8. Design question

> A startup must build a product with **(a)** a web dashboard, **(b)** an API, **(c)** a nightly job crunching 50 GB of sensor data and **(d)** an ML model that predicts failures.

In MY-NOTES.md: for each part, would you pick Python, TypeScript or C++ (or a mix)? Justify each with a strength *and* a weakness from section 3.

## 9. Short assessment

1. Python is dynamically **and** strongly typed. Explain both words with one example each.
2. What is CPython?
3. Why is `numpy` fast even though Python loops are slow?
4. What is a PEP? Name two famous ones.
5. How often does a new Python version come out, and roughly how long is each supported?

<details><summary>Answers</summary>

1. Dynamic: a name can refer to an `int` now and a `str` later; types are checked at runtime. Strong: Python won't silently convert unrelated types, so `"3" + 3` raises `TypeError`.
2. The reference implementation of Python, written in C: the program that runs your `.py` files when you type `python`.
3. The heavy loops run inside compiled C code on whole arrays at once; Python only orchestrates.
4. A Python Enhancement Proposal: a design document for a change. PEP 8 (style guide), PEP 20 (the Zen).
5. Every October; about five years.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain "dynamic and strong typing" to a 10-year-old.
- Which line of the Zen of Python do you disagree with, or not understand yet?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| CPython | The reference Python implementation, written in C |
| Dynamic typing | Types belong to objects and are checked at runtime |
| Strong typing | No implicit conversion between unrelated types |
| Standard library | The modules that ship with Python |
| PEP | Python Enhancement Proposal |
| Zen of Python | PEP 20: Python's design philosophy |

## ✅ Done when

- [ ] I ran both examples and tried `import this` in the REPL
- [ ] Both exercises are green (predictions written first)
- [ ] Both type-check bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
