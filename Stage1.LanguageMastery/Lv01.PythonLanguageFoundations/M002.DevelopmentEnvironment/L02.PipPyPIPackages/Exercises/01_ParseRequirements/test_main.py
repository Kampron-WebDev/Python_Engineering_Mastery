# Run with:  python -m pytest

SAMPLE = """
# web stuff
Requests>=2.32   # http
Django_REST.framework==3.15
pytest ; python_version >= "3.12"
-r base.txt
--index-url https://example.org/simple

numpy ~= 2.1
"""


def test_normalize(main):
    assert main.normalize("Requests") == "requests"
    assert main.normalize("Django_REST.framework") == "django-rest-framework"
    assert main.normalize("a--b__c..d") == "a-b-c-d"


def test_parse_sample(main):
    assert main.parse_requirements(SAMPLE) == {
        "requests": ">=2.32",
        "django-rest-framework": "==3.15",
        "pytest": "",
        "numpy": "~=2.1",
    }


def test_empty(main):
    assert main.parse_requirements("") == {}
    assert main.parse_requirements("# only a comment\n\n") == {}


def test_other_operators(main):
    assert main.parse_requirements("urllib3!=2.0.0\nidna<4") == {"urllib3": "!=2.0.0", "idna": "<4"}
