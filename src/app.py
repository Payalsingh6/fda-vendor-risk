from src.tools.schemas import ContractState
from src.agents.extractor import extractor_agent
from src.agents.reviewer import reviewer_agent
from src.agents.risk_scorer import risk_scorer_agent
from src.agents.summarizer import summarizer_agent
import uuid

def build_graph():
    """Simple graph without langgraph - for AppLocker blocked systems"""
    print("Building pipeline: extractor -> reviewer -> risk_scorer -> summarizer")
    return True

def run_app(contract_text: str):
    trace_id = f"trace-{uuid.uuid4().hex[:8]}"
    print(f"Starting App Trace: {trace_id}")
    
    state = ContractState(
        trace_id=trace_id,
        contract_id="FDA-001",
        clauses=[],
        deviations=[],
        review_loops=0,
        needs_human=False
    )
    
    # Same flow as langgraph
    state = extractor_agent(state)
    print(f"Extractor found {len(state.clauses)} clauses")
    state = reviewer_agent(state)
    print(f"Reviewer found {len(state.deviations)} deviations")
    state = risk_scorer_agent(state)
    print(f"Risk score: {state.risk_score}")
    state = summarizer_agent(state)
    
    print("LANGGRAPH SUCCESS! (Fallback mode for AppLocker)")
    print(f"Memo: {state.memo}")
    return state

if __name__ == "__main__":
    run_app("dummy FDA contract")