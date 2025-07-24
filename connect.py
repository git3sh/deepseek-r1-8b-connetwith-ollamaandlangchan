from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st

# Display app title including model name/version
st.title("Langchain-DeepSeek-R1:8b Chatbot App")

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

# Use the deepseek-r1:8b model as requested
model = OllamaLLM(model="deepseek-r1:8b")

chain = prompt | model


question = st.chat_input("Enter your question here")
if question: 
    st.write(chain.invoke({"question": question}))