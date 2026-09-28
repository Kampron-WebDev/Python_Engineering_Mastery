# The Zen of Python, and a secret.   Run me:  python zen.py

import this  # importing it PRINTS the Zen (a side effect of running the module once)

print("\n" + "─" * 60)
print("But inside the module, the text is stored scrambled:\n")
print(this.s[:120], "…")
print("\nThe module un-scrambles it with a lookup table, this.d:")
print({k: this.d[k] for k in "abcHello"})
print("\nThat's ROT13: every letter is shifted 13 places. You'll write your own decoder today.")
