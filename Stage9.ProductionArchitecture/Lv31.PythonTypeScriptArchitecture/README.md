# Level XXXI: Python + TypeScript Architecture

[🏠 Course](../../README.md) · [Stage 9](../README.md) · [🗺️ Roadmap](../../ROADMAP.md)

⏱️ About **1 week** · Scoring scheme **B**

> Stop choosing Python OR TypeScript: build systems where each does the job it's best at.

## 🧪 Integration workshop

This level has no numbered modules: it's a hands-on workshop that combines this course with your other courses.

```text
                   ┌─────────────────┐
                   │ Next.js / TS    │
                   │ Web Platform    │
                   └────────┬────────┘
                         API/BFF
           ┌────────────────┴─────────────────┐
   TypeScript Services                 Python Services
   Users / Billing / CRUD              AI / ML / Data
           └───────────────┬──────────────────┘
                       Event Bus
                    PostgreSQL / Redis
```

- [ ] Shared contracts: generate TypeScript types from Pydantic/OpenAPI schemas (and vice versa)
- [ ] A Next.js front end calling a TypeScript BFF that delegates AI work to a Python service
- [ ] Events between a TypeScript service and a Python worker through Redis or a broker
- [ ] Decision record: which responsibilities belong in TypeScript, which in Python, and why

## 📊 Scoring weights

| Area | Weight |
|---|---:|
| Language knowledge | 10% |
| Coding exercises | 15% |
| Problem solving / algorithms | 15% |
| Debugging | 15% |
| Projects | 25% |
| Code design / architecture | 20% |
