import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()):
    import this


def _shift(char, base):
    return chr((ord(char) - base + 13) % 26 + base)


def rot13(text):
    result = []
    for char in text:
        if "a" <= char <= "z":
            result.append(_shift(char, ord("a")))
        elif "A" <= char <= "Z":
            result.append(_shift(char, ord("A")))
        else:
            result.append(char)
    return "".join(result)  # joining a list is faster than += on strings (Module 005)


def zen_lines():
    lines = rot13(this.s).splitlines()
    return [line for line in lines[1:] if line.strip()]
