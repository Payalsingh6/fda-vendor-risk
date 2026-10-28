from src.tools.contract_tools import search_playbook

def _get(state, key, default=None):
    if isinstance(state, dict):
        return state.get(key, default)
    return getattr(state, key, default)

def _set(state, key, value):
    if isinstance(state, dict):
        state[key] = value
    else:
        setattr(state, key, value)
    return state

def comparator_agent(state):
    clauses = _get(state, "clauses", [])
    deviations = []
    for clause in clauses:
        clause_type = clause.get("clause_type", "general") if isinstance(clause, dict) else getattr(clause, "clause_type", "general")
        clause_num = clause.get("clause_number", "0") if isinstance(clause, dict) else getattr(clause, "clause_number", "0")
        clause_text = clause.get("text","") if isinstance(clause, dict) else getattr(clause, "text", "")
        
        playbook_rules = search_playbook(clause_type)
        for rule in playbook_rules:
            deviation = {
                "clause_number": clause_num,
                "clause_type": clause_type,
                "clause_text": clause_text[:500],
                "playbook_rule": rule["rule_id"],
                "rule_id": rule["rule_id"],
                "citation": rule["rule_id"],
                "is_deviation": "unlimited" in clause_text.lower() or "no encryption" in clause_text.lower() or "perpetual" in clause_text.lower()
            }
            deviations.append(deviation)
            print(f"[Comparator][RAG] Clause {clause_num} -> {rule['rule_id']}")

    _set(state, "deviations", deviations)
    return state

def reviewer_agent(state):
    return comparator_agent(state)