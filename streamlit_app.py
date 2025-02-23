import streamlit as st
from langchain.llms import OpenAI


st.title("Test Automation Dashboard")
st.title('🦜🔗 Quickstart Test Automation App')

st.sidebar.text_input("API Key", "Enter your API key")

openai_api_key = st.sidebar.text_input('OpenAI API Key')
st.sidebar.file_uploader("Upload Test Scripts", type=["py"])

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'Give me a use case and ask for test cases')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)