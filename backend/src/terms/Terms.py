from enum import Enum
from typing import Dict
from TermType import TermType

class Terms:
    def __init__(self, id: int, type: TermType, description: str, data: Dict):
        self.id = id  
        self.type = type  
        self.description = description 
        self.data = data  

    def __repr__(self) -> str:
        return (f"Terms(id={self.id}, type={self.type.name}, description='{self.description}', "
                f"data={self.data})")
