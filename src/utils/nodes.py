from dotenv import load_dotenv
from src.utils.state import GenerateAnalystState
from src.utils.model import llm
from src.utils.objects import Perspective 
from src.utils.prompts import analyst_instructions
from langchain.messages import SystemMessage , HumanMessage
load_dotenv()



## Create Nodes

def create_analyst(state:GenerateAnalystState):
    """
    Creates a list of analysts for the given topic.
    """

    topic = state["topic"]
    max_analysts = state["max_analysts"]
    human_feedback = state.get("human_feedback" , "")

    ## enforece structured output here
    structured_llm = llm.with_structured_output(Perspective)
    
    # System Msg
    system_msg = analyst_instructions.format(
        topic=topic,
        human_analyst_feedback=human_feedback,
        max_analysts=max_analysts
    )

    # Generate analyst
    analysts = structured_llm.invoke([SystemMessage(content=system_msg)] + [HumanMessage(content="Please Generate the set of analysts")])
    
    return {"analysts": analysts.analysts}