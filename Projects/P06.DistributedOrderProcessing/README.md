# P06: Distributed Order Processing System

[🏠 Course](../../README.md) · [🗺️ Roadmap](../../ROADMAP.md)

**Do after:** [Level XVII: Distributed Backend Systems](../../Stage4.ConcurrencyDistributedArchitecture/Lv17.DistributedBackendSystems/README.md) · ⏱️ about 2 weeks

## 🎯 Brief

API service → PostgreSQL → event queue → payment and notification workers, with failures injected on purpose.

## ✅ Requirements

- [ ] Outbox pattern
- [ ] Idempotent consumers
- [ ] Retries with backoff + dead-letter queue
- [ ] Saga with compensation
- [ ] Chaos tests: kill workers mid-flow and recover correctly

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
