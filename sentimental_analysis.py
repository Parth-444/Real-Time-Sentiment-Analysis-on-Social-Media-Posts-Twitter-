from transformers import pipeline
from sqlalchemy.orm import Session
from database_work import *

sentiment_pipeline = pipeline('sentiment')


def analyze_sentiment_in_db(session: Session):
    """
        Fetches tweets from the database, applies sentiment analysis, and updates the database.

        Args:
            session (Session): SQLAlchemy session object.
        """
    try:
        tweets = session.query(Tweet).filter(Tweet.sentiment_label == None).all()
        print(f"Found {len(tweets)} tweets for sentiment analysis.")

        for tweet in tweets:
            sentiment = sentiment_pipeline(tweet.cleaned_text)[0]
            tweet.sentiment_label = sentiment['label']
            tweet.sentiment_score = sentiment['score']

        session.commit()
        print(f"Successfully analyzed sentiment for {len(tweets)} tweets.")

    except Exception as e:
        print(f"Error during sentiment analysis: {e}")
