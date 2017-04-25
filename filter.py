from gender_detector import GenderDetector
import couchdb
import re
server = couchdb.client.Server('http://0.0.0.0:5984/')
db= server['twitter']
pattern="[a-zA-Z ]+"
#to check tweet_id to filter duplicates
def filter_duplicate(tweet_id):
    for id in db:
        eml=db.get(id)
        if tweet_id==(str)(eml['tweetid']):
           return False
    return True

#to identify gender by first name
def gender_identify(name):
       name=re.findall(pattern,name,re.M)
       detector = GenderDetector('uk')
       temp_name=name[0]
       if ' 'in temp_name:
           temp_name= temp_name.split(" ")
           return detector.guess(temp_name[0])
       else:
           return detector.guess(temp_name)
