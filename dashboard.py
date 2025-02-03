import streamlit as st
import matplotlib.pyplot as plt
from fetch_database_data import fetch_data
import pandas as pd

# Set up Streamlit app
st.set_page_config(page_title="Sentiment Analysis Dashboard", layout="wide")

# Sidebar Filters
st.sidebar.header("Filters")
sentiment = st.sidebar.selectbox("Sentiment", ["All", "POSITIVE", "NEGATIVE", "NEUTRAL"])
keyword = st.sidebar.text_input("Search Keyword")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

# Main Content
st.title("Sentiment Analysis Dashboard")
st.write("Visualize real-time sentiment trends for fetched tweets.")

# Fetch data
filtered_data = fetch_data(
    sentiment=None if sentiment == "All" else sentiment,
    keyword=keyword,
    start_date=str(start_date),
    end_date=str(end_date),
)

# Sentiment Distribution
st.subheader("Sentiment Distribution")
if not filtered_data.empty:
    sentiment_counts = filtered_data["Sentiment"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(sentiment_counts, labels=sentiment_counts.index, autopct="%1.1f%%", startangle=90)
    ax1.axis("equal")
    st.pyplot(fig1)
else:
    st.write("No data available for the selected filters.")

# Sentiment Over Time
st.subheader("Sentiment Over Time")
if not filtered_data.empty:
    filtered_data["Created At"] = pd.to_datetime(filtered_data["Created At"])
    time_trend = filtered_data.groupby([filtered_data["Created At"].dt.date, "Sentiment"]).size().unstack()
    st.line_chart(time_trend)
else:
    st.write("No data available for the selected filters.")

# Tweet Table
st.subheader("Filtered Tweets")
if not filtered_data.empty:
    st.dataframe(filtered_data[["Text", "Sentiment", "Score"]])
else:
    st.write("No tweets to display.")
