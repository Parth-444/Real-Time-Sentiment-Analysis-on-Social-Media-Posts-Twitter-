import os
import torch
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
from tweet_streamer import fetch_recent_tweets  # Import tweet fetching function
from preprocessing import preprocess_tweets  # Import preprocessing function
from sentimental_analysis import analyze_sentiment_in_db  # Import sentiment analysis function

# Load environment variables
load_dotenv()

# Initialize database
engine = create_engine("sqlite:///tweets.db")
Session = sessionmaker(bind=engine)
session = Session()

# Twitter API credentials
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Initialize Twitter client (for search_recent endpoint)
from tweepy import Client
client = Client(bearer_token=BEARER_TOKEN)

# Main function to run the pipeline
def main():
    print("===== Step 1: Fetching Tweets =====")
    query = "iphone 16"
    fetch_recent_tweets(client, query=query, max_results=10, session=session)

    print("===== Step 2: Preprocessing Tweets =====")
    preprocess_tweets(session)

    print("===== Step 3: Sentiment Analysis =====")
    analyze_sentiment_in_db(session)

    print("Pipeline execution completed. Check the database for results.")

if __name__ == "__main__":
    main()
