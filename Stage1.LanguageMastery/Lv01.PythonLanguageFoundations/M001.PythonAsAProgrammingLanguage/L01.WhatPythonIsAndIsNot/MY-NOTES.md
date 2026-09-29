# My Notes

The surprises, compared with JavaScript:
'3' \* 3 → '333' (str repetition is DEFINED for str \_ int), while JS gives 9
'3' + 3 → TypeError (strong typing), while JS gives '33'
True + 1 → 2, because bool is a subclass of int (the one "implicit" numeric rule)
'5' == 5 → False, not an error: comparing different types for equality is allowed

## Duck Typing

Duck typing means Python cares about what an object can do, not its exact type.

> “If it walks like a duck and quacks like a duck, treat it like a duck.”

Avoid:

```python
if type(x) == list:
```

This is usually un-Pythonic because it rejects tuples, sets, generators, and custom objects that can do the same job.

Prefer using the object directly:

```python
for item in x:
    print(item)
```

Use `isinstance(x, list)` only when you specifically require a list or list subclass.

## Design question (my answer)

## Language Choices

| Product part           | Choice               | Strength                                                                           | Weakness                                              |
| ---------------------- | -------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Web dashboard          | TypeScript           | Excellent for interactive web interfaces.                                          | More complex than JavaScript for beginners.           |
| API                    | Python or TypeScript | Python is quick to develop; TypeScript gives strong type checking.                 | Python can be slower; TypeScript requires more setup. |
| Nightly 50 GB data job | Python + C++         | Python handles the workflow; C++ provides high performance for heavy calculations. | C++ is harder and slower to develop.                  |
| ML failure prediction  | Python               | Best ecosystem for machine learning libraries and experimentation.                 | Usually slower than C++ for raw computation.          |

### Overall choice

Use a mix:

- TypeScript for the dashboard
- Python or TypeScript for the API
- Python for data orchestration
- C++ only for performance-critical processing
- Python for the ML model

## Quiz: my answers before checking

1. **Dynamically typed:** You do not declare a variable’s type; Python discovers it while running.

   ```python
   x = 10
   x = "hello"
   ```

   **Strongly typed:** Python does not silently mix incompatible types.

   ```python
   "3" + 3  # TypeError
   ```

2. **CPython:** The main implementation of Python, written mostly in C. It translates and runs Python code.

3. **Why NumPy is fast:** NumPy moves heavy looping into optimized C or Fortran code. Python starts the operation, but the slow Python loop happens outside Python.

4. **PEP:** Python Enhancement Proposal—a document suggesting or describing a Python feature, rule, or standard.

   Famous examples:
   - PEP 8: Python style guide
   - PEP 20: The Zen of Python

5. **Release schedule:** A new major Python version comes out about once a year, usually in October. Each version is supported for roughly five years: about two years of regular fixes and three years of security fixes. [PEP 602](https://peps.python.org/pep-0602/), [Python Developer Guide](https://devguide.python.org/versions/)

## Reflection

**Explain it to a 10-year-old:**

### Dynamic typing

Python figures out the type of a value while the program is running.

```python
box = 10
box = "hello"
```

The same `box` can hold a number first and text later. You do not need to declare its type.

### Strong typing

Python does not automatically mix unrelated types.

```python
"3" + 3
```

This causes an error because `"3"` is text and `3` is a number.

You must convert the text yourself:

```python
int("3") + 3  # 6
```

A simple way to remember:

- **Dynamic:** A box can hold different kinds of things at different times.
- **Strong:** Python does not pretend different kinds of things are the same.

**What surprised me:** Indentations in python and how simple it looks

**Still fuzzy:**
