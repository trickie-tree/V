import streamlit as st
import pandas as pd


st.write("""
# Spectrum plot 
*The aim of this page is to provide a web app that allows a
user to drop a csv file of a spectrum (row 1) and range (row 2)
into the file drop below and plot the spectrum*
""")

dataframe = []

uploaded_file = st.file_uploader('files', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
if uploaded_file is not None:
    
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file).set_index('Wavenumbers')

    

if len(dataframe) > 0:
    st.line_chart(dataframe)
