from tweet_streamer import *

session = Session()
# if __name__ == "__main__":
#     from tweepy import Client
#     import os
#     from dotenv import load_dotenv
#
#     # Load environment variables
#     load_dotenv()
#     BEARER_TOKEN = os.getenv("BEARER_TOKEN")
#
#     # Initialize Twitter client
#     client = Client(bearer_token=BEARER_TOKEN)
#
#     # Create a new session
#     session = Session()
#
#     # Example query
#     keywords = "GBP"
#     fetch_recent_tweets(client, query=keywords, max_results=10, session=session)


# def inspect_database(session):
#     """
#     Prints all rows from the tweets table.
#     """
#     try:
#         tweets = session.query(Tweet).all()
#         print("Database Contents:")
#         for tweet in tweets:
#             print(f"ID: {tweet.id}, Text: {tweet.text}, Created At: {tweet.created_at}")
#     except Exception as e:
#         print(f"Error inspecting database: {e}")
#
#
# # Example usage
# if __name__ == "__main__":
#     inspect_database(session)
