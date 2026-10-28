from src.tools.contract_tools import segment_contract

def _get(state, key, default=None):
    if isinstance(state, dict):
        return state.get(key, default)
    return getattr(state, key, default)

def _set_safe(state, key, value):
    try:
        if isinstance(state, dict):
            state[key] = value
        else:
            # Only set if field exists in Pydantic model
            if hasattr(state, 'model_fields') and key in state.model_fields:
                setattr(state, key, value)
            elif hasattr(state, '__dict__') and key in state.__dict__:
                setattr(state, key, value)
            else:
                # Try anyway, if fails skip
                try:
                    setattr(state, key, value)
                except:
                    pass
    except:
        pass
    return state

def extractor_agent(state):
    contract_path = _get(state, "contract_path", "data/contracts/high_risk.txt")
    
    text = ""
    try:
        with open(contract_path, "r", encoding="utf-8-sig", errors="ignore") as f:
            text = f.read()
    except:
        with open(contract_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

    text = text.replace("\x00", "").replace("\ufeff", "").replace("\ufffe", "")
    clauses = segment_contract(text)
    print(f"[Extractor] Extracted {len(clauses)} clauses")

    _set_safe(state, "clauses", clauses)
    # Don't set contract_text if field doesn't exist
    return state