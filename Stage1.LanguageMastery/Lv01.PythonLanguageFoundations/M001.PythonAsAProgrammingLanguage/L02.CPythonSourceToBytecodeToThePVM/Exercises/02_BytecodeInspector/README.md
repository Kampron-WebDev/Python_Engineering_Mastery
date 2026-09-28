# Exercise 02: Bytecode Inspector

**Goal:** look at the actual instructions the Python Virtual Machine runs, and discover *why* local variables are faster than global ones.

## Your task

### `opnames(func)`

Return the list of **instruction names** in `func`'s bytecode, in order.

```python
def add(a, b):
    return a + b

opnames(add)   # → e.g. ['RESUME', 'LOAD_FAST_LOAD_FAST', 'BINARY_OP', 'RETURN_VALUE']
```

(The exact names differ slightly between Python versions. That's normal, and the tests allow for it.)

### `load_kinds(func)`

Return a **sorted list of the unique instruction names that start with `LOAD_`**.

```python
RATE = 0.2
def tax(amount):
    return amount * RATE

load_kinds(tax)   # contains 'LOAD_GLOBAL' (for RATE) and a 'LOAD_FAST…' (for amount)
```

## Useful tools

`dis.get_instructions(func)` yields instruction objects; each has an `.opname` string.
Try `import dis; dis.dis(tax)` in the REPL first.

## Check your work

```powershell
python -m pytest
```

**Think (MY-NOTES.md):** `LOAD_FAST` reads a slot in an array. `LOAD_GLOBAL` looks a name up in a dictionary (and then in the built-ins). Which is faster, and why? What does that mean for a hot loop that uses a global constant?
