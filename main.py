max_volum=0
import tweepy
import config
import history_twitter
import new_twitter
import threading
import time
import sys

if __name__=="__main__":
    file = sys.argv[1]
    config.get_config(file)
    max_volum=(int)(config.max_size)
    max_history_tweet= max_volum*2/3
#    twitter_stream.filter(track=config.streaming_topic,locations=config.bound,async=True)
#    # to use thread to control two crawling fucntion
    while(1):
       myStreamListener =new_twitter.MyStreamListener()
       new_twitter.get_max(max_volum)
       twitter_stream = tweepy.Stream(auth = new_twitter.get_connection(), listener=myStreamListener)
       try:
          t1 = threading.Thread(target=history_twitter.tweeet_crawl(max_history_tweet))
          t1.start()
          t1.join()
       except Exception as e:
          time.sleep(5)
          print ("Error: t1 thread stop",e)
       try:
          t2 = threading.Thread(target=twitter_stream.filter(locations=config.bound,async=True))
          t2.start()
          t2.join()
       except Exception as e:
          time.sleep(5)
          print ("Error: t2 thread stop",e)
    print ("congratulation! Data harvest finished!")
