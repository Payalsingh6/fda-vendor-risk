from ..tools.schemas import ContractState
from ..tools.contract_tools import score_risk, get_fallback_language

def risk_scorer_agent(state: ContractState) -> ContractState:
    print(f"[{state.trace_id}] Risk Scorer: Scoring {len(state.deviations)} deviations")
    for dev in state.deviations:
        risk_level = score_risk(dev.expected_deviation)
        dev.risk = risk_level
        dev.fallback = get_fallback_language(dev.clause_type)
        if risk_level.value == "High":
            dev.reason = f"High risk: {dev.expected_deviation} violates playbook {dev.playbook_rule_id}"
    # Loop logic for human review
    if any(d.risk.value == "High" for d in state.deviations):
        state.review_loops += 1
        if state.review_loops > 2:
            state.needs_human = True
    return state