from textblob import TextBlob

# Sentiment Analysis using TextBlob
def sentiment_analysis(text):

    # Calculate the polarity of the text
    polarity = TextBlob(text).sentiment.polarity

    # Classify polarity into Positive, Negative, or Neutral
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis to a column of headlines
def apply_sentiment_analysis(news_data):
    news_data['sentiment'] = news_data['headline'].apply(sentiment_analysis)
    return news_data
