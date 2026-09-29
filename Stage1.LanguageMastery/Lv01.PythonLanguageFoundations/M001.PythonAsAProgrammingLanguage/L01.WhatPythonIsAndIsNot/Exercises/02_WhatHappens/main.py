def what_happens(expression):
    """Evaluate expression; return the result's type name, or the raised exception's name."""
    # TODO: eval inside try/except
    try:
        value = eval(expression)
        return type(value).__name__
    except Exception as err:
        return type(err).__name__


# print(what_happens("3 + 3.5") )  # → 'float'
# print(what_happens("'3' + 3")  ) # → 'TypeError'
# print(what_happens("1 / 0") )     # → 'ZeroDivisionError'
