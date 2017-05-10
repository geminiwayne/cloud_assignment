#################################
#Team 4                         #
#Melbourne,Sydney,Brisbane,Perth#
#Dong Wang     773504           #
#Danping Zeng  777691           #
#Jia Zhen      732355           #
#Jinghan Liang 732329           #
#Sixue Yang    722804           #
#################################
import json
import couchdb

print ("Please input the path of files and area_code,area_name,rate by(,):")
path=raw_input()
temp_path=path.split(",")
couch =couchdb.Server('http://admin:password@115.146.93.201:5984/')
db= couch['aurin_data']
with open(temp_path[0], 'r') as f:
     data = json.load(f)
     for each in data[u'features']:
         temp=each[u'id'].split(".")
         doc={'rate':each[u'properties'][temp_path[3]],'area_name':each[u'properties'][temp_path[2]],'area_code':each[u'properties'][temp_path[1]],'topic':temp[0]}
         db.save(doc)
print ("Task finished!")
