# Am I in a virtual environment?   Run me with different pythons (see the lesson).
import os
import site
import sys

in_venv = sys.prefix != sys.base_prefix
print("executable  :", sys.executable)
print("prefix      :", sys.prefix)
print("base_prefix :", sys.base_prefix)
print("in a venv?  :", "YES" if in_venv else "no, this is a base installation")
print("VIRTUAL_ENV :", os.environ.get("VIRTUAL_ENV", "(not set)"))
print("packages go :", site.getsitepackages()[-1])

cfg = os.path.join(sys.prefix, "pyvenv.cfg")
if os.path.exists(cfg):
    print("\npyvenv.cfg says:")
    with open(cfg, encoding="utf-8") as f:
        print("  " + f.read().strip().replace("\n", "\n  "))
