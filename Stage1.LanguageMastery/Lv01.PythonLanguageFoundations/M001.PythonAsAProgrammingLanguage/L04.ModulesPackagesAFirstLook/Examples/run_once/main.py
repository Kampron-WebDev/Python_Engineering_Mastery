# Run me:  python main.py
# Predict: how many times does "counter.py is being executed" print? What do a and b print?
import sys

import a
import b

print("main.py: counter is cached in sys.modules?", "counter" in sys.modules)
# Answer: counter.py runs ONCE. a and b share the same module object, so the same count: 1, then 2.
