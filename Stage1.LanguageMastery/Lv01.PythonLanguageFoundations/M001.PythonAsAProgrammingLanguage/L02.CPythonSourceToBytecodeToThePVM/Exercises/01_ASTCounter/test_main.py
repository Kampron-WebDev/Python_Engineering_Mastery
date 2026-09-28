# Run with:  python -m pytest
import pytest


def test_simple_assignment(main):
    counts = main.count_nodes("x = 1 + 2")
    assert counts["Module"] == 1
    assert counts["Assign"] == 1
    assert counts["BinOp"] == 1
    assert counts["Constant"] == 2
    assert counts["Name"] == 1


def test_function_definition(main):
    counts = main.count_nodes("def f(a):\n    return a * 2\n")
    assert counts["FunctionDef"] == 1
    assert counts["Return"] == 1
    assert counts["BinOp"] == 1


def test_names_used(main):
    assert main.names_used("total = price * qty + price") == ["price", "qty", "total"]
    assert main.names_used("print(len(items))") == ["items", "len", "print"]
    assert main.names_used("42") == []


def test_invalid_source_raises_syntax_error(main):
    with pytest.raises(SyntaxError):
        main.count_nodes("x = = 1")
