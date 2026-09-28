# Lesson 06: VS Code, IPython & the Debugger

[🏠 Course](../../../../README.md) · [Module 002](../README.md) · [⬅ Previous](../L05.EnvironmentVariablesConfiguration/README.md) · [Next ➡](../L07.ModuleReview/README.md)

**Module 002 · Lesson 06** · ⏱️ about 2 hours · Needs: Lessons 01–05

---

## 1. Concept

🧸 **Simple version:**
Adding `print()` everywhere is like finding a problem in a car by driving it past a camera again and again. A **debugger** lets you **freeze time**: stop the car mid-drive, open the bonnet, look at every part, then move forward one tiny step at a time.

🎓 **Precise version:**

| Tool | What it's for |
|---|---|
| **`pdb`** / `breakpoint()` | Python's built-in debugger: pause, inspect, step, in any terminal |
| **VS Code debugger** (debugpy) | The same power with a visual interface: breakpoints, variables panel, watch, call stack |
| **IPython** | A supercharged REPL: `?` help, `%timeit`, `%run`, `%debug` post-mortem |
| **`timeit`** | Measure small pieces of code *properly* (many repetitions, no noise from printing) |

## 2. Why it exists

Print-debugging needs a guess about *what* to print, a re-run for every new question, and clean-up afterwards. A debugger answers **every** question in one run: the value of every variable, the path that led here, what happens on the next line.
The best engineers use both: prints (or better, logging) for *production*, debuggers for *understanding*.

## 3. Internal mechanics

### `breakpoint()` and pdb

Put `breakpoint()` on any line and run the program. It stops there with a `(Pdb)` prompt:

| Command | Does |
|---|---|
| `l` (list) / `ll` | Show code around the current line / the whole function |
| `n` (next) | Run the current line, stop at the next one (step **over** calls) |
| `s` (step) | Step **into** the function called on this line |
| `r` (return) | Run until the current function returns |
| `c` (continue) | Run to the next breakpoint |
| `p expr` / `pp expr` | Print / pretty-print any expression |
| `w` (where) | Show the call stack |
| `u` / `d` | Move up / down the stack to inspect callers |
| `b 42` | Set a breakpoint on line 42 |
| `q` | Quit |

Tip: set the environment variable `PYTHONBREAKPOINT=0` to make every `breakpoint()` do nothing. That's useful if one sneaks into a commit.

### The VS Code debugger (this course is already set up)

1. Click left of a line number to set a red breakpoint.
2. **F5 → "Debug this file"** (or "Debug this exercise's tests" when a test file is open).
3. **F10** step over, **F11** step into, **Shift+F11** step out, **F5** continue.
4. Watch the **Variables**, **Watch** and **Call Stack** panels. Right-click a breakpoint for **conditional breakpoints** (`i == 500`) and **logpoints** (print without editing code).

### IPython (optional install)

```powershell
.venv\Scripts\python -m pip install ipython
.venv\Scripts\ipython
```

```text
In [1]: str.split?          ← documentation
In [2]: %timeit sum(range(1000))
In [3]: %run my_script.py   ← run a file, keep its variables
In [4]: %debug              ← after an exception: jump into the crash in pdb
```

### Measuring properly with `timeit`

```python
import timeit
timeit.timeit(lambda: sum(range(1000)), number=10_000)   # total seconds for 10,000 runs
```

Never time a single run of a fast function. Noise dominates.

## 4. Simple examples

```powershell
cd Examples
python pdb_tour.py          # stops at breakpoint(): try n, s, p total, w, c
python -m timeit -n 10000 "sum(range(1000))"
```

Then open `pdb_tour.py` in VS Code, remove the `breakpoint()` line, set a red breakpoint instead, and press **F5**.

## 5. Real-world examples

- **Post-mortem debugging:** `python -m pdb -c continue app.py` runs the program and drops into the debugger exactly where it crashes.
- **Remote debugging:** debugpy can attach VS Code to a Python process running in a Docker container or on a server.
- **Performance questions** ("is `join` faster than `+=`?") are settled with `timeit`, not opinions.

## 6. Coding exercise

| # | Exercise | Skill |
|---|---|---|
| 1 | [Timing Lab](Exercises/01_TimingLab/README.md) | Measuring with `timeit`, and making decisions with data |

## 7. Debugging challenge

[Use the Debugger](Debugging/01_UseTheDebugger/README.md): **3 bugs**. You must record hypothesis → experiment → result for each, using breakpoints.

## 8. Design question

> A colleague says: "I never use debuggers, prints are faster." Another says: "prints are for amateurs."

In MY-NOTES.md: argue *both* sides fairly. When is each approach genuinely better? What would you use in production, where you can't pause the program?

## 9. Short assessment

1. What does `breakpoint()` do?
2. `n` vs `s` in pdb?
3. How do you inspect the *caller's* variables in pdb?
4. How do you disable all `breakpoint()` calls without editing code?
5. Why time a function 10,000 times instead of once?

<details><summary>Answers</summary>

1. It pauses the program at that line and opens the debugger (pdb by default).
2. `n` runs the whole current line (stepping over calls); `s` steps into the function being called.
3. `u` (up) moves to the caller's frame; then `p` its variables. `d` goes back down.
4. Set `PYTHONBREAKPOINT=0`.
5. A single fast run is dominated by noise (timer resolution, other processes); many repetitions give a stable average.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain "stepping through code" to a 10-year-old.
- Compare with the Node/VS Code debugging in your JS course, and gdb from the C++ course.
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| Breakpoint | A place where execution pauses |
| Step over / into / out | Run a line / enter a call / finish the current function |
| Call stack | The chain of active function calls |
| Post-mortem debugging | Inspecting the program's state at the moment it crashed |
| `timeit` | Standard-library tool for accurate micro-benchmarks |

## ✅ Done when

- [ ] I used every pdb command in the table on `pdb_tour.py`
- [ ] I used a VS Code breakpoint and the Variables panel
- [ ] Timing Lab is green
- [ ] All three bugs fixed **with** hypothesis → experiment notes
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
