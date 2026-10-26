from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class RiskLevel(str, Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class Clause(BaseModel):
    clause_number: str
    clause_type: str
    text: str

class Deviation(BaseModel):
    clause_number: str
    clause_type: str
    playbook_rule_id: str
    expected_deviation: str
    risk: RiskLevel
    reason: str
    fallback: str

class ContractState(BaseModel):
    trace_id: str
    contract_id: str
    clauses: List[Clause] = []
    deviations: List[Deviation] = []
    review_loops: int = 0
    needs_human: bool = False
    memo: Optional[str] = None