from gender_detector import GenderDetector
import couchdb
import re

#to use a list to store tweetid to filter duplicates
tweetId=[]
pattern="[a-zA-Z ]+"
##to check tweet_id to filter duplicates
def  filter_duplicate(tweet_id):
    if tweet_id in tweetId:
       return False
    else:
       tweetId.append(tweet_id)
       return True

##to identify gender by first name
#def gender_identify(name):
#       name=re.findall(pattern,name,re.M)
#       detector = GenderDetector('uk')
#       temp_name=name[0]
#       if ' 'in temp_name:
#           temp_name= temp_name.split(" ")
#           return detector.guess(temp_name[0])
#       else:
#           return detector.guess(temp_name)

# to check the value is valid or not
def checkText(temp_text):
    if temp_text is None:
        return None
    else:
        return temp_text

