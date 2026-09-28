# Run with:  python -m pytest
import dis

RATE = 0.2


def add(a, b):
    return a + b


def tax(amount):
    return amount * RATE


def test_opnames_are_real_instructions(main):
    names = main.opnames(add)
    assert isinstance(names, list) and names
    assert all(name in dis.opmap for name in names)


def test_addition_uses_binary_op(main):
    assert "BINARY_OP" in main.opnames(add)


def test_opnames_keep_order(main):
    names = main.opnames(add)
    assert names == [ins.opname for ins in dis.get_instructions(add)]


def test_load_kinds_local_vs_global(main):
    kinds = main.load_kinds(tax)
    assert kinds == sorted(set(kinds)), "sorted and unique"
    assert "LOAD_GLOBAL" in kinds, "RATE is a global"
    assert any(k.startswith("LOAD_FAST") for k in kinds), "amount is a local"
    assert all(k.startswith("LOAD_") for k in kinds)
