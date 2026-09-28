# Run me from the package_demo folder:  python -m greetings.hello
def hello(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello("package"), "| my __name__ is", __name__, "| my package is", __package__)
