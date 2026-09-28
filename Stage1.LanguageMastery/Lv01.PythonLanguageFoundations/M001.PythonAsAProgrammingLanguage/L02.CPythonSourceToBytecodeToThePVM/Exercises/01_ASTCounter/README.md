# Exercise 01: AST Counter

**Goal:** see your code the way the compiler sees it, as a **tree of nodes**, using the standard-library `ast` module.

## Your task

### `count_nodes(source)`

Parse `source` and return a **dict** mapping each node type's name to how many times it appears.

```python
counts = count_nodes("x = 1 + 2")
counts["Assign"]    # → 1
counts["BinOp"]     # → 1
counts["Constant"]  # → 2
counts["Name"]      # → 1
```

### `names_used(source)`

Return a **sorted list of the unique variable names** the code mentions (every `ast.Name` node's `.id`).

```python
names_used("total = price * qty + price")  # → ['price', 'qty', 'total']
```

## Useful tools

- `ast.parse(source)` returns the tree.
- `ast.walk(tree)` yields **every** node in it, in no particular order.
- `type(node).__name__` gives a node's type name, like `'BinOp'`.
- `isinstance(node, ast.Name)` checks for name nodes; `node.id` is the name.

Try `print(ast.dump(ast.parse("x = 1 + 2"), indent=2))` in the REPL first, to *see* the tree.

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint</summary>

The counting pattern: `counts[key] = counts.get(key, 0) + 1`. (Later you'll meet `collections.Counter`, which does this for you.)

</details>
