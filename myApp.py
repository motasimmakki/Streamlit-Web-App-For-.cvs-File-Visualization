import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
'''
    ## Polulation Status: 
'''
)

ob1 = pd.read_csv('./files/observations_1.csv')
ob2 = pd.read_csv('./files/observations_2.csv')
ob3 = pd.read_csv('./files/observations_3.csv')

st.write(
'''
    ### Observation 01:
'''
)
# st.dataframe(ob1)
st.line_chart(ob1)

st.write(
'''
    ### Observation 02:
'''
)
# st.dataframe(ob2)
st.line_chart(ob2)

st.write(
'''
    ### Observation 03:
'''
)
# st.dataframe(ob3)
st.line_chart(ob3)


