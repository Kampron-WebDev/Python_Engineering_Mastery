# A peek at your process's environment.   Run me:  python show_env.py
import os

for name in ["USERNAME", "COMPUTERNAME", "OS", "VIRTUAL_ENV", "PYTHONPATH", "APP_PORT"]:
    print(f"{name:<14} = {os.environ.get(name, '(not set)')}")

print("\nTotal variables:", len(os.environ))
print("Every value is a str:", all(isinstance(v, str) for v in os.environ.values()))
