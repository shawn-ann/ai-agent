from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from typing import List
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0,
    base_url="http://localhost:11434",
)

messages = [
    (
        "system",
        "You are a helpful assistant that answer users question.",
    ),
    ("human", "今天天气怎么样？"),
]
ai_msg = llm.invoke(messages)
print(ai_msg)

# @tool
# def validate_user(user_id: int, addresses: List[str]) -> bool:
#     """Validate user using historical addresses.
#
#     Args:
#         user_id (int): the user ID.
#         addresses (List[str]): Previous addresses as a list of strings.
#     """
#     return True
#
#
# llm = ChatOllama(
#     model="llama3.2",
#     temperature=0,
# ).bind_tools([validate_user])
#
# result = llm.invoke(
#     "Could you validate user 123? They previously lived at "
#     "123 Fake St in Boston MA and 234 Pretend Boulevard in "
#     "Houston TX."
# )
# result.tool_calls