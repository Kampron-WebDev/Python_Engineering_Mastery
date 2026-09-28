# P02: Automation Toolkit

[🏠 Course](../../README.md) · [🗺️ Roadmap](../../ROADMAP.md)

**Do after:** [Level XII: Files, Operating System & Automation](../../Stage3.AutomationDataBackend/Lv12.FilesOSAutomation/README.md) · ⏱️ about 1 week

## 🎯 Brief

A set of idempotent automation scripts for real chores: backups, file organisation, builds and data transforms.

## ✅ Requirements

- [ ] Backup with rotation
- [ ] File organiser
- [ ] Build/deploy helper wrapping subprocesses safely
- [ ] CSV/JSON transformer
- [ ] Dry-run mode for everything
- [ ] Tests

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
