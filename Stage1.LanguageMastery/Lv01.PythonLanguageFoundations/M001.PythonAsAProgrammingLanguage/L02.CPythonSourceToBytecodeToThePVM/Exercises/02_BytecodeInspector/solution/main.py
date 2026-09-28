import dis


def opnames(func):
    return [instruction.opname for instruction in dis.get_instructions(func)]


def load_kinds(func):
    return sorted({name for name in opnames(func) if name.startswith("LOAD_")})


# Think-about-it: LOAD_FAST indexes straight into the frame's array of local variables.
# LOAD_GLOBAL has to look the name up in the module's dict (and fall back to builtins).
# In a hot loop, copying a global into a local first (rate = RATE) can measurably help,
# but measure before "optimising" (Level XIX).
