"""
Look at function getState() for how I resolve the state of each tweet.

This program should be called using "python happiest_state.py AFINN-111.txt data.json"

The algorithm is pretty simple. I try to get the location of the tweet using multiple ways.

I then add up all the sentiments of the tweets in that state to a dictionary holding { state : total_sentiment } key value pairs.

Then I get the max-key from the dictionary as my answer.
"""
import re 
import json
from collections import defaultdict
import sys


us_states =\
  {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'American Samoa': 'AS',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District Of Columbia': 'DC',
    'Federated States Of Micronesia': 'FM',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Guam': 'GU',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Marshall Islands': 'MH',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands': 'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
  }

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
        TweetsDict = json.loads(jsonObj)
        TweetsList.append(TweetsDict)
#####

### PART 3 : Get the state of tweet using function
# Here I used the place_type variable as you can see
# There are a few tweets that use 'poi' or 'Neighborhood' placetype variable that I can't resolve to location without using some kind of geography python library
def getState(t):
    try:
        if t['place']['place_type'] == 'city':
            if t['place']['country_code'] == 'US':
                return t['place']['full_name'][-2:]
            else :
                return None
    except :
        pass

    try:
        if t['place']['place_type'] == 'admin':
            if t['place']['country'] == 'United States':
                return us_states[t["place"]["name"]]
    except:
        pass

    try:
        location =  t['user']['location']
        for state in us_states:
            if location.find(state) != -1 or  location.find(us_states[state]) != -1:
                return us_states[state]
    except:
        pass

    return None
#####

#### This is from the other file tweet_sentiment.py
# I WROTE A LITTLE FUNCTION THAT TAKES A line  AND RETURNS THE TOTAL SENTIMENT OF THAT  LINE
def tweet_sentiment(line):
    sentiment   = 0
    words=re.findall(r'[a-zA-Z\-\']+', line)
    for word in words:
        if word.lower() in scores:
            sentiment += scores[word.lower()]
    return sentiment
#######


happiness = defaultdict(lambda : 0)

### Find and add up the sentiments of each state
for tweet in TweetsList:
    if 'text' in tweet:
        state = getState(tweet)
        if state:
            happiness[state] += tweet_sentiment(tweet['text'])
#######

max_key = max(happiness, key=happiness.get)
print(max_key)
