# Names are labels on objects.   Run me:  python names_and_objects.py

x = 42
print("x ->", type(x).__name__, "object with id", id(x))
x = "hi"                        # the LABEL moved to a new object
print("x ->", type(x).__name__, "object with id", id(x))

a = [1, 2]
b = a                           # two labels, ONE list
b.append(3)
print("a is b:", a is b, "| a =", a, "(changed through b!)")

c = [1, 2, 3]
print("a == c:", a == c, "| a is c:", a is c, "(equal value, different objects)")
print("isinstance(True, int):", isinstance(True, int), "| True + True =", True + True)
