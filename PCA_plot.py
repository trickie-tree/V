import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def main_page():
    st.markdown("Home page")
    st.sidebar.markdown("Home page")

    st.write("""
    The aim of this app is to process and plot a vibrational spectroscopy spectrum

    Index:
        Page 2: Cumulative explained variance (CEV) plot
        Page 3: Score plot
        Page 4: Loading plot
    """)

def page2():
    st.markdown("Page 2: CEV plot")
    st.sidebar.markdown("Page 2: CEV plot")

    st.write("""
    This page will plot the cumulative explained variance,
    indicating the number of principal components that relate
    to an acceptable ammount of variance within the dataset.
    """)

    dataframe2 = [] 
    uploaded_file = st.file_uploader('files', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
    
    if uploaded_file is not None:
        # Can be used wherever a "file-like" object is accepted:
        dataframe2 = pd.read_csv(uploaded_file).set_index('Wavenumbers')
    
    
    # The next step is to make a csv file with the labels in the 
    # first column and add a few lines selecting the labels and dataset
    # from dataframe2 at the beginning of the if statement 

    if len(dataframe2) > 0:
        pca = PCA().fit(dataframe2)
        fig, ax = plt.subplots()
        ax.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],np.cumsum(pca.explained_variance_ratio_[0:15]))
        ax.xlabel('number of components')
        ax.ylabel('cumulative explained variance')
        ax.title('Explained variance', fontsize = 10)
        ax.grid()    

        st.write(fig)

def page3():
    st.markdown("Page 3: Score plot")
    st.sidebar.markdown("Page 3: Score plot")

    st.write("""
    The aim of this page is to plot two principal components 
    against ech other, showing their score plot. 
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
