from .schemas import Clause, Deviation, RiskLevel
from typing import List

def segment_contract(contract_text: str) -> List[Clause]:
    """Structure-aware parsing of 10-15 page contract"""
    clauses = []
    lines = contract_text.split('\n')
    curr_num = "1.0"
    curr_text = ""
    for line in lines:
        if line.strip() and line[0].isdigit():
            if curr_text:
                clauses.append(Clause(clause_number=curr_num, clause_type="unknown", text=curr_text))
            parts = line.split(' ', 1)
            curr_num = parts[0]
            curr_text = parts[1] if len(parts)>1 else ""
        else:
            curr_text += " " + line
    if curr_text:
        clauses.append(Clause(clause_number=curr_num, clause_type="unknown", text=curr_text))
    return clauses

def search_playbook(clause_type: str) -> dict:
    """RAG over playbook - finds deviation"""
    playbook = {
        "limitation of liability": {"rule_id": "R-001", "standard": "Cap at annual fees"},
        "indemnity": {"rule_id": "R-002", "standard": "Mutual indemnity only"},
        "termination": {"rule_id": "R-003", "standard": "30 days notice"},
        "auto-renewal": {"rule_id": "R-004", "standard": "No auto-renewal without notice"},
        "payment terms": {"rule_id": "R-005", "standard": "Net 60"},
        "data protection": {"rule_id": "R-006", "standard": "HIPAA + encryption"},
        "SLA": {"rule_id": "R-007", "standard": "99.5% uptime"},
        "IP": {"rule_id": "R-008", "standard": "Vendor retains pre-existing IP"},
        "governing law": {"rule_id": "R-009", "standard": "Delhi law"},
        "confidentiality": {"rule_id": "R-010", "standard": "2 year NDA"}
    }
    return playbook.get(clause_type.lower(), {"rule_id": "R-000", "standard": "Not in playbook"})

def score_risk(deviation: str) -> RiskLevel:
    """Risk scorer High/Medium/Low with reason"""
    high_keywords = ["unlimited", "perpetual", "no liability", "auto-renewal"]
    if any(k in deviation.lower() for k in high_keywords):
        return RiskLevel.HIGH
    if "termination" in deviation.lower() or "payment" in deviation.lower():
        return RiskLevel.MEDIUM
    return RiskLevel.LOW

def get_fallback_language(clause_type: str) -> str:
    """Suggested fallback wording"""
    fallbacks = {
        "limitation of liability": "Liability capped at fees paid in last 12 months.",
        "indemnity": "Each party indemnifies for its own gross negligence.",
        "auto-renewal": "Renewal requires 30 days written notice.",
        "data protection": "Vendor shall encrypt patient data and comply with DPDP Act."
    }
    return fallbacks.get(clause_type.lower(), "Propose standard playbook language.")