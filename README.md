# AI-Agent
记录学习AI-Agent的过程，详细成果记录在[doc文件夹](./doc)中


## Ollama
### 1. Install the ollama and llama 3.2
```bash
docker pull ollama/ollama
# Run ollama with CPU
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
# Run model locally
docker exec -it ollama ollama run llama3.2
```
Refer to https://hub.docker.com/r/ollama/ollama

### 2. install langchain-ollama
```bash
%pip install -U langchain-ollama
%pip install langgraph
# UI
%pip install flask tk

```
Refer to https://python.langchain.com/docs/integrations/chat/ollama/


## Dify ecosystem
https://github.com/langgenius/dify
### 1. install dify
```bash
git clone https://github.com/langgenius/dify.git
cd dify
cd docker
cp .env.example .env
docker compose up -d
```
### 2. access the Dify dashboard in your browser at http://localhost/install and start the initialization process.

## 3. install open webui

```bash
# With GPU Support: Utilize GPU resources by running the following command:
docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
# For CPU Only: If you're not using a GPU, use this command instead:
docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
# Refer to https://github.com/open-webui/open-webui
```