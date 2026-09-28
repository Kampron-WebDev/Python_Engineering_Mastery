# Debugging 01: Truthy Trap

Two tiny config helpers caused a real incident: production ran with **debug mode on**, and a health check compared the port with an integer and failed.

```python
get_debug({"DEBUG": "false"})   # → False   (it returned True!)
get_debug({})                   # → False
get_port({"PORT": "8080"})      # → 8080    (an int, not "8080")
get_port({})                    # → 8000
```

There are **2 bugs**.

## Your task

1. `python -m pytest`.
2. Fix both. In MY-NOTES.md: explain why `bool("false")` is `True`, and why `get_port` returned an `int` in one environment and a `str` in another.

<details><summary>Hint 2</summary>

`env.get("PORT", 8000)`: what's the type of the default? What's the type of a value that *was* set?

</details>
