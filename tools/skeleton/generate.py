"""Generates the course map from curriculum.py.

    .venv\\Scripts\\python tools\\skeleton\\generate.py

⚠️ OVERWRITES Stage / Level / Module / Project READMEs, ROADMAP.md and PROGRESS.md.
   Hand-written lesson folders (L01.* …) and Level-Exam folders are never touched.
"""

import math
import re
from pathlib import Path

from curriculum import FINALS, LEVELS, PROJECTS, REVIEW, STAGES, WORKSHOPS

ROOT = Path(__file__).resolve().parents[2]
READY = {1, 2}  # modules whose lessons are written

WEIGHTS = {
    "A": {"Language knowledge": 20, "Coding exercises": 20, "Problem solving / algorithms": 15, "Debugging": 15, "Projects": 20, "Code design / architecture": 10},
    "B": {"Language knowledge": 10, "Coding exercises": 15, "Problem solving / algorithms": 15, "Debugging": 15, "Projects": 25, "Code design / architecture": 20},
}


def pascal(text: str) -> str:
    words = re.sub(r"[^A-Za-z0-9 ]", " ", text).split()
    return "".join(w[0].upper() + w[1:] for w in words)[:40]


def scheme(stage: int) -> str:
    return "A" if stage <= 3 else "B"


def weight_table(stage: int) -> str:
    rows = [f"| {k} | {v}% |" for k, v in WEIGHTS[scheme(stage)].items()]
    return "\n".join(["| Area | Weight |", "|---|---:|", *rows])


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8", newline="\n")


def up(rel_dir: str) -> str:
    return "../" * len(rel_dir.split("/"))


stage_dir = {n: f"Stage{n}.{slug}" for n, slug, *_ in STAGES}
level_dir = {lv[0]: f"{stage_dir[lv[4]]}/Lv{lv[0]:02d}.{lv[2]}" for lv in LEVELS}
modules = [(m, lv) for lv in LEVELS for m in lv[7]]
module_dir = {m[0]: f"{level_dir[lv[0]]}/M{m[0]:03d}.{m[1]}" for m, lv in modules}
project_dir = {p[0]: f"Projects/{p[0]}.{p[1]}" for p in PROJECTS}
final_dir = {f[0]: f"Final/{f[1]}" for f in FINALS}


def lesson_dir(i: int, title: str) -> str:
    return f"L{i + 1:02d}.{'ModuleReview' if title == REVIEW else pascal(title)}"


GATE = """Reading a lesson is **not** finishing it. Tick every box, honestly:

- [ ] **Explain it:** I can answer every question below out loud, simply, without notes.
{questions}
- [ ] **Implement it:** all exercises are green, written without opening solutions first.
- [ ] **Debug it:** I fixed every debugging challenge and can explain *why* each bug happened.
- [ ] **Apply it:** I used this module's ideas in a project or a program of my own.
- [ ] **Compare alternatives:** I can name another way to solve the same problem (in Python, and in JS/TS or C++).
- [ ] **Identify trade-offs:** I can say when this is the *wrong* tool."""

# ───────────────────────── Modules ─────────────────────────
for idx, (m, lv) in enumerate(modules):
    n, slug, title, big, lessons, explain, build = m
    d = module_dir[n]
    back = up(d)
    prev = modules[idx - 1][0] if idx > 0 else None
    nxt = modules[idx + 1][0] if idx + 1 < len(modules) else None
    nav = [f"[🏠 Course]({back}README.md)", f"[Level {lv[1]}](../README.md)"]
    if prev:
        nav.append(f"[⬅ M{prev[0]:03d}]({back}{module_dir[prev[0]]}/README.md)")
    if nxt:
        nav.append(f"[M{nxt[0]:03d} ➡]({back}{module_dir[nxt[0]]}/README.md)")

    rows, ready_count = [], 0
    for i, t in enumerate(lessons):
        ld = lesson_dir(i, t)
        ready = (ROOT / d / ld / "README.md").exists()
        ready_count += ready
        rows.append(f"| {i + 1:02d} | {f'[{t}]({ld}/README.md)' if ready else t} | {'🟢' if ready else '📋'} |")
    status = "🟢 Ready" if ready_count == len(lessons) else "📋 Planned (lessons are written just before you reach this module)"
    build_md = ("\n## 🛠️ Build it yourself\n\n" + "\n".join(f"- {b}" for b in build) + "\n") if build else ""

    write(f"{d}/README.md", f"""
# Module {n:03d}: {title}

{' · '.join(nav)}

**Stage {lv[4]} · Level {lv[1]}: {lv[3]}** · Status: {status}

## 🧸 The big idea

{big}

## 📖 Lessons

| # | Lesson | |
|---|---|---|
{chr(10).join(rows)}

Every lesson follows the 10-part format: Concept → Why it exists → Internal mechanics → Simple example → Real-world example → Coding exercise → Debugging challenge → Design question → Short assessment → Reflection.
{build_md}
## 🎯 Mastery gate

{GATE.format(questions=chr(10).join(f'  - {q}' for q in explain))}

Record the result in [PROGRESS.md]({back}PROGRESS.md).

## 📊 Scoring for this stage (scheme {scheme(lv[4])})

{weight_table(lv[4])}
""")

# ───────────────────────── Levels ─────────────────────────
for lv in LEVELS:
    num, roman, slug, title, stage, weeks, goal, mods = lv
    d = level_dir[num]
    back = up(d)
    unlocked = [p for p in PROJECTS if p[3] == num]
    exam_ready = (ROOT / d / "Level-Exam" / "README.md").exists()
    if mods:
        body = "## Modules\n\n| Module | Title | Lessons |\n|---|---|---:|\n" + "\n".join(
            f"| {m[0]:03d} | [{m[2]}](M{m[0]:03d}.{m[1]}/README.md) | {len(m[4])} |" for m in mods)
    else:
        w = WORKSHOPS[num]
        body = ("## 🧪 Integration workshop\n\nThis level has no numbered modules: it's a hands-on workshop that combines this course with your other courses.\n\n"
                f"```text\n{w['diagram']}\n```\n\n" + "\n".join(f"- [ ] {t}" for t in w["tasks"]))
    projects_md = ("\n## 🏗️ Unlocks these projects\n\n" + "\n".join(f"- [{p[0]}: {p[2]}]({back}{project_dir[p[0]]}/README.md)" for p in unlocked) + "\n") if unlocked else ""
    exam_md = "" if not mods else f"""
## 🎓 Level exam{': [open it](Level-Exam/README.md)' if exam_ready else ''}

Taken only when every module gate in this level is ticked. Four parts, each scored separately (pass mark **70%** in each):

1. **Knowledge:** a written quiz without notes.
2. **Coding:** timed exercises with no hints.
3. **Debugging:** broken programs, where you fix them *and* explain the causes.
4. **Design:** one open question about structuring a solution, and why.
"""
    write(f"{d}/README.md", f"""
# Level {roman}: {title}

[🏠 Course]({back}README.md) · [Stage {stage}](../README.md) · [🗺️ Roadmap]({back}ROADMAP.md)

⏱️ About **{weeks} week{'s' if weeks > 1 else ''}** · Scoring scheme **{scheme(stage)}**

> {goal}

{body}
{projects_md}{exam_md}
## 📊 Scoring weights

{weight_table(stage)}
""")

# ───────────────────────── Stages ─────────────────────────
for n, slug, title, months in STAGES:
    lvs = [lv for lv in LEVELS if lv[4] == n]
    rows = []
    for lv in lvs:
        mods = lv[7]
        rng = f"{mods[0][0]:03d}–{mods[-1][0]:03d}" if mods else "workshop"
        rows.append(f"| {lv[1]} | [{lv[3]}](Lv{lv[0]:02d}.{lv[2]}/README.md) | {rng} | {lv[5]} |")
    write(f"{stage_dir[n]}/README.md", f"""
# Stage {n}: {title}

[🏠 Course](../README.md) · [🗺️ Roadmap](../ROADMAP.md) · Suggested timing: **{months}** · Scoring scheme **{scheme(n)}**

| Level | Title | Modules | Weeks |
|---|---|---|---:|
{chr(10).join(rows)}
""")

# ───────────────────────── Projects & finals ─────────────────────────
RUBRIC = """| Area | Points |
|---|---:|
| Functionality: every requirement works, edge cases handled | 30 |
| Code design: clear modules, types, no duplication | 20 |
| Tests: meaningful, green, cover the core logic | 20 |
| Reliability: errors, retries, logging where relevant | 10 |
| Documentation: README + ARCHITECTURE.md | 10 |
| Defence: you can justify every major decision | 10 |"""

for pid, slug, title, after, weeks, brief, reqs in PROJECTS:
    d = project_dir[pid]
    back = up(d)
    lv = next(x for x in LEVELS if x[0] == after)
    write(f"{d}/README.md", f"""
# {pid}: {title}

[🏠 Course]({back}README.md) · [🗺️ Roadmap]({back}ROADMAP.md)

**Do after:** [Level {lv[1]}: {lv[3]}]({back}{level_dir[after]}/README.md) · ⏱️ about {weeks} week{'s' if weeks > 1 else ''}

## 🎯 Brief

{brief}

## ✅ Requirements

{chr(10).join(f'- [ ] {r}' for r in reqs)}

## 📦 Deliverables

- Its **own Git repository** (portfolio work; link it in PROGRESS.md)
- `pyproject.toml`, strict type checking, Ruff, and a test suite that passes with one command
- `README.md` (what, how to run, how to test) and `ARCHITECTURE.md` (components, data flow, the 3 most important decisions and their trade-offs)

## 📊 Rubric (100 points)

{RUBRIC}

📋 A detailed spec with acceptance tests is written when you reach this project.
""")

for fid, slug, title, weeks, brief, reqs in FINALS:
    d = final_dir[fid]
    back = up(d)
    write(f"{d}/README.md", f"""
# {title}

[🏠 Course]({back}README.md) · [🗺️ Roadmap]({back}ROADMAP.md) · ⏱️ about {weeks} weeks

## 🎯 Brief

{brief}

## ✅ Sections / requirements

{chr(10).join(f'- [ ] {r}' for r in reqs)}

Pass mark: **70% in every section.**
""")

# ───────────────────────── ROADMAP.md ─────────────────────────
week, rows = 0, []


def add_row(kind: str, label: str, link: str, weeks: int) -> None:
    global week
    week += weeks
    rows.append(f"| {kind} | [{label}]({link}) | {weeks} | {week} | ≈ month {math.ceil(week / 4.345)} |")


for lv in LEVELS:
    mods = lv[7]
    rng = (f"M{mods[0][0]:03d}" if len(mods) == 1 else f"M{mods[0][0]:03d}–M{mods[-1][0]:03d}") if mods else "workshop"
    add_row(f"Level {lv[1]}", f"{lv[3]} ({rng})", f"{level_dir[lv[0]]}/README.md", lv[5])
    for p in PROJECTS:
        if p[3] == lv[0]:
            add_row(f"🏗️ {p[0]}", p[2], f"{project_dir[p[0]]}/README.md", p[4])
for f in FINALS:
    add_row(f"🎓 {f[0]}", f[2], f"{final_dir[f[0]]}/README.md", f[3])

write("ROADMAP.md", f"""
# 🗺️ Roadmap: the full sequence

[🏠 Course](README.md) · [🔗 SYNC.md](SYNC.md)

Levels and projects in the order you do them. Weeks are **estimates at a steady pace alongside your other courses**. Competency gates, not the calendar, decide when you move on.

| Step | What | Weeks | Total weeks | When |
|---|---|---:|---:|---|
{chr(10).join(rows)}

**Total: about {week} weeks ≈ {week / 4.345:.0f} months.**
""")

# ───────────────────────── PROGRESS.md ─────────────────────────
mod_rows = "\n".join(f"| {m[0]:03d} {m[2]} | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | |" for m, _ in modules)
exam_rows = "\n".join(f"| {lv[1]} {lv[3]} | | | | | ☐ | |" for lv in LEVELS if lv[7])
proj_rows = "\n".join(f"| {p[0]} {p[2]} | | | |" for p in [*PROJECTS, *[(f[0], f[1], f[2]) for f in FINALS]])
write("PROGRESS.md", f"""
# 📈 My Progress: Python Engineering Mastery

**Started on:** ____-__-__

## Module gates

E = Explain · I = Implement · D = Debug · A = Apply · C = Compare alternatives · T = Trade-offs.

| Module | E | I | D | A | C | T | Date |
|---|---|---|---|---|---|---|---|
{mod_rows}

## Level exams (%)

| Level | Knowledge | Coding | Debugging | Design | Passed? | Date |
|---|---|---|---|---|---|---|
{exam_rows}

## Projects

| Project | Score /100 | Repo link | Date |
|---|---|---|---|
{proj_rows}

## Weekly log

```md
### Week __ (dates) · Modules __
- Lessons finished:
- Exercises done without looking at solutions: __ / __
- Hardest idea this week:
- What made it click:
- To revisit:
```
""")

print(f"Generated {len(STAGES)} stages, {len(LEVELS)} levels, {len(modules)} modules, {len(PROJECTS) + len(FINALS)} projects/finals, {week} weeks.")
for m, _ in modules:
    if m[0] in READY:
        for i, t in enumerate(m[4]):
            print(f"{module_dir[m[0]]}/{lesson_dir(i, t)}")
