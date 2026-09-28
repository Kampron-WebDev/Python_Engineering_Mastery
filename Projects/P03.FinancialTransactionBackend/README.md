# P03: Financial Transaction Backend

[🏠 Course](../../README.md) · [🗺️ Roadmap](../../ROADMAP.md)

**Do after:** [Level XIII: Database Engineering with Python](../../Stage3.AutomationDataBackend/Lv13.DatabaseEngineering/README.md) · ⏱️ about 2 weeks

## 🎯 Brief

Python + PostgreSQL + Redis: accounts and money movement that must never be wrong.

## ✅ Requirements

- [ ] Accounts & balances in integer minor units
- [ ] Transfers in database transactions
- [ ] Audit log
- [ ] Authentication
- [ ] Idempotency keys (Redis)
- [ ] Concurrency-safe tests (double-spend attempts)

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
