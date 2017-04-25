import tweepy
import couchdb
import time
import config
from textblob import TextBlob
import filter

## access to tweepy to get place id
#auth1 = tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
#auth1.set_access_token(config.access_token,config.access_secret)
#api1=tweepy.API(auth1)
tweet_id=0
tweet_max=1000000
# access to tweepy
auth = tweepy.AppAuthHandler(config.consumer_key,config.consumer_secret)
# to catch exceptions and cope with
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# access to couchdb server
couch =couchdb.Server('http://0.0.0.0:5984/')
db= couch['twitter']

# get placeid
#places = api1.geo_search(query=config.location, granularity="city")
#place_id = places[0].id
#searchQuery='place:'+place_id+' '+'\"'+config.topic+'\"'
searchQuery=config.topic

# to check the value is valid or not
def checkText(temp_text):
   if temp_text is None:
      return None
   else:
      return temp_text

# to crwal tweet by tweepy
while tweet_id<tweet_max:
  tweet_num=0
  for tweet in tweepy.Cursor(api.search,q=searchQuery,geocode=config.geo,tweetsPerQry = 100).items() :
    if tweet._json is not None:
        if tweet._json[u'coordinates'] is not None:
           if filter.filter_duplicate(tweet._json[u'id']):
               #sentiment analyse for tweet
              testimonial=TextBlob(tweet._json[u'text'])
              # save valid and useful tweet info into couchdb
              #include data, tweet_id, content, favorite_count, polarity of tweet, subjectivity of tweet, lat, lng, gender, topic
              doc={'tweetid':checkText(tweet._json[u'id']),'content':checkText(tweet._json[u'text']),'user':checkText(tweet.user.name),'date':checkText(tweet._json[u'created_at']),'polarity':testimonial.sentiment.polarity,'subjectivity':testimonial.sentiment.subjectivity,'favorite_count':checkText(tweet._json[u'favorite_count']),'lat':checkText(tweet._json[u'coordinates'][u'coordinates'][0]),'lng':checkText(tweet._json[u'coordinates'][u'coordinates'][1]),'topic':config.topic,'gender':filter.gender_identify(tweet.user.name)}
              db.save(doc)
              tweet_id+=1
              tweet_num+=1
        else:
           if filter.filter_duplicate(tweet._json[u'id']):
              testimonial=TextBlob(tweet._json[u'text'])
              doc={'tweetid':checkText(tweet._json[u'id']),'content':checkText(tweet._json[u'text']),'user':checkText(tweet.user.name),'date':checkText(tweet._json[u'created_at']),'polarity':testimonial.sentiment.polarity,'subjectivity':testimonial.sentiment.subjectivity,'favorite_count':checkText(tweet._json[u'favorite_count']),'location':config.geo,'lat':'null','lng':'null','topic':config.topic,'gender':filter.gender_identify(tweet.user.name)}
              db.save(doc)
              tweet_id+=1
              tweet_num+=1
  print ("total tweets are collected %d"%tweet_num)
print  ("data harvest finished and %d tweets are stored"%tweet_id)


