# Dynamic + strong typing.   Run me:  python typing_tour.py   (predict each line first!)

x = 42
print("x is", type(x).__name__)
x = "forty-two"          # DYNAMIC: the same name now refers to a str. Totally allowed.
print("x is", type(x).__name__)

print("3" * 3)           # str * int is defined: repetition → '333'
print(3 + 4.5)           # int + float: numbers promote → 7.5
print(True + True)       # bool is a kind of int → 2

try:
    print("3" + 3)       # STRONG: no guessing between text and numbers
except TypeError as err:
    print("TypeError:", err)

print(int("3") + 3)      # be explicit instead → 6
print("3" + str(3))      # or → '33'

# Compare JavaScript, which is WEAKLY typed:  "3" + 3 → "33"  and  "3" * 3 → 9  (!)
