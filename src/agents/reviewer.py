from ..tools.schemas import ContractState, Deviation
from ..tools.contract_tools import search_playbook

def reviewer_agent(state: ContractState) -> ContractState:
    print(f"[{state.trace_id}] Reviewer: Checking {len(state.clauses)} clauses")
    for clause in state.clauses:
        playbook_result = search_playbook(clause.clause_type)
        if playbook_result["rule_id"] != "R-000":
            # Create deviation - will be scored next
            dev = Deviation(
                clause_number=clause.clause_number,
                clause_type=clause.clause_type,
                playbook_rule_id=playbook_result["rule_id"],
                expected_deviation=playbook_result["standard"],
                risk="Low",
                reason=f"Found non-standard {clause.clause_type}",
                fallback="Use standard"
            )
            state.deviations.append(dev)
    return state