import streamlit as st 
import torch
from transformers import pipeline
import time

st.title ("English_Summarizer")
text = st.text_area ("Input Your Sentences", placeholder = "Write Here")
if st.button ("Summarize"):
  with st.spinner(text="In progress..."):  
    pipe = pipeline("summarization")
    container = st.container(border=True)
    result = pipe(text, max_length = 150, min_length = 30)
    "Summary"
    st.success (result[0]["summary_text"] )
    st.success('This is a success message!', icon="✅")

