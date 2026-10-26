from src.tools.schemas import ContractState
from src.agents.extractor import extractor_agent
from src.agents.reviewer import reviewer_agent
from src.agents.risk_scorer import risk_scorer_agent
from src.agents.summarizer import summarizer_agent
import uuid

def run_pipeline(contract_text: str):
    trace_id = f"trace-{uuid.uuid4().hex[:8]}"
    print(f"Starting pipeline Trace: {trace_id}")
    state = ContractState(
        trace_id=trace_id,
        contract_id="FDA-001",
        clauses=[],
        deviations=[],
        review_loops=0,
        needs_human=False
    )
    state = extractor_agent(state)
    print(f"Extractor found {len(state.clauses)} clauses")
    state = reviewer_agent(state)
    print(f"Reviewer found {len(state.deviations)} deviations")
    state = risk_scorer_agent(state)
    print("Risk score calculated")
    state = summarizer_agent(state)
    print("SUCCESS! Memo created")
    print(state.memo)
    return state

if __name__ == "__main__":
    run_pipeline("This is a dummy FDA contract for testing")