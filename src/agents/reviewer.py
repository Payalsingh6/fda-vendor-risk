from src.tools.schemas import ContractState

def reviewer_agent(state: ContractState) -> ContractState:
    state.deviations = [{"clause_id": "1", "risk": "low"}]
    return state