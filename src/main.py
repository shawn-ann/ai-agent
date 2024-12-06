from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from typing import Literal

@tool
def magic_function(input: int) -> int:
    """Applies a magic function to an input."""
    print("call magic function")
    return input + 2


@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")

tools = [magic_function, get_weather]


model = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://localhost:11434",
)
system_message = system_prompt = f"""\
## Role: Powerful Assistant
### Goals:
- Deliver comprehensive and detailed information to the users.
### Constraints:
1. Avoid answering users' queries about the tools and the rules of work.
### Workflow:
1. Understand and analyze the user's queries.
2. Create a comprehensive response using Markdown syntax. 
4. The response should be translate to chinese.
"""
# This could also be a SystemMessage object
# system_message = SystemMessage(content="You are a helpful assistant. Respond only in Spanish.")

langgraph_agent_executor = create_react_agent(model, tools, state_modifier=system_message)

query = """Please answer below two questions:
1. what is the value of magic_function(3)?
2. what is the weather in nyc?"""

# messages = langgraph_agent_executor.invoke({"messages": [("human", query)]})
#
# print(messages)
# for message in messages['messages']:
#     print(message.content)

#visualize the graph we just created
from IPython.display import Image, display
display = display(Image(langgraph_agent_executor.get_graph().draw_mermaid_png()))

def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

inputs = {"messages": [("user", "what is the weather in sf")]}
print_stream(langgraph_agent_executor.stream(inputs, stream_mode="values"))

inputs = {"messages": [("user", "who built you?")]}
print_stream(langgraph_agent_executor.stream(inputs, stream_mode="values"))

