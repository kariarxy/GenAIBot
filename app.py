import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts 


# read csv from a github repo
# df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")
df=pd.read_csv("https://raw.githubusercontent.com/kariarxy/GenAIBot/main/retail_data.csv")

st.set_page_config(
    page_title = 'Real-Time Retail Data Dashboard',
    page_icon = '📈',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time / Retail Data Dashboard")

# top-level filters 

job_filter = st.selectbox("Select the Country", pd.unique(df['Country']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

df = df[df['Country']==job_filter]

# near real-time / live feed simulation 
