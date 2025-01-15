import tweepy
import os
from dotenv import load_dotenv
import json

load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")


def authenticate_twitter(bearer_token):
    return tweepy.StreamingClient(bearer_token=bearer_token)


class MyStreamListener(tweepy.StreamingClient):
    def __init__(self, bearer_token, output_file):
        super().__init__(bearer_token)
        self.output_file = output_file

    def on_tweet(self, tweet):
        try:
            with open(self.output_file, 'a') as f:
                f.write(json.dumps({
                    "id": tweet.id,
                    "created_at": tweet.created_at,
                    "text": tweet.text
                }) + "\n")
            print(f"tweet collected: {tweet.text}")
        except Exception as e:
            print(f"Error processing tweet: {e}")

    def on_error(self, status_code):
        print(f"Error: {status_code}")
        if status_code == 420:
            return False
