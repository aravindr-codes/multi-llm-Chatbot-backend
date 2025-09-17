from typing import TypedDict
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END


# Define state structure
class AgentState(TypedDict):
    input: str
    code: str
    review: str
    final_output: str


# Agent 1: Coder
def coder_agent(state: AgentState):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = f"Write Python code that {state['input']}."
    response = llm.invoke(prompt)
    return {"code": response.content}


# Agent 2: Reviewer
def reviewer_agent(state: AgentState):
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    prompt = f"Review the following Python code and suggest improvements:\n\n{state['code']}"
    response = llm.invoke(prompt)
    return {"review": response.content}


# Postprocess step
def postprocess(state: AgentState):
    final = f"Generated Code:\n{state['code']}\n\nReviewer Feedback:\n{state['review']}"
    return {"final_output": final}


# Build the LangGraph workflow
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("coder", coder_agent)
graph.add_node("reviewer", reviewer_agent)
graph.add_node("postprocess", postprocess)

# Define edges
graph.set_entry_point("coder")
graph.add_edge("coder", "reviewer")
graph.add_edge("reviewer", "postprocess")
graph.add_edge("postprocess", END)

# Compile app
app = graph.compile()


# Run it
if __name__ == "__main__":
    task = "prints the Fibonacci sequence up to 10"
    result = app.invoke({"input": task})
    print("=== Final Output ===")
    print(result["final_output"])
