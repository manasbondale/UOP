Data files
AFINN-111.txt : contains sentiment scores for words
data.json : contains test tweet data
us_states.json : us state coordinates and abbreviations

Code files
frequency.py : outputs the frequencies of all words in all tweets
happiest_state.py : outputs the state that has the highest sentiment score
scraper.py : download USA public tweet data and dumps to tweets.json
term_sentiment.py : calculates sentiment scores for words not in AFINN-111.txt
top_ten.py : finds the top ten most used hashtags 
tweet_sentiment.py : calculates the total sentiment score of each tweet

Output files
tweets.json : downloaded tweet data from scraper.py
frequency_output.txt : Output of frequency.py with AFINN-111.txt and data.json as parameters
happiest_state_output.txt : Output of happiest_state.py with AFINN-111.txt and data.json as parameters
term_sentiment_output.txt : Output of term_sentiment.py with AFINN-111.txt and data.json as parameters
top_ten_output.txt : Output of top_ten.py with AFINN-111.txt and data.json as parameters
tweet_sentiment_output.txt : Output of tweet_sentiment.py with AFINN-111.txt and data.json as parameters
