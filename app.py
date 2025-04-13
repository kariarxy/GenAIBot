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

# top-level filters 

selected_country = st.selectbox("Select the Country", pd.unique(df['Country']))

# creating a single-element container.
placeholder = st.empty()

# filter by country

df = df[df['Country']==selected_country]

# Add a text input box for the query
query = st.text_input("Enter your query here:", "")

# Menu
menu = ["Home", "Data Exploration", "Visualization", "About"]
selected_page = st.sidebar.selectbox("Select a page:", menu)

# Slider
slider_value = st.sidebar.slider("Select a value:", 0, 100, 50)

# Display content based on selected page
if selected_page == "Home":
    st.write("Welcome to the home page!")
    st.write(f"Selected Country: {selected_country}")
    st.write(f"Slider Value: {slider_value}")

elif selected_page == "Data Exploration":
    st.write("Data Exploration page")
    st.write(f"Selected Country: {selected_country}")
    st.write(f"Slider Value: {slider_value}")
elif selected_page == "Visualization":
    st.write("Visualization page")
    st.write(f"Selected Country: {selected_country}")
    st.write(f"Slider Value: {slider_value}")
elif selected_page == "About":
    st.write("About Us")
    st.write(f"Selected Country: {selected_country}")
    st.write(f"Slider Value: {slider_value}")

# Display the filtered data
st.write(f"Data for {selected_country}:")
st.dataframe(country_data)

# Column selection for min/max
columns_to_analyze = st.multiselect("Select columns to find min/max:", df.columns[2:]) #Exclude CustomerID and Country

if columns_to_analyze:
    for col in columns_to_analyze:
        if col in country_data.columns: # Check if the column exists in the filtered data
          min_val = country_data[col].min()
          max_val = country_data[col].max()
          st.write(f"For {col} in {selected_country}:")
          st.write(f"- Minimum: {min_val}")
          st.write(f"- Maximum: {max_val}")
        else:
            st.warning(f"Column '{col}' not found in data for {selected_country}")
else:
  st.write("Select at least one column to display min/max values.")
