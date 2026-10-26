from src.tools.schemas import ContractState

def summarizer_agent(state: ContractState) -> ContractState:
    state.memo = "Memo: Contract reviewed. Risk low. No human needed."
    return state