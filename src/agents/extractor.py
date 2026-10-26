from ..tools.schemas import ContractState

def summarizer_agent(state: ContractState) -> ContractState:
    print(f"[{state.trace_id}] Summarizer: Creating memo")
    high = sum(1 for d in state.deviations if d.risk.value == "High")
    memo = f"""
CONTRACT REVIEW MEMO
Contract ID: {state.contract_id}
Trace ID: {state.trace_id}
Total Clauses: {len(state.clauses)}
Deviations Found: {len(state.deviations)}
High Risk: {high}
Review Loops: {state.review_loops}
Needs Human: {state.needs_human}

DEVIATIONS:
"""
    for d in state.deviations:
        memo += f"\n- Clause {d.clause_number} [{d.clause_type}] Risk:{d.risk.value} Reason:{d.reason} Fallback:{d.fallback}"
    
    state.memo = memo
    return state