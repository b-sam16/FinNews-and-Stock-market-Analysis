from textblob import TextBlob

# Sentiment Analysis using TextBlob
def sentiment_analysis(text):

    # Calculate the polarity of the text
    polarity = TextBlob(text).sentiment.polarity

    # Classify polarity into Positive, Negative, or Neutral
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to a column of headlines
def apply_sentiment_analysis(news_data):
    news_data['sentiment'] = news_data['headline'].apply(sentiment_analysis)
    return news_data

def apply_sentiment_analysis_and_map(news_data):
    """
    Applies sentiment analysis to the 'headline' column and maps numeric sentiment values 
    (1, 0, -1) to text labels ('Positive', 'Neutral', 'Negative').
    
    Parameters:
        news_data (DataFrame): DataFrame containing the 'headline' column.
        
    Returns:
        DataFrame: Updated DataFrame with 'sentiment_numeric' and 'sentiment_label' columns.
    """
    # Apply sentiment analysis to the 'headline' column and store numeric values
    news_data['sentiment'] = news_data['headline'].apply(sentiment_analysis)
    
    # Map numeric sentiment to text labels
    sentiment_map = {'Positive': 1,'Neutral': 0,'Negative': -1}
    news_data['sentiment_label'] = news_data['sentiment'].map(sentiment_map)
    
    return news_data