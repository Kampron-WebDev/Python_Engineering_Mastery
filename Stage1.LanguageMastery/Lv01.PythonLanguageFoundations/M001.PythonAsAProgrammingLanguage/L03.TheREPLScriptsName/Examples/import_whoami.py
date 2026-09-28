# Run me:  python import_whoami.py
# Predict: which lines of whoami.py will print?

import whoami  # runs whoami.py's top-level code ONCE, with __name__ == 'whoami'

print("import_whoami.py can reuse its function:", whoami.shout("reuse"))
print("My own __name__ is", repr(__name__))
