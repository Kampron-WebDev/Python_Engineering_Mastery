# Module 002: Development Environment

[🏠 Course](../../../README.md) · [Level I](../README.md) · [⬅ M001](../../../Stage1.LanguageMastery/Lv01.PythonLanguageFoundations/M001.PythonAsAProgrammingLanguage/README.md) · [M003 ➡](../../../Stage1.LanguageMastery/Lv01.PythonLanguageFoundations/M003.SyntaxAndProgramStructure/README.md)

**Stage 1 · Level I: Python Language Foundations** · Status: 🟢 Ready

## 🧸 The big idea

A professional Python setup is reproducible: the right interpreter, an isolated virtual environment per project, declared and locked dependencies, configuration from the environment, and a real debugger.

## 📖 Lessons

| # | Lesson | |
|---|---|---|
| 01 | [Installing Python & Managing Versions](L01.InstallingPythonManagingVersions/README.md) | 🟢 |
| 02 | [pip, PyPI & Packages](L02.PipPyPIPackages/README.md) | 🟢 |
| 03 | [Virtual Environments (venv)](L03.VirtualEnvironmentsVenv/README.md) | 🟢 |
| 04 | [pyproject.toml, uv & Poetry](L04.PyprojectTomlUvPoetry/README.md) | 🟢 |
| 05 | [Environment Variables & Configuration](L05.EnvironmentVariablesConfiguration/README.md) | 🟢 |
| 06 | [VS Code, IPython & the Debugger](L06.VSCodeIPythonTheDebugger/README.md) | 🟢 |
| 07 | [Module Review](L07.ModuleReview/README.md) | 🟢 |

Every lesson follows the 10-part format: Concept → Why it exists → Internal mechanics → Simple example → Real-world example → Coding exercise → Debugging challenge → Design question → Short assessment → Reflection.

## 🛠️ Build it yourself

- A version comparer that doesn't fall for '3.9' > '3.13'
- A requirements.txt parser
- A pyproject.toml reader with tomllib
- A typed settings loader from environment variables

## 🎯 Mastery gate

Reading a lesson is **not** finishing it. Tick every box, honestly:

- [ ] **Explain it:** I can answer every question below out loud, simply, without notes.
  - Why does every project get its own virtual environment?
  - What is a lockfile, and what problem does it solve that requirements ranges don't?
  - Why is `bool(os.getenv('DEBUG'))` a bug?
  - sys.prefix vs sys.base_prefix: what do they tell you?
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
