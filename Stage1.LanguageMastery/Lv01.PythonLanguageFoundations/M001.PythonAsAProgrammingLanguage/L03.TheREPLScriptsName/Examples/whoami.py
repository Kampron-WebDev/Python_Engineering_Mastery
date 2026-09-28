# Run me directly:     python whoami.py
# Or import me:        python import_whoami.py
# Or inspect after:    python -i whoami.py   (then type: greeting, shout("hi"), __name__)

print(f"whoami.py is running, and its __name__ is {__name__!r}")

greeting = "hello"


def shout(text):
    return text.upper() + "!"


if __name__ == "__main__":
    print("I was run DIRECTLY, so I do my main job:", shout(greeting))
