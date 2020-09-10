"""
The approach I have come up is to count all the scores of all the words that the term appears in the same tweet with, and then average them up.
So:
    1. The team members were hard to tell apart since they all wore their hair in a ponytail.
    2. He liked to play with words in the bathtub.
    3. The tree fell unexpectedly short.
 
 Lets say tree=3, short=2, team=4, apart=-1, hard=-2, ponytail=1, bathtub=1

 The score for the word 'the' will be i [ team+hard+apart+ponytail+bathtub+tree+short / 7 ]
 which is 3+2+4+-1+-2+1+1 = 8 / 7 = 1.1....

 The problem with using the total tweet sentiment of each tweet a word appeared in and taking an average of that would be that a term only appearing in a highly positive tweet will have a seriously high.

    1. The greatest champion won the biggest prize.

    Here lets say greatest=4, champion=4, won=5, biggest=3 and prize=4.
    If we divided the total by the number of tweets, the word 'The' will have a score of 4+4+5+3+4 divided by 1. Which is 20!!!
    Instead if we counted THE WORDS and divided by number of the words 'The' will have a score of 4+4+5+3+4 = 20 divided by 5  = 4 .... which makes more sense than going with '20'


So my formula is : Take all the sentimental terms the non-sentimental term appears in tweets with, add their sentimental scores, and divide by the number of the sentimental terms.
"""


import re 
import json
import sys

AFINN111 = sys.argv[1]
DATAJSON =  sys.argv[2]


###### PART 1 : READ THE AFFINN TEXT FILE INTO A DICTIONARY CALLED scores
scores = {} 
with open(AFINN111, 'r') as afinnfile: 
    for line in afinnfile:
        term, score = line.split("\t") 
        scores[term] = int(score) 
#####


#### PART 2 : READ THE DATA.JSON FILE FOR ALL THE TWEETS 
TweetsList = []
with open(DATAJSON, 'r', encoding='utf-8') as f:
    for jsonObj in f:
        TweetDict = json.loads(jsonObj)
        TweetsList.append(TweetDict)
######

### PART 3: lets count all the non-sentimental terms and put them in a dictionaries as keys and each will have an empty list as their values..... for now

nonsentimental = {}
for tweet in TweetsList:
    if 'text' in tweet:
        line = tweet['text'] 
        words = re.findall(r'[a-zA-Z\-\']+', line)
        for word in words:
            if word.lower() not in scores and word.lower() not in nonsentimental:
                nonsentimental[word.lower()] = []

####

### PART 4 : For every non-sentimental word lets count all the scores of the sentimental words it appears with

for tweet in TweetsList:
    if 'text' in tweet:
        sentiments=[]
        line = tweet['text']
        words = re.findall(r'[a-zA-Z\-\']+', line)

        for word in words:
            if word.lower() in scores:
                sentiments.append(scores[word.lower()]) #take scores of all sentimental words in the tweet
            else:
                nonsentimental[word.lower()].extend(sentiments) #put them in the lists of all the nonsentimental words in the same tweet

###

## PART 5 : Calculate the sentimental scores of every nonsentimental word using my formula

calculated_scores={}
for word in iter(nonsentimental.items()):
    neighbouring_scores =  word[1]
    if len(neighbouring_scores)==0:
        calculated_scores[word[0]] = 0 
        continue
    calculated_scores[word[0]] = sum(neighbouring_scores)/len(neighbouring_scores)

####

### PART 6 : Print 
for word in iter(calculated_scores.items()):
    print(word[0]+'\t'+str(word[1]))
### 
