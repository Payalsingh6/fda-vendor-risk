from src.tools.schemas import ContractState

def extractor_agent(state: ContractState) -> ContractState:
    # Dummy extraction for Day-6 testing
    state.clauses = [{"id": "1", "text": "Sample FDA clause"}]
    return state