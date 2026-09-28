# Lesson 05: Environment Variables & Configuration

[🏠 Course](../../../../README.md) · [Module 002](../README.md) · [⬅ Previous](../L04.PyprojectTomlUvPoetry/README.md) · [Next ➡](../L06.VSCodeIPythonTheDebugger/README.md)

**Module 002 · Lesson 05** · ⏱️ about 1.5–2 hours · Needs: Lessons 01–04

---

## 1. Concept

🧸 **Simple version:**
A program is like a **travelling chef**. The recipes (the code) stay the same everywhere, but each kitchen has different settings: which oven, which supplier, the Wi-Fi password. Instead of writing those into the recipe book, each kitchen leaves a **note on the door**, and the chef reads it on arrival.
**Environment variables** are those notes on the door.

🎓 **Precise version:**
**Environment variables** are key–value **strings** that every process receives from its parent (your shell, VS Code, Docker, the cloud platform). In Python they're in **`os.environ`**, a mapping of `str → str`.

```python
import os
os.environ["DATABASE_URL"]            # KeyError if missing: good for REQUIRED settings
os.environ.get("PORT", "8000")        # default if missing: good for OPTIONAL settings
os.getenv("PORT")                     # same as .get → None if missing
```

**Everything is a string.** `PORT=8080` arrives as `"8080"`; `DEBUG=false` arrives as the *non-empty*, truthy string `"false"`. Converting and validating is **your** job.

## 2. Why it exists

The same code must run on your laptop, in CI, in staging and in production, with different databases, secrets and settings. Hard-coding them means editing code per environment (dangerous) and committing **secrets** to Git (a security incident).
The **Twelve-Factor App** rule: *store config in the environment.* Code is identical everywhere; only the environment changes.

## 3. Internal mechanics

### Setting variables

```powershell
$env:APP_PORT = "8080"          # PowerShell: this terminal only (and processes it starts)
python -c "import os; print(os.environ['APP_PORT'])"
Remove-Item Env:APP_PORT        # unset
```

```bash
export APP_PORT=8080            # bash / zsh
APP_PORT=8080 python app.py     # just for one command
```

Children **inherit** a *copy* of the parent's environment. A child can't change its parent's variables.

### `.env` files

A `.env` file lists variables for local development:

```text
# .env (never commit this!)
DATABASE_URL=postgresql://localhost/quiz
DEBUG=true
export SECRET_KEY="dev-only-secret"
```

Python does **not** read `.env` automatically. A library (`python-dotenv`, or your framework) loads it into the environment at start-up. Commit a **`.env.example`** with fake values instead, so teammates know what's needed. (This course's `.gitignore` already blocks `.env`.)

### Load, convert, validate: once, at start-up

The professional pattern: read **all** configuration in one place when the program starts, convert types, validate, and **fail fast** with a clear message listing *everything* that's wrong, rather than crashing an hour later on the first request that needs a missing value. (Level XIV does this with Pydantic Settings.)

## 4. Simple examples

```powershell
cd Examples
python show_env.py                          # a few real variables from your machine
$env:APP_DEBUG = "false"; python truthy_trap.py ; Remove-Item Env:APP_DEBUG
```

## 5. Real-world examples

- **Docker / Kubernetes / cloud platforms** inject configuration and secrets as environment variables.
- **Secrets managers** (AWS Secrets Manager, Vault) often deliver secrets into the environment at start-up.
- A classic production incident: `DEBUG=false` read with `bool(os.getenv("DEBUG"))` → debug mode **on** in production, leaking stack traces to users. Today's debugging challenge.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [Settings Loader](Exercises/01_SettingsLoader/README.md) | Convert, validate, fail fast with every error at once |
| 2 | [Dotenv Parser](Exercises/02_DotenvParser/README.md) | Parsing `.env` files by hand |

## 7. Debugging challenge

[Truthy Trap](Debugging/01_TruthyTrap/README.md): the production-incident bug, plus a type that changes depending on the environment. **2 bugs**.

## 8. Design question

> Your API needs: a database URL, a secret key, a port, a debug flag, a list of allowed origins, and an API key for a payment provider.

In MY-NOTES.md: which are **required**, which have safe **defaults**, and which are **secrets**? How would you represent the list of origins in a single environment variable? What should happen if the secret key is missing in production but present in development?

## 9. Short assessment

1. What type are environment variable values in Python?
2. `os.environ["X"]` vs `os.environ.get("X")`: when would you use each?
3. Why is `bool(os.getenv("DEBUG"))` wrong?
4. Does Python read `.env` files automatically?
5. Why validate all configuration at start-up?

<details><summary>Answers</summary>

1. Always `str`.
2. `[...]` for required settings (fail loudly if missing); `.get()` for optional ones with a default.
3. Any non-empty string is truthy, so `"false"` and `"0"` become `True`.
4. No. A library or framework must load it.
5. To fail fast with one clear report, instead of crashing later at an unpredictable moment.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain environment variables to a 10-year-old (the note on the door, or your own).
- Where did your JS course use `process.env`? What's the same?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| Environment variable | A key–value string passed to a process by its parent |
| `os.environ` | Python's mapping of the environment |
| `.env` file | A local file of variables for development (never committed) |
| Twelve-Factor App | Principles for cloud apps, including "config in the environment" |
| Fail fast | Stop immediately with a clear error when something is wrong |

## ✅ Done when

- [ ] I ran both examples, including the truthy trap
- [ ] Both exercises are green
- [ ] Both configuration bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
