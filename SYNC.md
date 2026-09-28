# 🔗 SYNC: keeping your four courses converging

[🏠 Python course](README.md)

You now have four long courses:

| Course | Folder | Role |
|---|---|---|
| **The C++ 20 Masterclass** | `Desktop\The-C-20-Masterclass-Source-Code-main` (lessons 00–60) | Memory, performance, systems thinking |
| **JavaScript & TypeScript Mastery** | `Desktop\JavaScript-TypeScript-Mastery` (Phases 1–30) | The web platform language, deeply |
| **Full-Stack Engineering Mastery** | `Desktop\Full-Stack-Engineering-Mastery` (Months 1–36) | **The spine**: how systems are engineered |
| **Python Engineering Mastery** | this folder (Levels I–XXXII) | Backend, data, AI and AI infrastructure |

They must **not** become four unrelated curricula. The Full-Stack course is the spine; the three language courses feed it. When the spine reaches a topic, the language courses should already have prepared you for it.

---

## ⏱️ Suggested weekly time split

A suggestion for about 20 study hours per week. Shift it as life requires, but keep the *spine* steady.

| Period | Full-Stack (spine) | JS/TS | Python | C++ |
|---|---:|---:|---:|---:|
| Months 1–12 | 8 h | 6 h | 4 h | 2 h (finish the remaining lessons, then weekly practice) |
| Months 13–24 | 8 h | 3 h | 7 h | 2 h |
| Months 25–36 | 8 h | 2 h | 7 h | 3 h (the Python + C++ integration work) |

Rule of thumb: **never** run more than **two** big projects at once. Project weeks borrow hours from the other language courses, not from the spine.

---

## 🎯 Convergence checkpoints

When the Full-Stack course reaches a row, aim to have the other columns done, or at least started. The last column is **the exercise that makes the courses meet**.

| Full-Stack reaches… | JS/TS | Python | C++ | Convergence exercise |
|---|---|---|---|---|
| **M01** Computing fundamentals | Phase 1 (engines, runtimes) | M001 (CPython, bytecode) | 01 How computers & C++ work | One page: "compiled vs JIT vs bytecode interpreter", with `node --print-bytecode`, `python -m dis` and `g++ -S` output side by side |
| **M02** Internet & web | Phase 12 comes later, and that's fine | M001–M002 | 18 Arguments to main | Write the same tiny HTTP GET in JS (fetch), Python (`urllib`) and C++ (sockets, stretch) |
| **M05–M06** JS core & advanced | Phases 4–11 | Level III (closures, decorators) | 21 Lambda functions | **Closures in three languages**: the same counter/memoiser in JS, Python and C++. What does each capture, and how? |
| **M11** TypeScript | Part II Phases 20–23 | Level VIII (typing, Protocols) | 24–25 Templates & Concepts | **Three type systems**: TS structural types, Python Protocols + generics, C++ concepts, all modelling the same `Repository<T>` |
| **M14** Node.js | Phase 19 | Level XII (files, OS, subprocesses) | 50 File I/O & streams | Stream a 1 GB file line by line in Node, Python (generators) and C++; measure memory |
| **M15–M16** Databases & PostgreSQL | — | Level XIII (drivers, SQLAlchemy, Redis) | — | Same schema, queried from Node and from Python; compare the transaction code |
| **M17** Backend & Express | Project JP7 (your own framework) | Level XIV (ASGI, FastAPI) | — | **Build the same REST API twice** (Express vs FastAPI), then write a comparison ADR |
| **M18** Auth | — | M104–M105 | — | Share one JWT between a Node service and a Python service |
| **M20** Testing | Phase 18 | Level XI (pytest, Hypothesis) | 55 Testing & debugging | Property-based tests for the same function in fast-check / Hypothesis |
| **M26–M27** Docker & CI/CD | — | P04 dockerised | 56 Build systems & CMake | One CI pipeline that builds a TS service, a Python service and a C++ module |
| **M31** Performance | Phase 15 (memory & performance) | Level XIX + **M139 Python + C++** | 58 Performance & memory | **Profile a Python hot spot, rewrite it in C++, bind it with pybind11**, benchmark all three |
| **M33–M34** System design & distributed | — | Levels XV–XVII (async, workers, idempotency, sagas) | 53 Concurrency | Same race condition demonstrated in C++ threads, Python threads and JS async; explain each fix |
| **M35** AI engineering | TS types for AI APIs | Levels XXIV–XXVII (LLMs, RAG, agents) | — | A TS front end calling a Python RAG service with streaming |
| **M36** Enterprise capstone | Final JS/TS Capstone | Levels XXXI–XXXII + Final Capstone | 59 Capstone projects | **One system, three angles** (see below) |

### Deep topics taught three times, on purpose

| Topic | C++ | JS/TS | Python | What comparing them teaches |
|---|---|---|---|---|
| Memory & references | 13 Pointers · 14 References · 33 Smart pointers · 52 RAII | Phase 15 Memory | Level IX (references, refcounting, GC) | Manual vs GC vs refcounting: lifetimes and leaks |
| Data structures & algorithms | 54 DSA | Phase 16 | Level X | The same algorithm's speed and code size across three abstraction levels |
| Concurrency | 53 Concurrency | Phase 11 Async | Levels XV–XVI (asyncio, GIL, processes) | Threads vs event loops vs processes: when each wins |
| Design patterns & architecture | 57 Design patterns & SOLID | Phase 17 | Level XVIII | Patterns that are native in one language but ceremony in another |

---

## 🏛️ One capstone, three angles

The three final capstones should be **the same platform**, so your portfolio shows one coherent, serious system instead of three half-finished ones:

```text
            Enterprise Learning Platform with an AI tutor
  ┌──────────────────────────────────────────────────────────────┐
  │ Next.js / TypeScript web app            ← JS/TS Final Capstone │
  │ API gateway + TS services (users, billing)                   │
  │ Python AI services: RAG, agents, lesson generation ← Python P12│
  │ C++ module for a hot numerical/parsing path  ← C++ 59 + Py M139│
  │ Events · Redis · Queue · PostgreSQL · Vector store · Objects │
  │ Docker · CI/CD · Cloud · Observability ← Full-Stack M36        │
  └──────────────────────────────────────────────────────────────┘
```

It's also exactly the scenario of the Python **architecture defence**: *"an AI tutoring platform for 5 million learners"*.

---

## 🔁 How to keep them in sync

- At the end of each **Full-Stack month**, glance at the checkpoint table. Behind in a language course? Use the next project week to catch up; don't skip the spine.
- Record all four courses' gates in their own PROGRESS.md files, and write one line per week in the Full-Stack weekly log naming what each course advanced.
- When you ask for the next batch of lessons in any course, say where you are in the others. The new lessons will reference what you've already done.
