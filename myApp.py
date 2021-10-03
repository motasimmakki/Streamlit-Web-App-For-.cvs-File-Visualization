import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
'''
    ## Polulation Status: 
'''
)

st.sidebar.subheader("Upload Files Here :")

uploaded_file = st.sidebar.file_uploader(
    label = "Upload your .cvs or excel file here."
)

def showGraph(filename):
    obj = pd.read_csv(filename)
    st.line_chart(obj)

if uploaded_file is not None:
    try:
        st.write(
        '''
            ### Observation :
        '''
        )
        showGraph(uploaded_file)
    except:
        print("Somthing goes wrong!")


