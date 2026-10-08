from pydantic import BaseModel , Field
from typing import List

# create Our object analyst 
class Analyst(BaseModel):
    affiliation : str = Field(description="Primary Affiliation of the analyst")
    name : str = Field(description="Name of the analyst")
    role: str = Field(description="Role of the analyst in the context of the topic")
    description: str = Field(description="A brief description of the analyst's background and expertise")


    @property
    def persona(self) -> str:
        return f"""
            You are {self.name},
            working at {self.affiliation}.
            Your expertise is {self.role}.
            {self.description}
        """


def Perspective(BaseModel):
    analyst: List[analyst] = Field(description="Comprehensive List of Analysts to consider for the topic")
    

    
        