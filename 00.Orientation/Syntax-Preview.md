# 🧰 Syntax Preview: Python next to JavaScript and C++

[⬅ Orientation](README.md)

Module 001 uses a little syntax before Modules 003–018 teach it properly (with all the "why"). You already know some C++ and JavaScript, so here's Python beside them.

> 🧸 C++ is building furniture from raw wood. JavaScript is IKEA. Python is IKEA where the instructions are written in almost-plain English, and **indentation is part of the instructions**.

## Blocks: indentation, not braces

```python
if age >= 18:          # colon starts a block
    print("adult")     # 4 spaces = inside the block
else:
    print("minor")
print("done")          # back out = outside the block
```

No `{ }`, no `;`. Wrong indentation is a **syntax error**, not a style issue.

## Side by side

| Idea | Python | JavaScript | C++ |
|---|---|---|---|
| Variable | `name = "Ama"` | `const name = 'Ama'` | `std::string name = "Ama";` |
| Print | `print("Hi", name)` | `console.log('Hi', name)` | `std::cout << "Hi " << name;` |
| Formatted string | `f"Hi {name}"` | `` `Hi ${name}` `` | `std::format("Hi {}", name)` |
| Function | `def add(a, b):` then `return a + b` | `function add(a, b) { return a + b }` | `int add(int a, int b) { return a + b; }` |
| Lambda | `lambda x: x * 2` | `x => x * 2` | `[](int x){ return x * 2; }` |
| Boolean | `True` / `False` | `true` / `false` | `true` / `false` |
| Nothing | `None` | `null` / `undefined` | `nullptr` |
| And / or / not | `and` / `or` / `not` | `&&` / `\|\|` / `!` | `&&` / `\|\|` / `!` |
| Equality | `==` (value) · `is` (same object) | `===` | `==` |
| Integer division | `7 // 2` → `3` | `Math.floor(7 / 2)` | `7 / 2` (ints) |
| Power | `2 ** 10` | `2 ** 10` | `std::pow(2, 10)` |
| List / array | `nums = [3, 1, 2]` | `const nums = [3, 1, 2]` | `std::vector<int> nums{3, 1, 2};` |
| Dict / object | `user = {"name": "Kofi"}` → `user["name"]` | `{ name: 'Kofi' }` → `user.name` | `std::map<std::string, std::string>` |
| Loop over items | `for n in nums:` | `for (const n of nums)` | `for (int n : nums)` |
| Counting loop | `for i in range(3):` | `for (let i = 0; i < 3; i++)` | `for (int i = 0; i < 3; ++i)` |
| Length | `len(nums)` | `nums.length` | `nums.size()` |
| Error | `raise ValueError("bad")` | `throw new Error('bad')` | `throw std::invalid_argument("bad");` |
| Catch | `try:` … `except ValueError as e:` | `try {} catch (e) {}` | `try {} catch (const std::exception& e) {}` |
| Import | `from money import format_money` | `import { formatMoney } from './money.js'` | `#include "money.h"` |
| Comment | `# like this` | `// like this` | `// like this` |

## Naming style (PEP 8)

`snake_case` for variables and functions, `PascalCase` for classes, `UPPER_CASE` for constants. (JavaScript uses `camelCase`; Python doesn't.)

## Docstrings

A string on the first line of a function *documents* it, and `help(fn)` shows it:

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```

## `pass` and `...`

A block can't be empty, so starter code uses `pass` (do nothing) or `...` as a placeholder. That's why an unfinished exercise function returns `None`.

That's enough to begin. ➡ [Back to Orientation](README.md)
