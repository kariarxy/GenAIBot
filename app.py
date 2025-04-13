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

st.title("Real-Time Retail Data Dashboard")

st.markdown("<h1 style='color: blue;'>Retail Data Analysis</h1>", unsafe_allow_html=True)


# Sidebar for filtering
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect("Select Countries", df['Country'].unique(), default=list(df["Country"].unique()))

# Filter data based on sidebar selections
filtered_df = df[df["Country"].isin(selected_countries)]

# Map of countries with color based on total spent
st.subheader("Country Map")
fig_map = px.choropleth(
    filtered_df, locations="Country", locationmode="country names", color="max_spent",
    hover_name="Country", title="Total Spent by Country"
)
st.plotly_chart(fig_map)

# Bar chart for top 10 countries with max spent
st.subheader("Top 10 Countries by Max Spent")
top_10_countries = filtered_df.nlargest(10, "max_spent")
fig_bar = px.bar(top_10_countries, x="Country", y="max_spent",
                 title="Top 10 Countries by Max Spent",
                 labels={"max_spent": "Max Spent"})
st.plotly_chart(fig_bar)

# Heatmap for total spent by country
st.subheader("Total Spent Heatmap")
heatmap_data = filtered_df.pivot_table(index='Country', values='max_spent', aggfunc="sum")
fig_heatmap = go.Figure(data=go.Heatmap(z=heatmap_data.values,
                                       x=heatmap_data.index,
                                       y=["Total Spent"],
                                       colorscale='Viridis'))
fig_heatmap.update_layout(title="Total Spent Heatmap")
st.plotly_chart(fig_heatmap)
