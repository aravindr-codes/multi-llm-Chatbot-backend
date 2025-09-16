import os

os.environ["OPENAI_API_KEY"] = 
from langchain.agents import Tool
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper
# Create the Wikipedia tool
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
# Register the tool so the agent knows how to use it
tools = [
    Tool(
        name="Wikipedia",
        func=wiki.run,
        description="Useful for looking up general knowledge."
    )
]
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
# Use a GPT model with zero randomness for consistent output
llm = ChatOpenAI(temperature=0)
# Combine reasoning (LLM) and tools (Wikipedia) into one agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True  # Show thought process step-by-step
)