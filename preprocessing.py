import re
import nltk
from nltk.corpus import stopwords
from sqlalchemy.orm import sessionmaker
from database_work import *

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
Session = sessionmaker(bind=engine)
session = Session()


def preprocess_tweet(tweet_text):
    """
        Cleans and preprocesses raw tweet text.

        Args:
            text (str): Raw tweet text.

        Returns:
            str: Cleaned tweet text.
        """
    tweet_text = re.sub(r"http\S+|www\S+|https\S+", "", tweet_text, flags=re.MULTILINE)
    tweet_text = re.sub(r"@\w+|#\w+", "", tweet_text)
    tweet_text = re.sub(r"[^A-Za-z\s]", "", tweet_text)
    tweet_text = tweet_text.lower()
    words = tweet_text.split()
    words = [word for word in words if word not in stop_words]
    cleaned_tweet = " ".join(words)
    return cleaned_tweet


def preprocess_tweets(input_file, output_file):
    """
        Fetches tweets from the database, preprocesses them, and updates the database.

        Args:
            session (Session): SQLAlchemy session object.
        """
    try:
        tweets = session.query(Tweet).filter(Tweet.cleaned_text == None).all()

        print(f"Found {len(tweets)} tweets to preprocess.")
        for tweet in tweets:
            tweet.cleaned_text = preprocess_tweet(tweet.text)

        session.commit()
        print(f"Successfully preprocessed {len(tweets)} tweets.")


    except Exception as e:
        print(f"Error during preprocessing: {e}")
