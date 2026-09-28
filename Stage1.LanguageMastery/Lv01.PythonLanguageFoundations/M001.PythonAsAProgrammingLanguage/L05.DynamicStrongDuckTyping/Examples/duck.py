# One function, many "ducks".   Run me:  python duck.py
import io


def count_lines(source):
    """Counts lines in ANYTHING you can iterate over line by line."""
    return sum(1 for _ in source)


print(count_lines(["a", "b", "c"]))                       # a list
print(count_lines(io.StringIO("x\ny\n")))                 # an in-memory "file"
with open(__file__, encoding="utf-8") as this_file:
    print(count_lines(this_file))                         # a real file (this one!)
print(count_lines(line for line in "p\nq".splitlines()))  # a generator
# count_lines never asked "are you a list?". It only needed to LOOP. That's duck typing.
