# Run with:  python -m pytest   (inside this folder)
# `main` is your main.py (or solution/main.py when checking solutions). See conftest.py.


def test_fn_doubles_a_number(main):
    assert main.fn(1) == 2
