import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def main_page():
    st.markdown("Home page")
    st.sidebar.markdown("Home page")

    st.write("""
    The aim of this app is to process and plot a vibrational spectroscopy spectrum\n
    \n
    Index:\n
        Page 2: Cumulative explained variance (CEV) plot\n
        Page 3: Score plot\n
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

    dataframe0 = [] 
    uploaded_file0 = st.file_uploader('files', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
    
    if uploaded_file0 is not None:
        # Can be used wherever a "file-like" object is accepted:
        df0 = pd.read_csv(uploaded_file0)
        dataframe0 = df0.drop(['400','2112','diagnostic'],axis=1)
        #labels = df0['diagnostic']
        #labels = np.array(labels)
    

    if len(dataframe0) > 0:
        pca = PCA().fit(dataframe0)
        
        fig0, ax0 = plt.subplots()
        ax0.plot([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],np.cumsum(pca.explained_variance_ratio_[0:15]))
        ax0.set_xlabel('number of components')
        ax0.set_ylabel('cumulative explained variance')
        ax0.set_title('Explained variance', fontsize = 10)
        ax0.grid()    

        st.write(fig0)

def page3():
    st.markdown("Page 3: Score plot")
    st.sidebar.markdown("Page 3: Score plot")

    st.write("""
    The aim of this page is to plot two principal components 
    against ech other, showing their score plot. 
    """)
    First_pc = ''
    Second_pc = ''

    First_pc = st.text_input("First PC: ")
    Second_pc = st.text_input("Second PC: ")

    if len(First_pc) > 0 and len(Second_pc) > 0:
        dataframe1 = [] 
        uploaded_file1 = st.file_uploader('files', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
        if uploaded_file1 is not None:
            df1 = pd.read_csv(uploaded_file1)
            dataframe1 = df1.drop(['400','2112','diagnostic'],axis=1)
            labels = df1['diagnostic']
            labels = np.array(labels)

        
        if len(dataframe1) > 0:
    
            transformer = PCA(n_components=8)
            X_pc = transformer.fit_transform(dataframe1)
            DF = pd.DataFrame(X_pc, columns = ['1', '2','3', '4', '5', '6', '7', '8'])
        
            fig1, ax1 = plt.subplots()
            #ax1 = fig1.add_subplot(1,1,1) 
            ax1.set_xlabel('Principal Component' + str(First_pc), fontsize = 15)
            ax1.set_ylabel('Principal Component' + str(Second_pc), fontsize = 15)
            ax1.set_title('2 component PCA', fontsize = 20)
            targets = [np.unique(labels)[0], np.unique(labels)[1]]
            colors = ['r','b']
            for target, color in zip(targets,colors):
                indicesToKeep = labels == target
                ax1.scatter(DF.loc[indicesToKeep, str(First_pc)]
                    , DF.loc[indicesToKeep, str(Second_pc)]
                    , c = color
                    , s = 50)
            ax1.legend(targets)
            ax1.grid()

            st.write(fig1)

def page4():

    st.write('#This will be the loadings plot page')
        

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
