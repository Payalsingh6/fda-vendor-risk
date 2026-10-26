from src.tools.schemas import ContractState

def risk_scorer_agent(state: ContractState) -> ContractState:
    state.risk_score = 0.2
    return state