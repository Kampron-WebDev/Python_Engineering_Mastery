# 🐍 Python Engineering Mastery

Not "Python for beginners". A **language + backend + AI-infrastructure** mastery track, and one of your three primary engineering languages.

**Start here → [00.Orientation](00.Orientation/README.md), then [Module 001, Lesson 01](Stage1.LanguageMastery/Lv01.PythonLanguageFoundations/M001.PythonAsAProgrammingLanguage/L01.WhatPythonIsAndIsNot/README.md).**
How this course fits with your other three: **[SYNC.md](SYNC.md)** · Full order and timing: **[ROADMAP.md](ROADMAP.md)** · Your scores: **[PROGRESS.md](PROGRESS.md)**

---

## 🧭 Python's job in your stack

```text
                 YOUR ENGINEERING STACK
  C++                    → memory, performance, systems                (The C++ 20 Masterclass)
  Python                 → backend systems, automation, data, AI/ML,   (THIS course)
                           distributed workers, AI infrastructure
  TypeScript             → platform services, APIs, shared types       (JavaScript & TypeScript Mastery)
  JavaScript / TS        → browser, React, Next.js, web apps           (+ Full-Stack Engineering Mastery)
  Rust (later)           → memory-safe systems & performance-critical infrastructure

  Around all of it: Linux · Docker · Git · SQL · PostgreSQL · Redis · Networking · Security · Testing
                    CI/CD · Cloud · Distributed Systems · System Design · DevOps · Observability
```

## 🎯 By the end you can…

- Write idiomatic, professional, strictly typed Python, and explain its execution model
- Master references, mutability, memory, garbage collection, closures, decorators and descriptors
- Use object-oriented and functional approaches where each fits
- Design, package and publish maintainable libraries; build CLI and automation tools
- Build asynchronous, concurrent and parallel systems, and choose the right model
- Build production APIs with PostgreSQL, Redis, queues and background workers
- Design backend and distributed architectures that survive failure
- Test, profile and optimise Python, and hand hot paths to C++ when justified
- Process large datasets, and understand NumPy and pandas well enough for engineering work
- Build ML and deep-learning systems, LLM / RAG infrastructure, AI services and agent systems
- Deploy, observe and scale Python services and production AI backends
- Integrate Python with TypeScript and C++

---

## 🗺️ The map: 9 stages · 32 levels · 226 modules · 12 projects

| Stage | Levels | Modules | Suggested timing |
|---|---|---|---|
| [1 · Python Language Mastery](Stage1.LanguageMastery/README.md) 🟢 | I–VII | 001–042 | Months 1–5 |
| [2 · Internals, Typing, Testing & Algorithms](Stage2.InternalsTypingTestingAlgorithms/README.md) | VIII–XI | 043–084 | Months 6–8 |
| [3 · Automation, Databases & Backend](Stage3.AutomationDataBackend/README.md) | XII–XIV | 085–105 | Months 9–12 |
| [4 · Concurrency, Distributed, Architecture & Performance](Stage4.ConcurrencyDistributedArchitecture/README.md) | XV–XIX | 106–139 | Months 13–15 |
| [5 · Data Engineering & Mathematics](Stage5.DataEngineeringMath/README.md) | XX–XXI | 140–149 | Months 16–18 |
| [6 · Machine Learning & Deep Learning](Stage6.MachineAndDeepLearning/README.md) | XXII–XXIII | 150–165 | Months 19–21 |
| [7 · Transformers, LLMs, RAG & Agents](Stage7.ModernAI/README.md) | XXIV–XXVII | 166–195 | Months 22–24 |
| [8 · AI Infrastructure & MLOps](Stage8.AIInfrastructureMLOps/README.md) | XXVIII–XXIX | 196–213 | Months 25–27 |
| [9 · Production Architecture & Capstone](Stage9.ProductionArchitecture/README.md) | XXX–XXXII | 214–226 + workshops | Months 28–30 |

### The project ladder

| # | Project | After |
|---|---|---|
| 1 | [Developer Productivity CLI](Projects/P01.DeveloperProductivityCLI/README.md) | Level XII |
| 2 | [Automation Toolkit](Projects/P02.AutomationToolkit/README.md) | Level XII |
| 3 | [Financial Transaction Backend](Projects/P03.FinancialTransactionBackend/README.md) | Level XIII |
| 4 | [Production FastAPI Application](Projects/P04.ProductionFastAPIApplication/README.md) | Level XIV |
| 5 | [High-Concurrency Processing Engine](Projects/P05.ConcurrentProcessingEngine/README.md) | Level XVI |
| 6 | [Distributed Order Processing](Projects/P06.DistributedOrderProcessing/README.md) | Level XVII |
| 7 | [Data Pipeline Platform](Projects/P07.DataEngineeringPipeline/README.md) | Level XX |
| 8 | [ML Deployment Service](Projects/P08.MLDeploymentService/README.md) | Level XXII |
| 9 | [Production RAG Platform](Projects/P09.ProductionRAGPlatform/README.md) | Level XXVI |
| 10 | [Agent Workflow Platform](Projects/P10.AgentWorkflowPlatform/README.md) | Level XXVII |
| 11 | [Distributed AI Inference Backend](Projects/P11.DistributedAIInferenceBackend/README.md) | Level XXVIII |
| 12 | [**Final Capstone: Enterprise AI Platform**](Final/FinalCapstone-EnterpriseAIPlatform/README.md) | Level XXXII |
| 🎓 | [**Final Python Assessment**](Final/FinalAssessment/README.md): 8 examinations | the end |

About **127 weeks ≈ 29 months**, running *alongside* your other courses. 🟢 = lessons written; the rest are written one module ahead of you.

---

## 🧩 Every lesson has 10 parts

**Concept** (simple analogy → precise words) · **Why it exists** · **Internal mechanics** · **Simple example** · **Real-world example** · **Coding exercise** · **Debugging challenge** · **Design question** · **Short assessment** · **Reflection**.

## ✅ Competency gates, not calendars

```text
Explain it → Implement it → Debug it → Apply it → Compare alternatives → Identify trade-offs
```

Every module README ends with its gate and that module's own questions. **You don't graduate because you reached Module 226.** You graduate by passing the [8-part Final Assessment](Final/FinalAssessment/README.md), which evaluates you as *an engineer who happens to use Python*.

## 🧠 Three layers for everything

| Layer | Question | Example (asyncio) |
|---|---|---|
| 1 | How do I **use** it? | `async def`, `await`, `TaskGroup` |
| 2 | How does it **work**? | The event loop, coroutines, how a task gets scheduled |
| 3 | **When** should I use it, and when not? | Async vs threads vs processes vs a worker fleet vs C++ |

## 📊 Assessment

| Area | Stages 1–3 (scheme A) | Stages 4–9 (scheme B) |
|---|---:|---:|
| Language knowledge | 20% | 10% |
| Coding exercises | 20% | 15% |
| Problem solving / algorithms | 15% | 15% |
| Debugging | 15% | 15% |
| Projects | 20% | 25% |
| Code design / architecture | 10% | 20% |

Each level ends with a **level exam** (knowledge · timed coding · debugging · design), with a pass mark of 70% in each part.

---

## 🛠️ Folder pattern & tools

```text
Stage1.LanguageMastery/Lv01.PythonLanguageFoundations/M001.PythonAsAProgrammingLanguage/L01.WhatPythonIsAndIsNot/
├── README.md            ← the 10-part lesson
├── Examples/            ← python example.py
├── Exercises/01_Name/   ← main.py (yours) · test_main.py (checker) · solution/ (after trying!)
├── Debugging/01_Name/   ← same shape, but main.py is broken
└── MY-NOTES.md          ← your answers and reflections
```

| Command (from the course folder) | What it does |
|---|---|
| `.venv\Scripts\activate` | Use the course's own Python (see Orientation) |
| `python -m pytest` *(inside an exercise folder)* | Checks **your** code |
| `powershell -ExecutionPolicy Bypass -File tools\check-exercises.ps1` | Proves every model solution passes |
| `powershell -ExecutionPolicy Bypass -File tools\sync-vscode.ps1` | Copies the VS Code setup everywhere |
| `python tools\skeleton\generate.py` | Rebuilds the map (⚠️ overwrites PROGRESS.md) |

VS Code: **Ctrl+Shift+B** runs the open file · **Ctrl+Shift+P → "Tasks: Run Test Task"** tests the exercise · **F5** debugs.

## 📚 Primary references

- [The Python Tutorial & Library Reference](https://docs.python.org/3/) · [The Language Reference](https://docs.python.org/3/reference/)
- [PEPs](https://peps.python.org/): the design documents behind every feature
- [Python Packaging User Guide](https://packaging.python.org/) · [Python typing docs](https://typing.python.org/)
