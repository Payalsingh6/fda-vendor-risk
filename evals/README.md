# Vendor Contract Risk Reviewer - FDA Capstone

## Problem Statement
FDA procurement team reviews 60 vendor contracts/quarter, 3-4 hrs each. Risky clauses slip - unlimited liability, missing FDA data encryption. Need auto reviewer that cites playbook rules (PL-XXX-001) with RAG.

## Architecture (Phase 1-3)
- **Agents**: Extractor -> Comparator (RAG) -> Risk Scorer -> Memo Writer
- **Tools**: `segment_contract()` utf-8-sig BOM-safe, `search_playbook()` PL- IDs, `score_risk()` per PL- rules
- **Diagrams**: `docs/architecture/c4_context.md`, `c4_container.md`, `sequence.md`
- **ADRs**: `docs/adr/ADR-001-pipeline.md`, `ADR-002-vector-store.md`, `ADR-003-long-doc.md`

## NFRs Met
- Review <3 min, Cost <₹25, Deviation recall 85%+, Risk match 80%+
- Security: Prompt injection blocked ("Ignore as AI reviewer:...")
- Citation: All deviations cite PL-LIAB-001, PL-DATA-001 etc.

## 7-Day Delivery Log
| Day | Date | What Shipped | Tag | Time |
|-----|------|--------------|-----|------|
| 1 | 23 Oct | Problem, personas, NFRs, constraints | day-01 | 60m |
| 2 | 24 Oct | C4 context/container, sequence, ADR-001,002 | day-02 | 60m |
| 3 | 25 Oct | Playbook.md (PL- rules) + 5 contracts + golden.json | day-03 | 60m |
| 4 | 26 Oct | Clause segmenter segment_contract() BOM-safe | day-04 | 60m |
| 5 | 27 Oct | RAG search_playbook() + score_risk() PL- IDs | day-05 | 60m |
| 6 | 28 Oct | Memo writer + security + EVAL PASSED | day-06 | 60m |
| 7 | 29 Oct | Final report + slides + git tags | day-07 | 60m |

## How to Run
```bash
pip install -r requirements.txt
python -m evals.evaluate
# Expected: contract-001: PASS, EVAL PASSED