"""
I count all the words in every tweet.
I also maintain a default dict for every word to count it's total occurances.
"""
import re 
import json
from collections import defaultdict
import sys

DATAJSON = sys.argv[1]

#### PART 1 : READ THE DATA.JSON FILE FOR ALL THE TWEETS 
TweetsList = []
with open(DATAJSON, 'r', encoding='utf-8') as f:
    for jsonObj in f:
        TweetDict = json.loads(jsonObj)
        TweetsList.append(TweetDict)
######


### PART 2 : Count all instances of every term. Also count all words in total.
terms2freq = defaultdict(lambda:0)
total_words_count=0
for tweet in TweetsList:
    if 'text' in tweet:
        line = tweet['text'] 
        words = re.findall(r'[a-zA-Z\-]+', line)
        total_words_count += len(words)
        for word in words:
            terms2freq[word.lower()]+=1
####

### PART 3 : Print frequencies
for terms, freq in terms2freq.items():
    print(terms+'\t'+str(freq/total_words_count))
####

