"""
I add up the sentiments for all the words in each tweet and record it as the total sentiment of that tweet.
I used regex to get all the words. I consider son-of-a-bitch as a single word as I have the sentiment for it in the affin text file
"""
import re 
import json
import sys

AFINN111 = sys.argv[1]
DATAJSON =  sys.argv[2]

###### READ THE AFFINN TEXT FILE INTO A DICTIONARY CALLED scores
afinnfile = open(AFINN111)
scores = {} 
for line in afinnfile:
    term, score = line.split("\t") 
    scores[term] = int(score) 
afinnfile.close()
#####


#### PART 2 : READ THE DATA.JSON FILE FOR ALL THE TWEETS 
TweetsList = []
with open(DATAJSON, 'r', encoding='utf-8') as f:
    for jsonObj in f:
        TweetDict = json.loads(jsonObj)
        TweetsList.append(TweetDict)
######

##### PART 3 : I WROTE A LITTLE FUNCTION THAT TAKES A line  AND RETURNS THE TOTAL SENTIMENT OF THAT  LINE
def tweet_sentiment(line):
    sentiment   = 0
    words=re.findall(r'[a-zA-Z\-\']+', line)
    for word in words:
        if word.lower() in scores:
            sentiment += scores[word.lower()]
    return sentiment
#######

###### PART 4 :  use that function i wrote earlier to calculate and then print the sentiment of each tweet
for tweet in TweetsList:
    if 'text' in tweet:
        print(str(tweet_sentiment(tweet['text'])))
    else:
        print('0')
#######
    

