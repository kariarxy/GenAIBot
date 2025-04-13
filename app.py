import streamlit as st # web development
import numpy as np # np mean, np random 
import pandas as pd # read csv, df manipulation
import time # to simulate a real time data, time loop 
import plotly.express as px # interactive charts
import plotly.graph_objects as go


# read csv from a github repo
# df = pd.read_csv("https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv")
df=pd.read_csv("https://raw.githubusercontent.com/kariarxy/GenAIBot/main/retail_data.csv")

st.set_page_config(
    page_title = 'Real-Time Retail Data Dashboard',
    page_icon = '📈',
    layout = 'wide'
)

# dashboard title

st.title("Real-Time Retail Data Dashboard")

st.markdown("<h1 style='color: blue;'>Retail Data Analysis</h1>", unsafe_allow_html=True)


# Sidebar for filtering
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect("Select Countries", df['Country'].unique(), default=list(df["Country"].unique()))

# Filter data based on sidebar selections
df_selected_country = df[df["Country"].isin(selected_countries)]

# Map of countries with color based on total spent
st.subheader("Country Map")
fig_map = px.choropleth(
    df_selected_country, locations="Country", locationmode="country names", color="max_spent",
    hover_name="Country", scope="europe", title="Total Spent by Country"
)
st.plotly_chart(fig_map)

 # Calculate total spent per country
country_totals = df.groupby('Country')['total_spent'].sum()

# Sort countries by total spent
sorted_countries = country_totals.sort_values(ascending=False).reset_index()


# Bar chart for countries with total spent
fig = px.bar(sorted_countries, x='Country', y='total_spent', title='Total Spent per Country (Sorted)')
st.plotly_chart(fig)
