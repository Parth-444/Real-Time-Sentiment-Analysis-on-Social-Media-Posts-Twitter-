import pandas as pd
from sqlalchemy import sessionmaker
from sqlalchemy import create_engine
from database_file import Tweet

engine = create_engine('sqlite:///tweets.db')
Session = sessionmaker(bind=engine)
session=Session()

def fetch_data(sentiment=None, keyword=None, start_date=None, end_date=None):
    """
        Fetch tweets from the database based on filters.

        Args:
            sentiment (str): Sentiment filter ('POSITIVE', 'NEGATIVE', 'NEUTRAL').
            keyword (str): Keyword to search in tweets.
            start_date (str): Start date for filtering (YYYY-MM-DD).
            end_date (str): End date for filtering (YYYY-MM-DD).

        Returns:
            pd.DataFrame: Filtered tweets as a DataFrame.
        """
    query = session.query(Tweet)
    if sentiment:
        query = query.filter(Tweet.sentiment_label == sentiment)
    if keyword:
        query = query.filter(Tweet.text.contains(keyword))
    if start_date and end_date:
        query = query.filter(Tweet.created_at.between(start_date, end_date))
    tweets = query.all()
