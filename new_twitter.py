# -*- coding: utf-8 -*-
import tweepy
import couchdb
import time
import main
import config
import json
from textblob import TextBlob
import filter
import gc

new_tweet_count=0
new_max_count=0

## access to tweepy streamming method
def get_connection():
   auth = tweepy.OAuthHandler(config.consumer_key,config.consumer_secret)
   auth.set_access_token(config.access_token,config.access_secret)
   api=tweepy.API(auth)
   # API Error handling
   if (not api):
      print ("Invalid info to connect to API !")
   return auth

def get_max(count):
    global new_max_count
        #to get the maximun of new tweet
    new_max_count=count/3

class MyStreamListener(tweepy.StreamListener):
    
   def on_status(self,status):
    global new_tweet_count
    try:
        # access to couchdb server and Error handling
        try:
#            couch=couchdb.Server('http://0.0.0.0:5984/')
            couch =couchdb.Server('http://admin:password@115.146.93.201:5984/')
            db= couch['twdata']
        except:
            print ("trouble in couchdb connection !")
        #filter duplicates by tweetid
           #Check if the tweet has coordinates,
        if  status.coordinates is not None:
               temp_lat=status.coordinates[0]
               temp_lng=status.coordinates[1]
        else:
               temp_lat=None
               temp_lng=None
           #check if the tweet has user_info
        if len(status.entities[u'user_mentions'])>0:
               temp_name=status.entities[u'user_mentions'][0][u'screen_name']
        else:
               temp_name=None
        if  status.created_at is not None:
               temp_date=(str)(status.created_at)
        else:
               temp_date=None
        # sentiment analyse for tweet
        testimonial=TextBlob(status.text)
        # save valid and useful tweet info into couchdb
        #include data, tweet_id, content, favorite_count, polarity of tweet, subjectivity of tweet, lat, lng, gender, topic
        if new_tweet_count< new_max_count:
            doc={'_id':(str)(status.id),'content':filter.checkText(status.text),'user':temp_name,'date':temp_date,'polarity':testimonial.sentiment.polarity,'subjectivity':testimonial.sentiment.subjectivity,'favorite_count':status.favorite_count,'lat':temp_lat,'lng':temp_lng,'source':filter.checkText(status.source),'location':filter.checkText(status.user.location),'topic':filter.split_combine(status.entities[u'hashtags']),'gender':filter.gender_identify(filter.checkText(temp_name))}
            try:
                db.save(doc)
                new_tweet_count+=1
            except couchdb.http.ResourceConflict:
                print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),"new_twitter sleep")
                new_tweet_count+=0
            return True
        #Error handling
        else:
            print ("data harvest finished and %d tweets are stored"%new_tweet_count)
            return False

    except BaseException as e:
       print("Error on_status: %s" % str(e))
   #Error handling
   def on_error(self, status):
       if status == 420:
           print("Rate limit!")
       return True
    
   #Timeout handling
   def on_timeout(self):
        print ("time out!")
        return True
