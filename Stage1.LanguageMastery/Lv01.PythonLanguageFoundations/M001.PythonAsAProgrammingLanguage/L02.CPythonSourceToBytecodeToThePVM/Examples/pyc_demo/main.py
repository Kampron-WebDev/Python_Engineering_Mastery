# Run me:  python main.py     then look in the __pycache__ folder that appears.
from pathlib import Path

import helper  # importing compiles helper.py and CACHES the bytecode

print(helper.shout("bytecode is cached"))

cache = Path(__file__).parent / "__pycache__"
print("\n__pycache__ contains:", [p.name for p in cache.glob("*.pyc")])
print("Notice: helper has a .pyc, main.py does NOT. The script you run directly isn't cached.")
print("The name includes the interpreter version (cpython-313), because bytecode changes between versions.")
