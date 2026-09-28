# Run me:  python main.py
# The folder of the script comes FIRST on sys.path, so `import random` finds ./random.py.
import random

try:
    print(random.randint(1, 6))
except AttributeError as err:
    print("AttributeError:", err)
    print("Fix: never name your files after standard-library modules (random, json, csv, statistics…).")
