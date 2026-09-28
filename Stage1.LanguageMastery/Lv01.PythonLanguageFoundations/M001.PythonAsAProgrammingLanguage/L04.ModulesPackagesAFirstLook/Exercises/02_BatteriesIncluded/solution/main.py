import json
from collections import Counter
from datetime import date


def top_words(text, n):
    return Counter(text.lower().split()).most_common(n)


def days_between(start, end):
    return (date.fromisoformat(end) - date.fromisoformat(start)).days


def pretty_json(data):
    return json.dumps(data, indent=2, sort_keys=True)
