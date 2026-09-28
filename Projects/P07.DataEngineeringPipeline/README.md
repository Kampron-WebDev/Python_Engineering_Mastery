# P07: Data Pipeline Platform

[🏠 Course](../../README.md) · [🗺️ Roadmap](../../ROADMAP.md)

**Do after:** [Level XX: Data Engineering Foundations](../../Stage5.DataEngineeringMath/Lv20.DataEngineeringFoundations/README.md) · ⏱️ about 2 weeks

## 🎯 Brief

Raw data → validation → transformation → storage → analytics API, on a large real dataset.

## ✅ Requirements

- [ ] Ingest a large public dataset
- [ ] Schema validation with a quarantine for bad rows
- [ ] Parquet storage, partitioned
- [ ] Re-runnable, idempotent runs
- [ ] An analytics API

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
