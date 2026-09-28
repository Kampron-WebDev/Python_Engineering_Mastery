# Watch CPython's pipeline for ONE line of code.   Run me:  python pipeline.py
import ast
import dis
import io
import sys
import tokenize

source = "total = price * 2\n"
print(f"Python {sys.version.split()[0]}\nSOURCE: {source}")

print("1) TOKENS")
for tok in tokenize.generate_tokens(io.StringIO(source).readline):
    if tok.string.strip():
        print(f"   {tokenize.tok_name[tok.type]:<8} {tok.string!r}")

print("\n2) AST")
print(ast.dump(ast.parse(source), indent=3))

print("\n3) CODE OBJECT")
code = compile(source, "<demo>", "exec")
print("   constants:", code.co_consts)
print("   names:    ", code.co_names)
print("   raw bytes:", code.co_code[:16], "...")

print("\n4) BYTECODE (what the PVM executes)")
dis.dis(code)

print("\n5) RUN IT")
namespace = {"price": 21}
exec(code, namespace)
print("   total =", namespace["total"])
