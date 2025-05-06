# Event RAG Agent

A minimal agentic RAG (Retrieval-Augmented Generation) system that fetches guest details, weather, and model statistics via LangGraph and a Hugging Face LLM.

![GitHub](https://img.shields.io/github/license/mozaloom/event-rag-agent) [![Docker Image CI](https://github.com/mozaloom/event-rag-agent/actions/workflows/docker-hub.yml/badge.svg)](https://github.com/mozaloom/event-rag-agent/actions/workflows/docker-hub.yml) [![CI](https://github.com/mozaloom/event-rag-agent/actions/workflows/main.yml/badge.svg)](https://github.com/mozaloom/event-rag-agent/actions/workflows/main.yml)

## Overview

This repository contains a production-ready agent that combines:

- **Retrieval**: Fetches relevant information from various sources
- **Augmentation**: Enhances raw data with context and processing
- **Generation**: Uses a Hugging Face LLM to generate responses
- **Orchestration**: Coordinates tools and workflow with LangGraph

## Repository Structure

```
.
├── DockerFile         # Container definition
├── LICENSE            # MIT License
├── Makefile           # Build automation
├── README.md          # This file
├── app.py             # Main CLI application
├── mylib              # Core library components
│   ├── retriever.py   # Data retrieval functionality
│   └── tools.py       # Tool definitions and utilities
├── requirements.txt   # Python dependencies
└── streamlit_app.py   # Streamlit web interface
```

## Setup

1. **Clone and enter the repository**:
   ```bash
   git clone https://github.com/mozaloom/event-rag-agent.git
   cd event-rag-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   - Copy `.env.example` to `.env`
   - Set your Hugging Face API token:
     ```
     HF_TOKEN=<your_huggingface_api_token>
     ```

## Dependencies

This project relies on:
- `python-dotenv`: Loads environment variables from `.env` file
- `langgraph`: Orchestrates tools in a graph-based workflow
- `langchain`: Provides LLM integration components
- `langchain-huggingface`: Connects to Hugging Face models
- `langchain-community`: Additional community integrations

## Usage

### Command Line Interface

```bash
python app.py
```

### Web Interface

```bash
streamlit run streamlit_app.py
```

### Docker Container

```bash
# Build the container
docker build -t event-rag-agent .

# Run the container
docker run -e HF_TOKEN=$HF_TOKEN -p 8000:8000 event-rag-agent
```

## Development

- Use the `Makefile` for common development tasks
- Run tests with `make test`
- Format code with `make format`

## License

This project is licensed under the [MIT License](LICENSE).