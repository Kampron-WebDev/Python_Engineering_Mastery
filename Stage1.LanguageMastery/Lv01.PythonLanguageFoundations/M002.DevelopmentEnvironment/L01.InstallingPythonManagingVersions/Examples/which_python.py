# Which Python is running me?   Run me:  python which_python.py   (then: py -3.12 which_python.py)
import os
import sys

print("executable    :", sys.executable)
print("version       :", sys.version.split()[0])
print("version_info  :", tuple(sys.version_info[:3]))
print("in a venv?    :", sys.prefix != sys.base_prefix)
print("VIRTUAL_ENV   :", os.environ.get("VIRTUAL_ENV", "(not set)"))

print("\nString comparison lies:   '3.9' > '3.13' =", "3.9" > "3.13")
print("Tuple comparison is right: (3, 9) > (3, 13) =", (3, 9) > (3, 13))

print("\nThe first entries on PATH (searched in this order):")
for folder in os.environ["PATH"].split(os.pathsep)[:6]:
    print("  ", folder)
