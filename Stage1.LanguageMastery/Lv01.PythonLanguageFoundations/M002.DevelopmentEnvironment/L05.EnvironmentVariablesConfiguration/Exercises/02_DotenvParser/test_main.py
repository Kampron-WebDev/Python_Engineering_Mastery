# Run with:  python -m pytest

SAMPLE = """
# local dev settings
DATABASE_URL=postgresql://localhost/quiz   # the local db
export SECRET_KEY="dev #not-a-comment"
EMPTY=
TOKEN=abc=def
   SPACED   =   value with spaces
SINGLE='single quoted'
this line has no equals sign
"""


def test_sample(main):
    assert main.parse_dotenv(SAMPLE) == {
        "DATABASE_URL": "postgresql://localhost/quiz",
        "SECRET_KEY": "dev #not-a-comment",
        "EMPTY": "",
        "TOKEN": "abc=def",
        "SPACED": "value with spaces",
        "SINGLE": "single quoted",
    }


def test_mismatched_quotes_are_kept(main):
    assert main.parse_dotenv("A=\"half") == {"A": "\"half"}


def test_empty_text(main):
    assert main.parse_dotenv("") == {}
    assert main.parse_dotenv("# nothing\n\n") == {}
