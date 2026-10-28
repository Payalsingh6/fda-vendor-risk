from src.tools.contract_tools import score_risk

def _get(state, key, default=None):
    if isinstance(state, dict):
        return state.get(key, default)
    return getattr(state, key, default)

def _set_safe(state, key, value):
    try:
        if isinstance(state, dict):
            state[key] = value
        else:
            setattr(state, key, value)
    except:
        pass
    return state

def risk_scorer_agent(state):
    deviations = _get(state, "deviations", [])
    risks = []
    for dev in deviations:
        result = score_risk(dev)
        risks.append(result)
        clause_num = dev.get("clause_number", "") if isinstance(dev, dict) else getattr(dev, "clause_number", "")
        print(f"[Risk] {clause_num} -> {result['level']} per {result['rule_id']}")
    
    _set_safe(state, "risks", risks)
    return state