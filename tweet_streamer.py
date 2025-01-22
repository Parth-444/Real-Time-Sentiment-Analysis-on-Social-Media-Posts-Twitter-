import tweepy
import os
from dotenv import load_dotenv
from database_work import *

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token=BEARER_TOKEN)


def authenticate_twitter(bearer_token):
    return tweepy.StreamingClient(bearer_token=bearer_token)


query = 'iphone 16'
output_file_name = "tweets.json"


def fetch_recent_tweets(client, query, session, max_results=2):
    """
    Fetch recent tweets using the search_recent endpoint and save them to a file.

    Args:
        client: Tweepy client object.
        query: Search query string.
        max_results: Maximum number of tweets to fetch (max 100 per request).
    """
    try:
        # Fetch tweets
        response = client.search_recent_tweets(
            query=query,
            tweet_fields=["id", "text", "created_at", "author_id", "lang"],
            max_results=max_results
        )

        # Check if response contains data
        if response.data:
            for tweet in response.data:
                if not session.query(Tweet).filter(Tweet.id == tweet.id).first():
                    new_tweet = Tweet(
                        id=tweet.id,
                        text=tweet.text,
                        created_at=tweet.created_at,
                        author_id=tweet.author_id
                    )
                    session.add(new_tweet)
            session.commit()
            print(f"Fetched and saved {len(response.data)} tweets to the database.")
        else:
            print("No tweets found for the given query.")


    except Exception as e:
        print(f"Error fetching tweets: {e}")
