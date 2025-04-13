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

 # Calculate total spent per country
country_totals = df.groupby('Country')['total_spent'].sum()

# Sort countries by total spent
sorted_countries = country_totals.sort_values(ascending=False).reset_index()

# Bar chart for countries with total spent
fig = px.bar(sorted_countries, x='Country', y='total_spent', title='Total Spent per Country (Sorted)')
st.plotly_chart(fig)

# Map of countries with color based on total spent
st.subheader("Country Map")
fig_map = px.choropleth(
    sorted_countries, locations="Country", locationmode="country names", color="total_spent",
    hover_name="Country", scope="europe", title="Total Spent by Country"
)
st.plotly_chart(fig_map)

# Text input for the query
user_query = st.text_input("Enter your query:")

# Display the query
st.write("Your query:", user_query)

#  Process the query (replace with your actual query processing logic)
# Example: (This part needs to be replaced with your database query)
if user_query:
    try:
        # Replace this with your actual query execution
        result =  "Query execution result would go here"  # Placeholder

        # Display the results
        st.write("Query Results:")
        st.write(result)
    except Exception as e:
        st.error(f"Error processing the query: {e}")
