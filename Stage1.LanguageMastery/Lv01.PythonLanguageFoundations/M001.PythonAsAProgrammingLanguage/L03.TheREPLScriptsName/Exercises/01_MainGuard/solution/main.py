import sys


def summarize(numbers):
    total = sum(numbers)
    return f"count={len(numbers)} total={total} mean={total / len(numbers):.1f}"


def main(argv):
    if not argv:
        print("error: give me some numbers", file=sys.stderr)
        return 1

    numbers = []
    for arg in argv:
        try:
            numbers.append(float(arg) if "." in arg else int(arg))
        except ValueError:
            print(f"error: not a number: {arg}", file=sys.stderr)
            return 1

    print(summarize(numbers))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
