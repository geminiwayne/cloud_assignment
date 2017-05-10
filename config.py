#################################
#Team 4                         #
#Melbourne,Sydney,Brisbane,Perth#
#Dong Wang     773504           #
#Danping Zeng  777691           #
#Jia Zhen      732355           #
#Jinghan Liang 732329           #
#Sixue Yang    722804           #
#################################
#  a key and token for twitter app to get permission of tweepy
consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""
geo=""
topic=""
bound=[]
streaming_topic=[]
max_size=0

#to covert the type and put in another list
def copy_convert(old_list,new_list,option):
    if option==1:
        for elem in old_list:
            new_list.append(float(elem))
        return new_list
    if option==0:
        for elem in old_list:
            new_list.append(elem)
        return new_list

def get_config(file_1):
  global consumer_key
  global consumer_secret
  global access_token
  global access_secret
  global geo
  global topic
  global bound
  global streaming_topic
  global max_size
    
  #to read file for these data
  count=0
  for line in open (file_1,'r'):
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
       if count==6:
          temp=line.split(',')
          copy_convert(temp,bound,1)
       if count==7:
          temp1=line.split(',')
          copy_convert(temp1,streaming_topic,0)
       if count==8:
          max_size=(int)(line)
       count+=1
