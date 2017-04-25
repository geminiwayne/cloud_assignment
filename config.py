#  a key and token for twitter app to get permission of tweepy
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
geo=""
topic=""
count=0

#to read file for these data
for line in open ('config.txt','r'):
   line=line.strip('\n')
   if count==0:
       consumer_key=line
   if count==1:
       consumer_secret=line
   if count==2:
       access_token=line
   if count==3:
       access_secret=line
   if count==4:
       geo=line
   if count==5:
       topic=line
   count+=1

