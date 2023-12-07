import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
env_api_host = os.environ.get("PATHWAY_REST_CONNECTOR_HOST", "127.0.0.1:8080")

# Sidebar for user input
with st.sidebar:
    st.markdown("## API Configuration")
    st.markdown("Note that you need to run the backend service first to use the app.")
    api_host = st.text_input("Pathway backend API Address", value=env_api_host)

    st.markdown("## How to query your data\n")
    st.markdown(
        """Enter your question, optionally
ask to be alerted.\n"""
    )
    st.markdown(
        "Example: 'When does the magic cola campaign start? Alert me if the start date changes'",
    )
    st.markdown(
        """[View the source code on GitHub](
https://github.com/pathway-labs/drive-alert)"""
    )
    st.markdown("## Current Alerts:\n")

# Streamlit UI elements
st.title("Google Drive notifications with LLM")

prompt = st.text_input("How can I help you today?")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    for message in st.session_state.messages:
        if message["role"] == "user":
            st.sidebar.text(f"📩 {message['content']}")

    url = f"http://{api_host}"
    
    data = {"query": prompt, "user": "user"}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        response = response.json()
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.error(
            f"Failed to send data to Discounts API. Status code: {response.status_code}"
        )