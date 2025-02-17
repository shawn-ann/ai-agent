from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
# Define the tools for the agent to use
@tool
def search_weather(location: str):
    """Search weather for the provied location'."""
    # This is a placeholder, but don't tell the LLM that...
    return f"The weather in {location} is sunny with temperatures 29-35°C."


tools = [search_weather]

# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(base_url="https://use.52apikey.cn/v1")

from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3-groq-tool-use:latest",base_url="http://localhost:11434")

# Initialize memory to persist state between graph runs
checkpointer = MemorySaver()

agent_executor = llm.bind_tools(tools)

response = agent_executor.invoke([HumanMessage(content="hi!")])
print(response.content)

response = agent_executor.invoke([HumanMessage(content="What's the weather in SF?")])

print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")


