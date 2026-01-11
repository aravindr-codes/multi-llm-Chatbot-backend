import os

# set your API key (or set OPENAI_API_KEY in your environment instead)
os.environ["OPENAI_API_KEY"] = "YOUR_KEY"

# modern imports
from langchain_openai import ChatOpenAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType

# Create the Wikipedia tool (requires `wikipedia` package)
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# pass the tool instance directly
tools = [wiki]

# Use a ChatOpenAI model with zero randomness
llm = ChatOpenAI(temperature=0, model="gpt-4o")  

# Combine reasoning (LLM) and tools into one agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

goal = "What are the top AI coding assistants and what makes them unique?"
response = agent.run(goal)
print("\nAgent's response:\n", response)
