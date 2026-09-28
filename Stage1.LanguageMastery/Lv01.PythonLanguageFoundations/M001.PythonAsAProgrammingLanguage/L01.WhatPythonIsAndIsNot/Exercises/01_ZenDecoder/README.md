# Exercise 01: Zen Decoder

**Goal:** reveal the Zen of Python from its scrambled form, writing the decoder **yourself**.

The `this` module stores the Zen encoded with **ROT13**: every letter moves 13 places along the alphabet, wrapping around (`a→n`, `n→a`, `H→U`). Other characters stay the same. Because the alphabet has 26 letters, applying ROT13 twice gives back the original.

## Your task

### `rot13(text)`

```python
rot13("Hello")   # → "Uryyb"
rot13("Uryyb")   # → "Hello"
rot13("Hi, 42!") # → "Uv, 42!"   (only letters change; case is kept)
```

🚫 Don't use the `codecs` module or `this.d`: build it from `ord()` and `chr()`.

### `zen_lines()`

Decode `this.s` with your `rot13` and return **only the aphorisms**: every non-empty line **after** the title line (`"The Zen of Python, by Tim Peters"`).

```python
zen_lines()[0]    # → "Beautiful is better than ugly."
len(zen_lines())  # → 19
```

## Check your work

```powershell
python -m pytest
```

<details><summary>Hint 1: shifting one letter</summary>

`ord("a")` is 97. For a lowercase letter `c`: position = `ord(c) - ord("a")` (0–25), new position = `(position + 13) % 26`, back to a letter with `chr(new + ord("a"))`. Same idea for uppercase with `ord("A")`.

</details>

<details><summary>Hint 2: lines</summary>

`text.splitlines()` gives a list of lines. `line.strip()` is empty for blank lines. Slicing (`lines[1:]`) skips the first item.

</details>
