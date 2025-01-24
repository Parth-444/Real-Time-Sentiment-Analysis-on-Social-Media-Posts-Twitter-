from sqlalchemy import create_engine, Integer, String, DATETIME, Text, Column, Float
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///tweets.db')
Session = sessionmaker(bind=engine)
session = Session()


class Tweet(Base):
    __tablename__ = "tweets"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DATETIME, nullable=False)
    author_id = Column(String, nullable=False)
    cleaned_text = Column(Text)
    sentiment_label = Column(Text)
    sentiment_score = Column(Float)


Base.metadata.create_all(engine)
print('Database created!!')
