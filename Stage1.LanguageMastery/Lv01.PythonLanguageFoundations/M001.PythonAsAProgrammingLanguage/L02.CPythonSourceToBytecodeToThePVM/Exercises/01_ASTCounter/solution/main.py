import ast


def count_nodes(source):
    counts = {}
    for node in ast.walk(ast.parse(source)):  # ast.parse raises SyntaxError for bad code
        name = type(node).__name__
        counts[name] = counts.get(name, 0) + 1
    return counts


def names_used(source):
    names = {node.id for node in ast.walk(ast.parse(source)) if isinstance(node, ast.Name)}
    return sorted(names)
