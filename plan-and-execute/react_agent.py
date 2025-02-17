from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_community.agent_toolkits import FileManagementToolkit
from tempfile import TemporaryDirectory
working_directory = TemporaryDirectory()
toolkit = FileManagementToolkit(
    root_dir=str(working_directory.name)
)  # If you don't provide a root_dir, operations will default to the current working directory
file_tools = toolkit.get_tools()

# Define the tools for the agent to use
@tool
def search_temperature(location: str):
    """Search today's temperature according to the location."""
    if location == "Shenzhen":
        return 19
    if location == "Dalian":
        return 2
    return 21
@tool
def search_clothes(temperature: int):
    """Search for what you need to wear based on the temperature."""
    if(temperature < 10):
        return f"Need to wear a coat."
    if(temperature < 20):
        return f"Need to wear a sweater."
    return f"Need to wear a T-shirt."


tools = [search_temperature,search_clothes]
# add file tools into tools array
tools.extend(file_tools)

from langchain_openai import ChatOpenAI

# llm = ChatOpenAI(model="gpt-4o", base_url="https://use.52apikey.cn/v1")
from langchain_ollama import ChatOllama
llm = ChatOllama(model="llama3-groq-tool-use:latest",base_url="http://localhost:11434")


# Initialize memory to persist state between graph runs
checkpointer = MemorySaver()
prompt = """
Your are a smart assistant. Please think step-by-step when answering the new question, and provide a well-read answer to the user.

You are given a number of tools as functions, you must use one of those tools and fillup 
all the parameters of those tools ,whose answers you will get from the given situation.

First analyze the given situation to fully understand what is the intention of the user,
what they need and exactly which tool will fill up that necessity.
Then look into the parameters and extract all the relevant informations to fill up the 
parameter with right values.
Finally, call the tool with the right parameters and provide the answer to the user.

"""
# """
# ---For example---
# Question:"I am in Shanghai, what should I wear today?".
# Thinking:
# first, you need to search the temperature in Shanghai, and then search the clothes based on the temperature.
# second, you need to call search_temperature with location "Shanghai" and call search_clothes with the temperature you get from search_temperature.
# Answer: The weather in Shanghai is sunny with temperatures 29-35°C. Need to wear a T-shirt.
# ---For example---
# """
agent_executor = create_react_agent(llm, tools,prompt=prompt, checkpointer=checkpointer)

config = {"configurable": {"thread_id": 42}}

# response = agent_executor.invoke(
#     {"messages": [HumanMessage(content="write 'aaa' into file 'example.txt' and then list all the files in the directory")]}, config
# )
# print(response["messages"])
# response = agent_executor.invoke(
#     {"messages": [HumanMessage(content="whats the weather in BeiJing?")]}, config
# )
# print(response["messages"])

# for chunk in agent_executor.stream(
#         {"messages": [HumanMessage(content="write 'aaa' into file 'example.txt' and then list all the files in the directory")]}, config
# ):
#     print(chunk)
#     print("----")

for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content="I am in Dalian, what should I wear today?")]}, config
):
    print(chunk)
    print("----")
