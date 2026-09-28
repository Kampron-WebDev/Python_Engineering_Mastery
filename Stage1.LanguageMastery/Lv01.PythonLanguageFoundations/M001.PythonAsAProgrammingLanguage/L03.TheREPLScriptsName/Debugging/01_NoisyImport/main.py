# ⚠️ 2 bugs: importing this file must be silent, and countdown must RETURN its text.


def countdown(n):
    """countdown(3) → '3... 2... 1... Liftoff!'"""
    parts = [f"{i}..." for i in range(n, 0, -1)]
    print(" ".join(parts + ["Liftoff!"]))


print("🚀 Launch sequence starting!")
countdown(10)
