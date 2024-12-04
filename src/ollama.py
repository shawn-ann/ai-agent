import ollama
import json
import requests
import time
import os
import logging

def do_math(a:int, op:str, b:int)->str:
    """
    Do basic math operations
    a: The first operand
    op: The operation to perform (one of '+', '-', '*', '/')
    b: The second operand
    """
    res = "Nan"
    if op == "+":
        res = str(int(a) + int(b))
    elif op == "-":
        res = str(int(a) - int(b))
    elif op == "*":
        res = str(int(a) * int(b))
    elif op == "/":
        if int(b) != 0:
            res = str(int(a) / int(b))
    return res

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

tools=[
    {
        "type": "function",
        "function": {
            "name": "do_math",
            "description": "Do basic math operations",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "int",
                        "description": "The first operand"
                    },
                    "op": {
                        "type": "str",
                        "description": "The operation to perform (one of '+', '-', '*', '/')"
                    },
                    "b": {
                        "type": "int",
                        "description": "The second operand"
                    }
                },
                "required": [
                    "a",
                    "op",
                    "b"
                ]
            }
        }
    },
]

logging.debug("Tools:")
logging.debug(json.dumps(tools, indent=4))
functions_desc = [ f["function"]["description"] for f in tools ]
print("I am a chatbot able to do run some functions.", "Functions:\n\t",  "\n\t".join(functions_desc))
print()
functions = {function["function"]["name"]: globals()[function["function"]["name"]] for function in tools }

messages = [('system', "You are an assistant with access to tools, if you do not have a tool to deal with the user's request but you think you can answer do it so, if not explain your capabilities")]
while True:
    try:
        query = input()
    except EOFError:
        break
    if query == "quit":
        break
    if query.strip() == "":
        continue
    messages.append(("user", query))
    response = ollama.chat(
        model='llama3.1',
        messages=[ {'role': role, 'content': content} for role,content in messages ],
        tools=tools,
    )

    if response['message']['content'] == "":
        tools_calls = response['message']['tool_calls']
        logging.debug(tools_calls)
        result = use_tools(tools_calls, functions)
    else:
        result = response['message']['content']
    print(result)
    messages.append(("assistant", result)