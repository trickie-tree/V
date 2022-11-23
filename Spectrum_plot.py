import streamlit as st
import pandas as pd
import numpy as np

def main_page():
    st.markdown("Home page")
    st.sidebar.markdown("Home page 🎈")

    st.write("""
    The aim of this app is to process and plot a vibrational spectroscopy spectrum

    Index:
        Page 2: CSV file format
        Page 3: Plot spectrum
    """)

def page2():
    st.markdown("Page 2: CSV file format")
    st.sidebar.markdown("# Page 2: CSV file format")

    st.write("""
    This page will take the spectrum file (in wdf. format)
    and automatically save the spectrum in CSV format, in the
    conformation that the spectrum plot on page 3 expects.
    """)

def page3():
    st.markdown("Page 3: Plot spectrum")
    st.sidebar.markdown("Page 3: Plot spectrum")

    st.write("""
    The aim of this page is to plot a spectrum from a 
    csv file dropped by the user into the file drop below
    """)
    
    dataframe = [] 
    uploaded_file = st.file_uploader('files', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
    
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file).set_index('Wavenumbers')
    
    if len(dataframe) > 0:
        st.line_chart(dataframe)

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
