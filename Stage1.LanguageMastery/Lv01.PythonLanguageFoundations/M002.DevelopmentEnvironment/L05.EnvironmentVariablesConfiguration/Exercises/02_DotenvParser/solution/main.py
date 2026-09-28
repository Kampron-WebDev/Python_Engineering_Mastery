def _is_quoted(value):
    return len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'"


def parse_dotenv(text):
    result = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[len("export "):]
        key, sep, value = line.partition("=")
        if not sep:
            continue
        value = value.strip()
        if _is_quoted(value):
            value = value[1:-1]  # keep the inside exactly, including '#'
        else:
            value = value.split(" #")[0].strip()
        result[key.strip()] = value
    return result
