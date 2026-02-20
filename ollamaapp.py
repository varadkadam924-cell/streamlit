from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#creating my prompts
prompts = ChatPromptTemplate.from_messages(
     [
        ("system",' you are helpful assistant , please respond to the question asked '),
        ("user","Question:{question}")
     
     ]
)

st.title('Langvhain demo Chat App with gemma:2b')
input_text = st.text_input ('write our prompt: ')

llm = Ollama(model="gemma2:2b")
output_parser =  StrOutputParser()
chain = prompts|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
