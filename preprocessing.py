import re
import nltk
from nltk.corpus import stopwords
import json

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))


def preprocess_tweet(tweet_text):
    tweet_text = re.sub(r"http\S+|www\S+|https\S+", "", tweet_text, flags=re.MULTILINE)
    tweet_text = re.sub(r"@\w+|#\w+", "", tweet_text)
    tweet_text = re.sub(r"[^A-Za-z\s]", "", tweet_text)
    tweet_text = tweet_text.lower()
    words = tweet_text.split()
    words = [word for word in words if word not in stop_words]
    cleaned_tweet = " ".join(words)
    return cleaned_tweet


def preprocess_tweets(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            tweets = json.load(infile)

        cleaned_tweets = []
        for tweet in tweets:
            cleaned_tweet = preprocess_tweet(tweet["text"])
            cleaned_tweets.append({
                "id": tweet["id"],
                "created_at": tweet["created_at"],
                "cleaned_text": cleaned_tweet
            })

        with open(output_file, "w") as outfile:
            json.dump(cleaned_tweets, outfile, indent=4)

        print(f"Preprocessed tweets saved to {output_file}")

    except Exception as e:
        print(f"Error during preprocessing: {e}")


# preprocess_tweets('recent_tweets.json', 'output_cleaned_file.json')
