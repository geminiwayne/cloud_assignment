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
import re
from gender_detector import GenderDetector

pattern="[a-zA-Z ]+"

#to identify gender by first name
def gender_identify(name):
      name=re.findall(pattern,name,re.M)
      detector = GenderDetector('uk')
      try:
         temp_name=name[0]
         if ' 'in temp_name:
             temp_name= temp_name.split(" ")
             return detector.guess(temp_name[0])
         else:
             return detector.guess(temp_name)
      except:
         return None

# to check the value is valid or not
def checkText(temp_text):
    if temp_text is None:
        return None
    else:
        return temp_text

# to split hashtags and combine topic and topic splict by ','
def split_combine(a):
    if len(a)>0:
        str=''
        count=0
        for i in a:
           str=str+i[u'text']+','
           count+=1
           if count== len(a):
              str=str+i[u'text']
        return str
    else:
       return None
