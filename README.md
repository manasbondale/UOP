# Data files

- __AFINN-111.txt__ : contains sentiment scores for words

- __data.json__ : contains test tweet data

- __us_states.json__ : us state coordinates and abbreviations


# Code files

- __frequency.py__ : outputs the frequencies of all words in all tweets

- __happiest_state.py__ : outputs the state that has the highest sentiment score

- __scraper.py__ : download USA public tweet data and dumps to tweets.json

- __term_sentiment.py__ : calculates sentiment scores for words not in AFINN-111.txt

- __top_ten.py__ : finds the top ten most used hashtags 

- __tweet_sentiment.py__ : calculates the total sentiment score of each tweet


# Output files

- __tweets.json__ : downloaded tweet data from scraper.py

- __frequency_output.txt__ : Output of frequency.py with AFINN-111.txt and data.json as parameters

- __happiest_state_output.txt__ : Output of happiest_state.py with AFINN-111.txt and data.json as parameters

- __term_sentiment_output.txt__ : Output of term_sentiment.py with AFINN-111.txt and data.json as parameters

- __top_ten_output.txt__ : Output of top_ten.py with AFINN-111.txt and data.json as parameters

- __tweet_sentiment_output.txt__ : Output of tweet_sentiment.py with AFINN-111.txt and data.json as parameters


