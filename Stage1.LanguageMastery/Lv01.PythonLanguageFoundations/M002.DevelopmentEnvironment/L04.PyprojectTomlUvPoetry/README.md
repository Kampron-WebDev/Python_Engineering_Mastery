# Lesson 04: pyproject.toml, uv & Poetry

[🏠 Course](../../../../README.md) · [Module 002](../README.md) · [⬅ Previous](../L03.VirtualEnvironmentsVenv/README.md) · [Next ➡](../L05.EnvironmentVariablesConfiguration/README.md)

**Module 002 · Lesson 04** · ⏱️ about 2 hours · Needs: Lessons 02–03

---

## 1. Concept

🧸 **Simple version: a shopping list and a receipt**

- **`pyproject.toml`** is the project's **shopping list**: "I need `requests`, version 2.32 or newer, and Python 3.12+."
- A **lockfile** (`uv.lock`, `poetry.lock`) is the **receipt**: *exactly* which versions were actually bought, including everything those packages needed, plus checksums proving nothing was swapped.

A shopping list says "milk". The receipt says "Brand X, 1 litre, batch 4471". To make the same meal again, you need the receipt.

🎓 **Precise version:**

- **`pyproject.toml`** (TOML format) is *the* standard project file: metadata (`[project]`, PEP 621), how to build it (`[build-system]`, PEP 518), dependency groups (`[dependency-groups]`, PEP 735) and tool settings (`[tool.pytest…]`, `[tool.ruff]`).
- **Direct dependencies** use *ranges* (`>=2.32`), so libraries stay flexible.
- A **lockfile** pins the **entire resolved dependency tree** (direct and transitive) to exact versions with hashes, so applications are reproducible.
- **uv** (fast, all-in-one: interpreters, venvs, resolving, locking, running) and **Poetry** are *project managers* that keep the venv, `pyproject.toml` and lockfile in sync.

## 2. Why it exists

`requirements.txt` + `pip` + `venv` works, but nothing ties them together: you forget to update the list, a transitive dependency releases a breaking change, and a deploy that worked yesterday fails today.
Modern tools solve three problems at once: **declare** (pyproject), **resolve and freeze** (lockfile), **reproduce** (sync the venv to the lockfile exactly).

## 3. Internal mechanics

### A realistic pyproject.toml

```toml
[project]
name = "quiz-api"
version = "0.3.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi>=0.115",
    "sqlalchemy>=2.0",
]

[dependency-groups]
dev = ["pytest>=8", "ruff"]

[tool.ruff]
line-length = 100
```

This course's own `pyproject.toml` (in the course root) is a real example. Open it!

### uv in five commands

```powershell
uv init quiz-api            # new project: pyproject.toml, .python-version, a sample file
uv add fastapi              # add a dependency → updates pyproject.toml AND uv.lock AND the venv
uv add --dev pytest         # into the dev dependency group
uv run pytest               # run a command inside the project's venv (created automatically)
uv sync                     # make .venv match uv.lock exactly (use this in CI and after git pull)
```

Plus: `uv python install 3.14` (manage interpreters), `uvx ruff check` (run a tool without installing it).

### Poetry equivalents

`poetry new`, `poetry add`, `poetry add --group dev`, `poetry run`, `poetry install` (→ `poetry.lock`). Same ideas, different tool. You'll meet both in real teams.

### Reading TOML from Python

Python 3.11+ ships **`tomllib`** (read-only):

```python
import tomllib
with open("pyproject.toml", "rb") as f:       # ⚠️ binary mode: TOML is defined as UTF-8 bytes
    data = tomllib.load(f)
data["project"]["requires-python"]            # keys keep their dashes!
```

## 4. Simple examples

```powershell
cd Examples
python read_course_pyproject.py      # read the real course pyproject.toml
uv --version                         # you have uv installed. Try the five commands in a scratch folder!
```

## 5. Real-world examples

- **Applications** (APIs, workers) commit their lockfile and deploy with `uv sync --frozen`, the exact same versions as in testing.
- **Libraries** (published packages) keep wide ranges in `dependencies`, so they don't fight their users' other packages.
- **CI caches** the resolved environment keyed on the lockfile's hash, which makes builds much faster.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [Read pyproject](Exercises/01_ReadPyproject/README.md) | `tomllib` + extracting project metadata |
| 2 | [Lock Check](Exercises/02_LockCheck/README.md) | Is every declared dependency in the lockfile? |

## 7. Debugging challenge

[TOML Troubles](Debugging/01_TomlTroubles/README.md): **2 bugs** everyone hits once with `tomllib`.

## 8. Design question

> Your team maintains **(a)** a web API deployed to production and **(b)** a small internal library other teams install.

In MY-NOTES.md: for each, would you commit a lockfile? Would you use exact pins or ranges in `dependencies`? Explain the difference between an *application* and a *library* here.

## 9. Short assessment

1. What goes in `[project]`, `[dependency-groups]` and `[tool.*]`?
2. Shopping list vs receipt: which is `pyproject.toml`, which is the lockfile?
3. What does `uv sync` do?
4. Why must `tomllib.load` get a file opened in binary mode?
5. Why do libraries avoid exact pins?

<details><summary>Answers</summary>

1. Project metadata and runtime dependencies; optional groups such as dev tools; configuration for tools like pytest or Ruff.
2. `pyproject.toml` is the shopping list (declared ranges); the lockfile is the receipt (exact resolved versions and hashes).
3. It makes the project's venv match the lockfile exactly, adding and removing packages as needed.
4. TOML is defined as UTF-8 bytes, so `tomllib` decodes it itself and refuses text-mode files (`TypeError`).
5. Exact pins would conflict with other packages the user installs; ranges let the resolver find a combination that works.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain a lockfile to a 10-year-old.
- Compare with `package.json` + `package-lock.json` from your JS course.
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| `pyproject.toml` | The standard project configuration file |
| TOML | A simple, strict config-file format |
| Direct vs transitive dependency | What you asked for vs what *they* need |
| Lockfile | Exact versions and hashes of the full dependency tree |
| uv / Poetry | Project managers: venv + resolving + locking + running |
| `tomllib` | Standard-library TOML reader (3.11+) |

## ✅ Done when

- [ ] I read the course `pyproject.toml` and ran the example
- [ ] I tried `uv init` / `uv add` / `uv run` in a scratch folder
- [ ] Both exercises are green
- [ ] Both TOML bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
