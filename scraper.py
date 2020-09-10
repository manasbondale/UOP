"""
scraper.py downloads 50 tweets from each us state.
Each tweet is a Status Object
I found _json object in each Status Object that I can JSONify and dump to file
"""
import sys
import tweepy 
import json 

CONSUMER_KEY="Fc4f7mtDOt77Mv2KIVzQmYPg1"
CONSUMER_SECRET="Wjresb4dpFvMGYDMK0dHvqz3tV5XdZfteZDWP9OD5a4vvDOTzc"
ACCESS_TOKEN="1309462340-xZLwVN1TGBjw94s14Uf4XAU5WeFrTP9Ra59suzQ"
ACCESS_SECRET="acyQiL3XWx4mAYjSCV7ZLEb3p3t6bP8aYfBJ9CRLNczeo"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET) #Get auth object
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth) #Get API object
"""
I am using API.search(q[, geocode][, lang][, locale][, result_type][, count][, until][, since_id][, max_id][, include_entities])  function to get location filter data.
I took coordinates for the US states from a website and used a 1000km radius to get most of the area inside.
I took 50 tweets from each state.
I later manually typed in the state into the tweet because the json in the tweet is very unreliable and I need the tweets geocoded for happiest_state program
"""

q = open('us_states.json', 'r') #us states latitude longitude data
us_states = json.load(q)
q.close()

tweets = {}
for state in us_states:
    coordinates = us_states[state][1]
    tweets[state]=api.search('', geocode=f"{coordinates[0]},{coordinates[1]},1000km", count = 50)
"""
Here I manually type in the place because the location/place data in the json is not reliable.
Tweets from NY have place set to null and location is sometimes user defined and can be anything.
Sometimes location is 'At Home' or some combination of unicode characters
This is so that happiest_state.py can pick up the location easily.
"""

with open("tweets.json", "w") as f:
    for state in tweets:
        for tweet in tweets[state]:
            tweet._json['place'] = {}  
            tweet._json['place']['place_type'] = 'admin'
            tweet._json['place']['country'] = 'United States'
            tweet._json['place']['name'] = state
            json.dump(tweet._json, f) #JSONify and dump the tweet to file 
            f.write('\n')

