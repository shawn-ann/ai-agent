# ai-agent
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

### 3. Run the agent
```bash
%python -m ai_agent
```

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

# chatui
## 1. install hugging face chatui
```bash
# https://github.com/huggingface/chat-ui
git clone https://github.com/huggingface/chat-ui
cd chat-ui
npm install    
docker run --name mongodb -d -p 27017:27017 mongodb/mongodb-community-server   

```
## 2. update env file
```

### MongoDB ###
MONGODB_URL=mongodb://localhost:27017 #your mongodb URL here, use chat-ui-db image if you don't want to set this
MONGODB_DB_NAME=root
MONGODB_DIRECT_CONNECTION=false

MODELS=`[
    {
      "name": "llama/llama3.2",
      "description": "Nous Research's latest Hermes 3 release in 8B size.",
      "promptExamples": [
        {
          "title": "Write an email from bullet list",
          "prompt": "As a restaurant owner, write a professional email to the supplier to get these products every week: \n\n- Wine (x10)\n- Eggs (x24)\n- Bread (x12)"
        }, {
          "title": "Code a snake game",
          "prompt": "Code a basic snake game in python, give explanations for each step."
        }, {
          "title": "Assist in a task",
          "prompt": "How do I make a delicious lemon cheesecake?"
        }
      ],
      "endpoints": [{
             "type" : "openai",
             "baseURL": "http://localhost:11434/llama3.2",
             "extraBody": {
               "repetition_penalty": 1.2,
               "top_k": 50,
               "truncate": 1000
             }
           }]
    }
]`

``` 

## 3. Run the chatui
```bash
   
npm run dev -- --open
```

## 4. install open webui

```bash
# With GPU Support: Utilize GPU resources by running the following command:
docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
# For CPU Only: If you're not using a GPU, use this command instead:
docker run -d -p 3000:8080 -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
# Refer to https://github.com/open-webui/open-webui
```