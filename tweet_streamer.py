import tweepy
import os
from dotenv import load_dotenv
import json

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")
client = tweepy.Client(bearer_token=BEARER_TOKEN)


def authenticate_twitter(bearer_token):
    return tweepy.StreamingClient(bearer_token=bearer_token)


query = 'iphone 16'
output_file_name = "tweets.json"


def fetch_recent_tweets(client, query, max_results=10, output_file="recent_tweets.json"):
    """
    Fetch recent tweets using the search_recent endpoint and save them to a file.

    Args:
        client: Tweepy client object.
        query: Search query string.
        max_results: Maximum number of tweets to fetch (max 100 per request).
        output_file: File to save the tweets.
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
            tweets = []
            for tweet in response.data:
                tweets.append({
                    "id": tweet.id,
                    "text": tweet.text,
                    "created_at": str(tweet.created_at),
                    "author_id": tweet.author_id
                })

            # Save to file
            with open(output_file, "w") as f:
                json.dump(tweets, f, indent=4)
            print(f"Saved {len(tweets)} tweets to {output_file}")
        else:
            print("No tweets found for the given query.")

    except Exception as e:
        print(f"Error fetching tweets: {e}")


fetch_recent_tweets(client, query)
