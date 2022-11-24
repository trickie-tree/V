import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


def home_page():

    # Task 1:
    # Formatting the app for improved user experiance

    # Task 2: 
    # Add a page for CSV formatting from wdf

    # Task 3: 
    # Add a page for the selection of PCs  

    st.markdown("Home page")
    st.sidebar.markdown("Home page")

    st.write("""
    The aim of this app is to process and plot a vibrational spectroscopy spectrum\n
    \n
    Index:\n
        Page 1: Formatting wdf file for CSV\n
        Page 2: Cumulative explained variance (CEV) plot\n
        Page 3: PC selection\n
        Page 4: Score plot\n
        Page 5: Loading plot
    """)


def page1():
    st.markdown("Page 1: CSV format")
    st.sidebar.markdown("Page 1: CSV format")
    # Add the wdf to csv formatting

def page2():

    # Task 1:
    # Format the plot, nicer plot

    # Task 2:
    # Have somthing print out the PCs representing a suitable ammount of variance
    # Potentially a method of setting a limit

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
    pass
    # Need to add the PC select page

def page4():

    # Task 1:
    # Automate x and y axis ranges

    # Task 2:
    # Build in a method of varying the number of classes

    st.markdown("Page 4: Score plot")
    st.sidebar.markdown("Page 4: Score plot")

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


def page5():

    # Task 1:
    # Improve the plot (wavenumbers, y-axis range, formatting)

    # Task 2:
    # Looking to include an automatic method for identifying
    # the top number of peaks, ideally using a slider
    
    st.markdown("Page 5: Loadings plots")
    st.sidebar.markdown("Page 5: Loadings plots")

    st.write('Loadings plot page')

    PC = ''
    
    PC = st.text_input("Principal component: ")
    
    dataframe2 = [] 

    if len(PC) > 0:
        
        uploaded_file2 = st.file_uploader('files', accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="hidden")
        if uploaded_file2 is not None:
            df2 = pd.read_csv(uploaded_file2)
            dataframe2 = df2.drop(['400','2112','diagnostic'],axis=1)
         
    if len(dataframe2) > 0:
        pca = PCA().fit(dataframe2)
        loadings = pca.components_.T
        Loadings = pd.DataFrame(loadings)

        PC_loading = pd.DataFrame(Loadings.iloc[:,int(PC)])

        fig2, ax2 = plt.subplots()
        ax2.plot(PC_loading) 
        ax2.set_title('PC' + str(PC) + ' Loading plot')
        ax2.grid()

        st.write(fig2)    


page_names_to_funcs = {
    
    # Need to update the page names,
    # perhaps after all pages are sorted  

    "Home Page": home_page,
    "Page 1 (CSV format)": page1,
    "Page 2 (CEV plot)": page2, 
    "Page 3 (PC select)": page3,
    "Page 4 (Score plot)": page4,
    "Page 5 (Loading plot)": page5,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
