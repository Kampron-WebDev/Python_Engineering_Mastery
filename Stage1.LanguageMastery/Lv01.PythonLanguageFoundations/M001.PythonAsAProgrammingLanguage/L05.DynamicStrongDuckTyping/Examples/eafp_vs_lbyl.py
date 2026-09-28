# Two ways to handle "might not work".   Run me:  python eafp_vs_lbyl.py

config = {"port": "8080"}

# LBYL: Look Before You Leap
if "port" in config and config["port"].isdigit():
    port = int(config["port"])
else:
    port = 8000
print("LBYL port:", port)

# EAFP: Easier to Ask Forgiveness than Permission (the Pythonic default)
try:
    port = int(config["port"])
except (KeyError, ValueError):
    port = 8000
print("EAFP port:", port)

# EAFP shines with duck typing: we don't care WHAT x is, only whether len() works.
for thing in ["abc", [1, 2], {"k": 1}, 42, None]:
    try:
        print(f"{thing!r:>10} has length {len(thing)}")
    except TypeError:
        print(f"{thing!r:>10} has no length")
