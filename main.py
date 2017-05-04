max_volum=0
import tweepy
import config
import history_twitter
import new_twitter
import threading
import sys

if __name__=="__main__":
    # file = sys.argv[1]
    file='config_5.txt'
    config.get_config(file)
    max_volum=(int)(config.max_size)
    max_history_tweet= max_volum*2/3
    myStreamListener =new_twitter.MyStreamListener()
    new_twitter.get_max(max_volum)
    twitter_stream = tweepy.Stream(auth = new_twitter.get_connection(), listener=myStreamListener)
    # to use thread to control two crawling fucntion
    try:
       t1 = threading.Thread(target=history_twitter.tweeet_crawl(max_history_tweet))
       t2 = threading.Thread(target=twitter_stream.filter(track=config.streaming_topic,locations=config.bound,async=True))
       t1.start()
       t2.start()
       t1.join()
       t2.join()
    except:
       print ("Error:  thread stop")
    print ("congratulation! Data harvest finished!")
