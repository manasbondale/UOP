"""
I take all the hashtags from each tweet.
They are present at tweet->_json->entities->hashtags->text
I maintain a multiset Counter() to count every hashtag
I then output the highest 10.
Sometimes one hashtag cannot be print cause of UnicodeEncodeError and I take the next tweet to replace it so that I always print ten.
I used a counter variable x = 0 to count while I print.
"""
import re 
import json
import sys
from collections import Counter

DATAJSON =  sys.argv[1]

#### READ THE DATA.JSON FILE FOR ALL THE TWEETS 
TweetsList = []
with open(DATAJSON, 'r', encoding='utf-8') as f:
    for jsonObj in f:
        TweetDict = json.loads(jsonObj)
        TweetsList.append(TweetDict)
######

multiset = Counter() ## I used this multiset data structure that keeps count of all items in it
### count all hashtags
for t in TweetsList:
    try:
        if "entities" in t:
            if 'hashtags' in t['entities']:
                htags=[]
                for h in t['entities']['hashtags']:
                    htags.append(h['text'])
                multiset.update(htags)
    except TypeError:
        pass

top_ten = multiset.most_common(20)
x=0

### Print out the top ten. This is a bit tricky because sometimes I get Unicode Error
### So I took the top 20 and outputed the top ten, excepting any Unicode Error.
for ht in top_ten:
    try:
        if x > 10:
          break
        print(ht[0],' ',ht[1])
        x+=1
    except UnicodeEncodeError:
        continue



