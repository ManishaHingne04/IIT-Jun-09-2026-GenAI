# install langgraph
# pip3 install langgraph 

# import graph and required nodes
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

# define the state schema
class AppState(TypedDict):
    messages: str
    attribute1: int

# define a tool
def tool1(state: AppState):
    print(f"tool1 executed")
    print(f"state => {state}")

    # return the output which will be used as an input for the next tool (node)
    return {
        "messages": "new state updated by tool1",
        "attribute1": 100
    }

# create the workflow (graph)
workflow = StateGraph(AppState)

# add a node
workflow.add_node("node1", tool1)

# add the required edges
workflow.add_edge(START, "node1")
workflow.add_edge("node1", END)

# compile the workflow and create the graph
graph = workflow.compile()

# send the data to the graph
graph.invoke({
    "messages": "user question",
    "attribute1":
})