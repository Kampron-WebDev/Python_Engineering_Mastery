# The truthy trap.   Run me (PowerShell):
#   $env:APP_DEBUG = "false"; python truthy_trap.py ; Remove-Item Env:APP_DEBUG
import os

raw = os.getenv("APP_DEBUG")
print("raw value        :", repr(raw))
print("bool(raw)        :", bool(raw), "  ← 'false' is a non-empty string, so it's True!")

TRUE_WORDS = {"1", "true", "yes", "on"}
print("parsed properly  :", (raw or "").strip().lower() in TRUE_WORDS)
