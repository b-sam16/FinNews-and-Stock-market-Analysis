
Financial News Sentiment and Stock Correlation Analysis

Overview

This project focuses on analyzing financial news headlines to understand their impact on stock price movements. By performing sentiment analysis and technical indicator calculations, the goal is to identify patterns that can inform investment strategies and improve forecasting accuracy.


---

Key Objectives

1. Sentiment Analysis: Analyze the sentiment of financial news (positive, neutral, negative) using tools like TextBlob.


2. Technical Indicators: Calculate stock market indicators (SMA, RSI, MACD) to analyze trends and market conditions.


3. Correlation Analysis: Determine the relationship between news sentiment and stock price movements.




---

Folder Structure

├── data/                  # Raw and processed datasets  
├── notebooks/             # Jupyter notebooks for analysis and visualization  
├── src/                   # Scripts for data preprocessing, analysis, and visualization  
├── results/               # Generated plots and results  
├── README.md              # Project overview and instructions  
└── requirements.txt       # Python dependencies


---

Setup Instructions

1. Clone the Repository:

git clone <repository-url>


2. Set Up the Environment:

pip install -r requirements.txt


3. Run the Analysis:

Use Jupyter notebooks in the notebooks/ directory for step-by-step execution.

Processed results and visualizations will be saved in the results/ directory.





---

Features

Sentiment Analysis:

Quantifies sentiment polarity of headlines.

Highlights trends in positive, negative, and neutral sentiment.


Technical Indicators:

Simple Moving Average (SMA) for smoothing trends.

Relative Strength Index (RSI) for identifying overbought/oversold conditions.

Moving Average Convergence Divergence (MACD) for trend signals.


Correlation Analysis:

Links sentiment scores to stock price movements using statistical metrics.




---

Key Insights

Sentiment Trends: Neutral sentiment dominates, but spikes in positive and negative sentiment align with major market events.

Stock Indicators: SMA, RSI, and MACD effectively track market trends and reversal points.

Challenges:

Time zone alignment of data was necessary to merge datasets.

Ambiguous headlines required additional preprocessing to improve sentiment accuracy.




---

Future Work

Enhance sentiment analysis using advanced models like VADER or BERT.

Develop an interactive dashboard for real-time insights.

Expand analysis to include more stock tickers and alternative news sources.



---

This project offers a framework for analyzing financial news and its impact on stock markets, laying the foundation for more robust predictive analytics in the future.

