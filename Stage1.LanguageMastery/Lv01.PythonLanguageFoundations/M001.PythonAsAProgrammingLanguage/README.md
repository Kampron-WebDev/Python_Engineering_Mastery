# Module 001: Python as a Programming Language

[🏠 Course](../../../README.md) · [Level I](../README.md) · [M002 ➡](../../../Stage1.LanguageMastery/Lv01.PythonLanguageFoundations/M002.DevelopmentEnvironment/README.md)

**Stage 1 · Level I: Python Language Foundations** · Status: 🟢 Ready

## 🧸 The big idea

Python is a language whose programs are read by an interpreter (CPython) that turns them into bytecode for a virtual machine. Names don't have types; objects do. And Python cares about what an object can DO more than what it IS (duck typing).

## 📖 Lessons

| # | Lesson | |
|---|---|---|
| 01 | [What Python Is and Is Not](L01.WhatPythonIsAndIsNot/README.md) | 🟢 |
| 02 | [CPython: Source to Bytecode to the PVM](L02.CPythonSourceToBytecodeToThePVM/README.md) | 🟢 |
| 03 | [The REPL, Scripts & __name__](L03.TheREPLScriptsName/README.md) | 🟢 |
| 04 | [Modules & Packages: A First Look](L04.ModulesPackagesAFirstLook/README.md) | 🟢 |
| 05 | [Dynamic, Strong & Duck Typing](L05.DynamicStrongDuckTyping/README.md) | 🟢 |
| 06 | [Module Review](L06.ModuleReview/README.md) | 🟢 |

Every lesson follows the 10-part format: Concept → Why it exists → Internal mechanics → Simple example → Real-world example → Coding exercise → Debugging challenge → Design question → Short assessment → Reflection.

## 🛠️ Build it yourself

- A ROT13 decoder that reveals the Zen of Python
- An AST node counter
- A bytecode inspector with `dis`
- A duck-typed total that works for any iterable

## 🎯 Mastery gate

Reading a lesson is **not** finishing it. Tick every box, honestly:

- [ ] **Explain it:** I can answer every question below out loud, simply, without notes.
  - Walk through source → tokens → AST → bytecode → PVM for a two-line program.
  - Dynamic vs static, strong vs weak: place Python, JavaScript and C++ on both axes.
  - What does `if __name__ == "__main__":` protect you from?
  - Why does `from pricing import TAX_RATE` not see later changes to pricing.TAX_RATE?
- [ ] **Implement it:** all exercises are green, written without opening solutions first.
- [ ] **Debug it:** I fixed every debugging challenge and can explain *why* each bug happened.
- [ ] **Apply it:** I used this module's ideas in a project or a program of my own.
- [ ] **Compare alternatives:** I can name another way to solve the same problem (in Python, and in JS/TS or C++).
- [ ] **Identify trade-offs:** I can say when this is the *wrong* tool.

Record the result in [PROGRESS.md](../../../PROGRESS.md).

## 📊 Scoring for this stage (scheme A)

| Area | Weight |
|---|---:|
| Language knowledge | 20% |
| Coding exercises | 20% |
| Problem solving / algorithms | 15% |
| Debugging | 15% |
| Projects | 20% |
| Code design / architecture | 10% |
