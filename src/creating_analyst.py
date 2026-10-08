from src.utils.nodes import create_analyst
from langgraph.graph import StateGraph , START , END
from src.utils.state import GenerateAnalystState
from dotenv import load_dotenv

load_dotenv()


## Create our graph

builder = StateGraph(GenerateAnalystState)

builder.add_node("create_analyst" , create_analyst)


## Define edges
builder.add_edge(START , "create_analyst")
builder.add_edge("create_analyst" , END)

## Compile the graph
graph_analyst = builder.compile()