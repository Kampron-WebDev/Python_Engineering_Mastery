# Run with:  python -m pytest   (inside this folder)
# `main` is your main.py, imported for you by the course's conftest.py.


def test_course_name(main):
    assert main.course_name() == "Python Engineering Mastery"


def test_primary_languages_sorted(main):
    assert main.primary_languages() == ["C++", "Python", "TypeScript"]
