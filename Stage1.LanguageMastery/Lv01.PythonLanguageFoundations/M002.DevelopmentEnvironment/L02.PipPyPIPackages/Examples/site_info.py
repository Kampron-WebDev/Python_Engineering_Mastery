# Where do THIS Python's packages live, and what's installed?   Run me:  python site_info.py
import site
import sys
from importlib import metadata

print("Interpreter   :", sys.executable)
print("site-packages :", site.getsitepackages())

print("\nInstalled distributions:")
for dist in sorted(metadata.distributions(), key=lambda d: d.metadata["Name"].lower()):
    print(f"  {dist.metadata['Name']:<20} {dist.version}")

print("\nWhat does pytest depend on?")
for requirement in metadata.requires("pytest") or []:
    print("  ", requirement)
