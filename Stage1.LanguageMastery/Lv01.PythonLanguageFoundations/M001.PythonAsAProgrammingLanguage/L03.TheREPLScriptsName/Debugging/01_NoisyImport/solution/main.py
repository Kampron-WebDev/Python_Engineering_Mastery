def countdown(n):
    parts = [f"{i}..." for i in range(n, 0, -1)]
    # Bug 2: print SHOWS the text; return GIVES it to the caller (who received None before).
    return " ".join(parts + ["Liftoff!"])


# Bug 1: top-level code runs on EVERY import. The guard makes it run only when this
# file is executed directly (python main.py), where __name__ == "__main__".
if __name__ == "__main__":
    print("🚀 Launch sequence starting!")
    print(countdown(10))
