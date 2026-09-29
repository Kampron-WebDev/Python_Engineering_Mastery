import contextlib
import io

# Importing `this` prints the Zen once; we silence that so your program stays quiet.
with contextlib.redirect_stdout(io.StringIO()):
    import this


def rot13(text):
    """Shift every letter 13 places (keeping case); leave other characters alone."""
    # TODO: build it with ord() and chr(). No codecs, no this.d!

    result = []

    for character in text:
        number = ord(character)
        if "a" <= character <= "z":
            new_number = (number - ord("a") + 13) % 26 + ord("a")
            result.append(chr(new_number))

        elif "A" <= character <= "Z":
            new_number = (number - ord("A") + 13) % 26 + ord("A")
            result.append(chr(new_number))

        else:
            result.append(character)
    return "".join(result)


            



def zen_lines():
    """Decode this.s with rot13 and return the 19 aphorisms (no title, no blank lines)."""
    # TODO
    decoded = rot13(this.s)

    lines = decoded.splitlines()

    title = "The Zen of Python, by Tim Peters" 

    title_position = lines.index(title)

    aphorisms = []

    for line in lines[title_position + 1:]:
        if line.strip():
            aphorisms.append(line)

    return aphorisms



# print(rot13("Hello"))       # Uryyb
# print(rot13("Uryyb"))       # Hello
# print(rot13("Hi, 42!"))     # Uv, 42!

# print(zen_lines()[0])       # Beautiful is better than ugly.
# print(len(zen_lines()))     # 19




