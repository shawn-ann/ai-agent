from langchain_core.messages import AIMessage
from typing import List
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field


from typing_extensions import Annotated, TypedDict

@tool
def add(a: int, b: int) -> int:
    """Add two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two integers.

    Args:
        a: First integer
        b: Second integer
    """
    return a * b


tools = [add, multiply]



llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://localhost:11434",
)
llm_with_tools = llm.bind_tools(tools, tool_choice="multiply")



query = "What is 3 * 12?"
result = llm_with_tools.invoke(query)
print(result)
print(result.tool_calls)

#https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.tool_example_to_messages.html 