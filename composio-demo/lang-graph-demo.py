from typing import Literal
from langchain_ollama import ChatOllama
from langgraph.graph import MessagesState, StateGraph
from langgraph.prebuilt import ToolNode
from composio_langgraph import Action, ComposioToolSet, App
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain import hub
from langgraph.prebuilt import create_react_agent

prompt = hub.pull("hwchase17/react")

composio_toolset = ComposioToolSet()

tools = composio_toolset.get_tools(
    apps=[App.GITHUB]
)
tool_node = ToolNode(tools)
model = ChatOllama(model="qwen2:7b",temperature=0, streaming=True)
task = "Star a repo composiohq/composio on GitHub"

agent = create_react_agent(model, tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute using agent_executor
inputs = {"messages": [("user",  task)]}
res = agent_executor.invoke(input=inputs)
print(res)

SELECT DATE_FORMAT(created_at, '%Y%m'), COUNT(1) FROM `job_instance` WHERE created_by NOT IN ('gengxin.zhang', 'xin.su', 'ying.sun', 'buvanesh.kg', 'yifan.xu', 'shuai.an', 'lin.song') AND DATE_FORMAT(created_at, '%Y%m') >= '202401' AND DATE_FORMAT(created_at, '%Y%m') <= '202412' GROUP BY DATE_FORMAT(created_at, '%Y%m');