from pydantic import BaseModel
from typing import List, Optional, Any

class ContractState(BaseModel):
    trace_id: str
    contract_id: str
    clauses: List[Any] = []
    deviations: List[Any] = []
    review_loops: int = 0
    needs_human: bool = False
    risk_score: float = 0.0
    memo: Optional[str] = None