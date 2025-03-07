from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,ToolMessage
# Define the tools for the agent to use
@tool
def add(a: int, b: int) -> int:
    """Adds a and b.

    Args:
        a: first int
        b: second int
    """
    return a + b


@tool
def multiply(a: int, b: int) -> int:
    """Multiplies a and b.

    Args:
        a: first int
        b: second int
    """
    return a * b


tools = [add,multiply]

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo",base_url="https://use.52apikey.cn/v1")

# from langchain_ollama import ChatOllama
# llm = ChatOllama(model="llama3-groq-tool-use:latest",base_url="http://localhost:11434")

# Initialize memory to persist state between graph runs
checkpointer = MemorySaver()
from langchain_core.output_parsers.openai_tools import PydanticToolsParser

llm_with_tools = llm.bind_tools(tools)

query="What is 3 * 12? Also, what is 11 + 49?"
messages = [HumanMessage(query)]
for chunk in llm_with_tools.stream(messages):
    print(chunk, end="", flush=True)

# ai_msg = llm_with_tools.invoke(messages)
# messages.append(ai_msg)
# for tool_call in ai_msg.tool_calls:
#     selected_tool = {"add": add, "multiply": multiply}[tool_call["name"].lower()]
#     tool_output = selected_tool.invoke(tool_call["args"])
#     messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))
#
#
# for message in messages:
#     print(message)
