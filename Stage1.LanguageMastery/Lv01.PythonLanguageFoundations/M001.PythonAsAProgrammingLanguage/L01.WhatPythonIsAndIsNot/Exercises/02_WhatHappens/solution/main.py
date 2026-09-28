def what_happens(expression):
    try:
        value = eval(expression)  # learning tool only: never eval untrusted input!
    except Exception as err:
        return type(err).__name__
    return type(value).__name__


# The surprises, compared with JavaScript:
#   '3' * 3   → '333' (str repetition is DEFINED for str * int), while JS gives 9
#   '3' + 3   → TypeError (strong typing), while JS gives '33'
#   True + 1  → 2, because bool is a subclass of int (the one "implicit" numeric rule)
#   '5' == 5  → False, not an error: comparing different types for equality is allowed
