```markdown
# event-rag-agent

A minimal agentic RAG system that fetches guest details, weather, and model stats via LangGraph and a Hugging Face LLM.

## Setup
1. Clone and enter the repo:
   ```bash
   git clone https://github.com/mozaloom/event-rag-agent.git
   cd event-rag-agent
   ```
2. Install dependencies:
   ```bash
   pip install python-dotenv langgraph langchain langchain-huggingface langchain-community
   ```  
   - Loads `.env` vars with `load_dotenv()`  ([python-dotenv - PyPI](https://pypi.org/project/python-dotenv/?utm_source=chatgpt.com))  
   - Orchestrates tools via LangGraph  ([langchain-ai/langgraph: Build resilient language agents as graphs.](https://github.com/langchain-ai/langgraph?utm_source=chatgpt.com))  
   - Uses `HuggingFaceEndpoint` + `ChatHuggingFace` for LLM calls  ([ChatHuggingFace - ️ LangChain](https://python.langchain.com/docs/integrations/chat/huggingface/?utm_source=chatgpt.com))  

## Configuration
- Copy `.env.example` → `.env` and set:
  ```
  HF_TOKEN=<your_huggingface_api_token>
  ```

## Usage
- **CLI**:  
  ```bash
  python app.py
  ```
- **Docker** (optional):
  ```bash
  docker build -t event-rag-agent .
  docker run -e HF_TOKEN=$HF_TOKEN -p 8000:8000 event-rag-agent
  ```

## License
MIT
```