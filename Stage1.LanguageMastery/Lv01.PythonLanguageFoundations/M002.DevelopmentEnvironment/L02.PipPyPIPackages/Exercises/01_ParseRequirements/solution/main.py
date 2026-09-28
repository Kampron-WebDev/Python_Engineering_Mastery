import re


def normalize(name):
    return re.sub(r"[-_.]+", "-", name).lower()


def _split(requirement):
    for index, char in enumerate(requirement):
        if char in "<>=!~":
            return requirement[:index].strip(), requirement[index:].strip()
    return requirement.strip(), ""


def parse_requirements(text):
    result = {}
    for raw in text.splitlines():
        line = raw.split(" #")[0].split(";")[0].strip()
        if not line or line.startswith(("#", "-")):
            continue
        name, specifier = _split(line)
        result[normalize(name)] = specifier.replace(" ", "")
    return result
