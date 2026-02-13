from dotenv import load_dotenv
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
import streamlit as st

load_dotenv(override=True)

st.title("Ollama Gemma Chatbot with Prompt Template")

role = st.selectbox("Select a role for Gemma:", ["AI Developer", "AI Teacher", "Data Scientist", "AI Researcher"])
goal = st.text_input("What is your goal for this conversation?")
context = st.text_area("Provide any additional context for Gemma:")
prompt_text = """ You are a {AI_role} and your goal is to {AI_goal}.
Here is some additional context for you: {AI_context}
Answer the user's question based on the above information.
"""
template = PromptTemplate(template=prompt_text, 
                          input_variables=['AI_role', 'AI_goal', 'AI_context'], 
                          validate_template=True)

prompt = template.invoke({'AI_role': role, 'AI_goal': goal, 'AI_context': context})

model = Ollama(model="gemma3:1b")

if st.button("Ask Gemma"):
    response = model.invoke(prompt)
    st.write(response)  