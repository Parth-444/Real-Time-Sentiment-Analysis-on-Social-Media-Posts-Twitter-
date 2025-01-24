# Real-Time Sentiment Analysis on Social Media Posts

## Project Overview
This project performs real-time sentiment analysis on tweets related to specific topics. It includes data ingestion, preprocessing, sentiment analysis, and visualization, storing the results in a database. The pipeline is modular and handles the entire workflow, from fetching tweets to analyzing and storing their sentiments, enabling real-time insights into public sentiment trends.

## Key Features
- **Tweet Ingestion:** Fetch recent tweets using Twitter's `search_recent` endpoint.
- **Database Integration:** Store raw tweets and processed data in an SQLite database.
- **Text Preprocessing:** Clean and normalize tweet text for analysis.
- **Sentiment Analysis:** Classify tweets as Positive, Negative, or Neutral using a Hugging Face model.
- **Pipeline Orchestration:** Seamlessly manage all steps via a `main.py` file.

## Technical Details
- **Programming Language:** Python
- **Database:** SQLite
- **Twitter API:** `search_recent` endpoint via Tweepy
- **Text Processing:** NLTK and regex
- **Sentiment Analysis:** Hugging Face Transformers (`distilbert-base-uncased-finetuned-sst-2-english`)
- **Project Orchestration:** Modular structure for scalability

## Project Structure
```plaintext
real_time_sentiment_analysis/
│
├── .idea/                   # IDE configuration files
├── .venv/                   # Virtual environment folder
├── _pycache_/               # Compiled Python files
├── dashboard/               # Contains visualization and frontend code
├── data/                    # Stores raw and processed data files
├── models/                  # Database models and schemas
├── .env                     # Environment variables for API keys
├── database_work.py          # Database setup and schema definition
├── preprocessing.py          # Functions for text preprocessing
├── sentimental_analysis.py   # Sentiment classification logic
├── tweet_streamer.py         # Fetch tweets from the Twitter API
├── main.py                   # Orchestrates the entire pipeline
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation (this file)
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/real-time-sentiment-analysis.git
cd real-time-sentiment-analysis
```

### 2. Install Dependencies
Use the following command to install all required libraries:
```bash
pip install -r requirements.txt
```

### 3. Add Your Twitter API Credentials
Create a `.env` file in the root directory and add your **Twitter Bearer Token**:
```plaintext
BEARER_TOKEN=your_twitter_bearer_token
```

### 4. Initialize the Database
Run the following script to set up the SQLite database:
```bash
python database_work.py
```

### 5. Run the Pipeline
Execute the `main.py` file to run the entire pipeline:
```bash
python main.py
```

## Example Output
- **Database (`tweets.db`):**
  - `text`: Raw tweet text
  - `cleaned_text`: Preprocessed version of the tweet
  - `sentiment_label`: Sentiment classification (Positive/Negative/Neutral)
  - `sentiment_score`: Confidence score
 
- **Console Output:**
```plaintext
===== Step 1: Fetching Tweets =====
Fetched and saved 10 tweets to the database.
===== Step 2: Preprocessing Tweets =====
Found 10 tweets to preprocess.
Successfully preprocessed 10 tweets.
===== Step 3: Sentiment Analysis =====
Found 10 tweets for sentiment analysis.
Successfully analyzed sentiment for 10 tweets.
Pipeline execution completed. Check the database for results.
```

## Requirements
- Python 3.8+
- Required Libraries:
  - tweepy
  - transformers
  - sqlalchemy
  - nltk
  - python-dotenv
 
## Contribution
Feel free to fork this repository and submit pull requests for new features or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
