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
    filtered_df, locations="Country", locationmode="country names", color="max_spent",
    hover_name="Country", title="Total Spent by Country"
)
st.plotly_chart(fig_map)

 # Calculate total spent per country
country_totals = df.groupby('Country')['total_spent'].sum()

# Sort countries by total spent
sorted_countries = country_totals.sort_values(ascending=False)


# Bar chart for top 10 countries with total spent
st.subheader("Top Countries by Sum of Total Spent")
st.dataframe(sorted_countries,column_order=("Country", "Total Spent"),hide_index=True, width=None,
             column_config={
                 "Countries": st.column_config.TextColumn("Countries",),
                 "Total Spent": st.column_config.ProgressColumn(
                     "Total Spent",
                     format="%f",
                     min_value=0,
                     max_value=max(sorted_countries.Total Spent),)}
            )
