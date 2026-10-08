from typing import List , TypedDict , Optional
from src.utils.objects import Analyst

class GenerateAnalystState(TypedDict):
    topic: str
    max_analysts: int # number of analyst
    human_feedback: Optional[str]
    analysts: Optional[List[Analyst]]
    
