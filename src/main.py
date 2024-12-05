from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

@tool
def magic_function(input: int) -> int:
    """Applies a magic function to an input."""
    print("call magic function")
    return input + 2


tools = [magic_function]


model = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://localhost:11434",
)
system_message = system_prompt = f"""\
You are an assistant that has access to a couple set of tools. if the tools can not be used then answer that "I have no idea about it.".
if user have more than one question then answer them one by one.
"""
# This could also be a SystemMessage object
# system_message = SystemMessage(content="You are a helpful assistant. Respond only in Spanish.")

langgraph_agent_executor = create_react_agent(model, tools, state_modifier=system_message)

query = """Please answer below two questions:
1. what is the value of magic_function(3)?"""

messages = langgraph_agent_executor.invoke({"messages": [("human", query)]})

print(messages)
for message in messages['messages']:
    print(message.content)
    # if message.tool_calls:
    #     print(message.tool_calls[0].tool.name)
    #     print(message.tool_calls[0].args)
