import contextlib
import io

# Importing `this` prints the Zen once; we silence that so your program stays quiet.
with contextlib.redirect_stdout(io.StringIO()):
    import this


def rot13(text):
    """Shift every letter 13 places (keeping case); leave other characters alone."""
    # TODO: build it with ord() and chr(). No codecs, no this.d!
    pass


def zen_lines():
    """Decode this.s with rot13 and return the 19 aphorisms (no title, no blank lines)."""
    # TODO
    pass
