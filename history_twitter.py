#################################
#Team 4                         #
#Melbourne,Sydney,Brisbane,Perth#
#Dong Wang     773504           #
#Danping Zeng  777691           #
#Jia Zhen      732355           #
#Jinghan Liang 732329           #
#Sixue Yang    722804           #
#################################
# -*- coding: utf-8 -*-
import tweepy
import couchdb
import time
import config
from textblob import TextBlob
import filter
import datetime

# to crwal tweet by tweepy
def tweeet_crawl(maxTweets):
  # to sum up the total number of tweet
  sleep_count=0
  history_tweet_count=0
  # per query reply
  tweetsPerQry=100
  # get topic
  searchQuery = config.topic
  # access to tweepy
  auth = tweepy.AppAuthHandler(config.consumer_key,config.consumer_secret)
  # to catch exceptions and cope with
  api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

  # API Error handling
  if (not api):
      print ("Invalid info to connect to API !")

  # access to couchdb server and Error handling
  try:
      couch =couchdb.Server('http://admin:password@115.146.93.201:5984/')
      db= couch['twdata']
  except:
      print ("Trouble in couchdb connection !")
  while history_tweet_count < maxTweets:
    tweet_num=0
    
    for tweet in tweepy.Cursor(api.search,geocode=config.geo,count=tweetsPerQry,lang = "en").items(maxTweets) :
            
           if tweet._json[u'coordinates'] is not None:
              temp_lat=tweet._json[u'coordinates'][u'coordinates'][0]
              temp_lng=tweet._json[u'coordinates'][u'coordinates'][1]
           else:
              temp_lat=None
              temp_lng=None
           #sentiment analyse for tweet
           testimonial=TextBlob(tweet._json[u'text'])
           # save valid and useful tweet info into couchdb
           #include data, history_tweet_count, content, favorite_count, polarity of tweet, subjectivity of tweet, lat, lng, gender, topic
           doc={'_id':(str)(filter.checkText(tweet._json[u'id'])),'content':filter.checkText(tweet._json[u'text']),'user':filter.checkText(tweet.user.name),'date':filter.checkText(tweet._json[u'created_at']),'polarity':testimonial.sentiment.polarity,'subjectivity':testimonial.sentiment.subjectivity,'favorite_count':filter.checkText(tweet._json[u'favorite_count']),'lat':temp_lat,'lng':temp_lng,'source':filter.checkText(tweet.source),'location':filter.checkText(tweet._json[u'user'][u'location']),'topic':filter.split_combine(tweet._json[u'entities'][u'hashtags']),'gender':filter.gender_identify(filter.checkText(tweet.user.name))}
           try:
              db.save(doc)
              history_tweet_count += 1
              tweet_num += 1
           except couchdb.http.ResourceConflict:
               tweet_num += 1
               sleep_count+=1
               if sleep_count>50:
                  print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())),":history_tweet sleep")
                  time.sleep(5)
                  sleep_count=0
    if tweet_num>0:
          #Display how many tweets we have collected
          print ("total new tweets are collected %d"%tweet_num)
  print  ("data harvest finished and %d tweets are stored"%history_tweet_count)

