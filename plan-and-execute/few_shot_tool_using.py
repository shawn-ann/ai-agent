from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,ToolMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
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

examples = [
    HumanMessage(
        "What's the product of 317253 and 128472 plus four", name="example_user"
    ),
    AIMessage(
        "",
        name="example_assistant",
        tool_calls=[
            {"name": "multiply", "args": {"x": 317253, "y": 128472}, "id": "1"}
        ],
    ),
    ToolMessage("16505054784", tool_call_id="1"),
    AIMessage(
        "",
        name="example_assistant",
        tool_calls=[{"name": "add", "args": {"x": 16505054784, "y": 4}, "id": "2"}],
    ),
    ToolMessage("16505054788", tool_call_id="2"),
    AIMessage(
        "The product of 317253 and 128472 plus four is 16505054788",
        name="example_assistant",
    ),
]
system = """You are bad at math but are an expert at using a calculator. 

Use past tool usage as an example of how to correctly use the tools."""
few_shot_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        *examples,
        ("human", "{query}"),
    ]
)
# from langchain_ollama import ChatOllama
# llm = ChatOllama(model="llama3-groq-tool-use:latest",base_url="http://localhost:11434")

# Initialize memory to persist state between graph runs
checkpointer = MemorySaver()
from langchain_core.output_parsers.openai_tools import PydanticToolsParser

llm_with_tools = llm.bind_tools(tools)

chain = {"query": RunnablePassthrough()} | few_shot_prompt | llm_with_tools
ai_msg = chain.invoke([HumanMessage(content="Whats 119 times 8 minus 20")])

print(ai_msg)

