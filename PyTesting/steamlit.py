import streamlit as st
import pandas as pd

st.write("""
# My first app 
Hello *world!*
""")
file = st.file_uploader("Pick a file")

date = st.date_input("Pick a date")