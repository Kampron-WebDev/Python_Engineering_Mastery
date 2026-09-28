# Run with:  python -m pytest
import pytest

CASES = [
    ("PyYAML", "yaml"),
    ("pyyaml", "yaml"),
    ("scikit-learn", "sklearn"),
    ("Scikit_Learn", "sklearn"),
    ("Pillow", "PIL"),
    ("PILLOW", "PIL"),
    ("python.dateutil", "dateutil"),
    ("my-cool-lib", "my_cool_lib"),
    ("requests", "requests"),
]


@pytest.mark.parametrize(("distribution", "expected"), CASES)
def test_import_name(main, distribution, expected):
    assert main.import_name(distribution) == expected


def test_results_are_valid_identifiers(main):
    for distribution, _ in CASES:
        assert main.import_name(distribution).isidentifier()
