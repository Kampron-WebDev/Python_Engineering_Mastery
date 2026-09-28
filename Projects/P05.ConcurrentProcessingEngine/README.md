# P05: High-Concurrency Processing Engine

[🏠 Course](../../README.md) · [🗺️ Roadmap](../../ROADMAP.md)

**Do after:** [Level XVI: Threads, Processes & Parallelism](../../Stage4.ConcurrencyDistributedArchitecture/Lv16.ThreadsProcessesParallelism/README.md) · ⏱️ about 1 week

## 🎯 Brief

API → task queue → worker pool → database → results, with performance experiments.

## ✅ Requirements

- [ ] Same workload implemented with asyncio, threads and processes
- [ ] Benchmarks for I/O-bound and CPU-bound variants
- [ ] Write-up choosing a model, with evidence

## 📦 Deliverables

- Its **own Git repository** (portfolio work; link it in PROGRESS.md)
- `pyproject.toml`, strict type checking, Ruff, and a test suite that passes with one command
- `README.md` (what, how to run, how to test) and `ARCHITECTURE.md` (components, data flow, the 3 most important decisions and their trade-offs)

## 📊 Rubric (100 points)

| Area | Points |
|---|---:|
| Functionality: every requirement works, edge cases handled | 30 |
| Code design: clear modules, types, no duplication | 20 |
| Tests: meaningful, green, cover the core logic | 20 |
| Reliability: errors, retries, logging where relevant | 10 |
| Documentation: README + ARCHITECTURE.md | 10 |
| Defence: you can justify every major decision | 10 |

📋 A detailed spec with acceptance tests is written when you reach this project.
