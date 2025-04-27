import os
import streamlit as st
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import AnyMessage, HumanMessage
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from retriever import guest_info_tool
from tools import weather_info_tool, hub_stats_tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import ToolNode
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition

# --- Load environment ---
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

# --- Streamlit page config ---
st.set_page_config(
    page_title="Alfred – Your Event RAG Agent",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("🎩 Alfred – Event RAG Agent")

# --- Initialize LLM & Tools once ---
@st.cache_resource(show_spinner=False)
def init_agent():
    # Web search tool
    search_tool = DuckDuckGoSearchRun()
    # HuggingFace LLM endpoint
    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        huggingfacehub_api_token=HF_TOKEN,
    )
    chat = ChatHuggingFace(llm=llm, verbose=False)
    tools = [guest_info_tool, search_tool, weather_info_tool, hub_stats_tool]
    chat_with_tools = chat.bind_tools(tools)

    # Build the state graph
    class AgentState(TypedDict):
        messages: Annotated[list[AnyMessage], add_messages]

    builder = StateGraph(AgentState)
    builder.add_node("assistant", lambda state: {"messages": [chat_with_tools.invoke(state["messages"])]})
    builder.add_node("tools", ToolNode(tools))
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges("assistant", tools_condition)
    builder.add_edge("tools", "assistant")
    return builder.compile()

alfred = init_agent()

# --- Initialize session state ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- Chat input & UI ---
user_input = st.chat_input("Type your message…")  # text input widget :contentReference[oaicite:2]{index=2}
if user_input:
    # Append human message
    st.session_state.history.append(HumanMessage(content=user_input))
    # Invoke agent
    response = alfred.invoke({"messages": st.session_state.history})
    ai_msg = response["messages"][-1]
    st.session_state.history.append(ai_msg)

# --- Render chat history ---
for msg in st.session_state.history:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)  # Display message in chat bubble :contentReference[oaicite:3]{index=3}
