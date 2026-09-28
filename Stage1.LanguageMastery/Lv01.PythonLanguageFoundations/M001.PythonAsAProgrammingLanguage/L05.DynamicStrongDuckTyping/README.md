# Lesson 05: Dynamic, Strong & Duck Typing

[🏠 Course](../../../../README.md) · [Module 001](../README.md) · [⬅ Previous](../L04.ModulesPackagesAFirstLook/README.md) · [Next ➡](../L06.ModuleReview/README.md)

**Module 001 · Lesson 05** · ⏱️ about 2 hours · Needs: Lessons 01–04

---

## 1. Concept

🧸 **Simple version: name tags and job interviews**

- **Names are sticky labels, not boxes.** `x = 42` sticks the label `x` on the object `42`. Later `x = "hi"` peels it off and sticks it on a string. The *label* never had a type; the *objects* do. That's **dynamic typing**.
- **Objects don't pretend to be something else.** Python won't quietly turn the text `"3"` into the number 3 because you tried to add them. It stops and complains. That's **strong typing**.
- **Python hires by skills, not by job title.** A function that needs "something I can loop over" accepts a list, a tuple, a file or a generator, anything that *can do the job*. "If it walks like a duck and quacks like a duck, it's a duck." That's **duck typing**.

🎓 **Precise version:**

| | Checked when? | Implicit conversions between unrelated types? |
|---|---|---|
| **Python** | Dynamic: at runtime, on objects | No: **strong** (only numeric promotion `bool → int → float → complex`) |
| **JavaScript** | Dynamic | Yes: **weak** (`"3" * 3 === 9`) |
| **C++** | Static: at compile time, on variables | Some implicit numeric conversions, otherwise strict |
| **TypeScript / Python + type hints** | Static checker *on top* of a dynamic runtime | (the runtime is unchanged) |

- **Duck typing:** code relies on an object's **behaviour** (methods and protocols like "iterable", "has `len`"), not its declared type.
- **EAFP**, "Easier to Ask Forgiveness than Permission": just try the operation and catch the exception. That's the Pythonic default.
- **LBYL**, "Look Before You Leap": check first (`if hasattr(x, "read")`). Useful sometimes, but racy and verbose.

## 2. Why it exists

Dynamic typing makes Python quick to write and extremely flexible: the same function works on many kinds of objects without templates or interfaces.
Strong typing keeps that flexibility **safe**: mistakes like `"3" + 3` fail immediately and loudly instead of producing `"33"` three functions later.
Duck typing is what makes Python's ecosystem compose so well: your class works with `for`, `len()`, `sorted()`, `with` and more, just by implementing the right methods (Module 025).

The cost: type errors only appear **when that line runs**. In large codebases that's why we add **type hints plus a static checker** (Level VIII), which gets you TypeScript-style safety on top of Python's dynamic runtime.

## 3. Internal mechanics

### Every object carries its type

```python
x = 42
type(x)            # <class 'int'>. The OBJECT knows its type
x = "hi"           # the name moved; 42 didn't change
isinstance(True, int)   # True! bool is a subclass of int
```

### Checking types: three tools, three meanings

| Check | Means | When to use |
|---|---|---|
| `type(x) is int` | Exactly `int`, not a subclass | Rare: when subclasses (like `bool`) must be excluded |
| `isinstance(x, int)` | `int` or any subclass | When you really need a *kind* of thing |
| *just use it* (EAFP) | "Can it do what I need?" | **The default in Python** |

For behaviour-based checks there are **abstract base classes** in `collections.abc`: `isinstance(x, Iterable)`, `Sized`, `Mapping`…

### Identity vs equality

```python
a == b    # equal VALUE: asks the objects (calls a.__eq__(b)), which can be customised
a is b    # SAME OBJECT: compares identity and can't be fooled
x is None # the correct way to test for None, always
```

### Type hints are not enforced at runtime

```python
def double(n: int) -> int:
    return n * 2

double("ha")   # 'haha': Python doesn't stop this! Hints are for tools (Level VIII).
```

## 4. Simple examples

```powershell
cd Examples
python names_and_objects.py   # labels moving between objects
python eafp_vs_lbyl.py        # the two styles side by side
python duck.py                # one function, many duck types
```

## 5. Real-world examples

- **File-like objects:** `json.load(f)` works on a real file, an in-memory `io.StringIO`, or a network response: anything with a `.read()` method.
- **pandas and NumPy** accept lists, tuples, generators, other arrays… duck typing at massive scale.
- **Web frameworks** (FastAPI, Level XIV) *use* type hints to validate incoming data at runtime via Pydantic, which bridges the static and dynamic worlds.

## 6. Coding exercises

| # | Exercise | Skill |
|---|---|---|
| 1 | [Type Table](Exercises/01_TypeTable/README.md) | Predicting what `a + b` does across types |
| 2 | [Duck Total](Exercises/02_DuckTotal/README.md) | EAFP: working with anything that has a length |

## 7. Debugging challenge

[Identity Crisis](Debugging/01_IdentityCrisis/README.md): **2 bugs** about `bool` being an `int`, and `==` vs `is`.

## 8. Design question

> You're designing `export_report(destination)`. Callers want to pass a file path (`str`), a `pathlib.Path`, an open file, or an in-memory buffer.

In MY-NOTES.md: would you use duck typing, `isinstance` checks, or separate functions? What would the error look like for an invalid destination? How would type hints document your decision (you can guess the syntax for now)?

## 9. Short assessment

1. Dynamic vs static typing, and strong vs weak: where do Python, JS and C++ sit?
2. Why is `isinstance(True, int)` true, and when does that matter?
3. EAFP vs LBYL, with a one-line example of each.
4. Why must you write `x is None` and not `x == None`?
5. Does Python enforce `def f(n: int)` at runtime?

<details><summary>Answers</summary>

1. Python: dynamic + strong. JS: dynamic + weak. C++: static + (mostly) strong.
2. `bool` is a subclass of `int`. It matters in validation: `isinstance(age, int)` accepts `True` as an age.
3. EAFP: `try: n = len(x) except TypeError: ...`. LBYL: `if hasattr(x, "__len__"): n = len(x)`.
4. `==` calls the object's `__eq__`, which a class can override (even to always return True); `is` checks identity and can't be fooled. `None` is a single, unique object.
5. No. Hints are ignored at runtime; static checkers (and some libraries) use them.

</details>

## 10. Reflection

In MY-NOTES.md:

- Explain duck typing to a 10-year-old (the job interview, or your own).
- Where did C++'s static typing save you from a bug? Where would Python's flexibility have saved time?
- What is still fuzzy?

## 🔑 Key words

| Word | Meaning |
|---|---|
| Dynamic typing | Types live on objects; checked at runtime |
| Strong typing | No implicit conversion between unrelated types |
| Duck typing | Relying on behaviour, not declared type |
| EAFP / LBYL | Try-and-catch vs check-first |
| Identity (`is`) | Same object |
| Equality (`==`) | Equal value, as defined by the objects |
| Type hint | An annotation for tools; not enforced at runtime |

## ✅ Done when

- [ ] I ran all three examples
- [ ] Both exercises are green (predictions first)
- [ ] Both identity bugs fixed and explained
- [ ] Design question, quiz and reflection in MY-NOTES.md
- [ ] Committed
