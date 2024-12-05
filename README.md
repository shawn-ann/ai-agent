# ai-agent

# 1. Install the ollama and llama 3.2
```bash
docker pull ollama/ollama
# Run ollama with CPU
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
# Run model locally
docker exec -it ollama ollama run llama3.2
```
Refer to https://hub.docker.com/r/ollama/ollama

# 2. install langchain-ollama
```bash
%pip install -U langchain-ollama
%pip install langgraph

```
Refer to https://python.langchain.com/docs/integrations/chat/ollama/

# 3. Run the agent
```bash
%python -m ai_agent
```