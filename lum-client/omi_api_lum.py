import acoustid
import sys
import webbrowser
import json
import pycurl
import pprint
import requests


jsonfile = open("../lum-client/result.json" , "r")
json_file = json.load(jsonfile)

apikey = 'cSpUJKpD'


title_list=[]
artist_list=[]
percentage_list = [5, 10, 8, 9, 15, 12, 7, 21, 11, 16]
for i in range(len(json_file)):
    data = json_file[i]
    result = "http://localhost:8888/api/recordings/;limit=1;offset=1?title=%27put_title%27&artist=%27put_artist%27"
    result = result.replace('put_title', data[1])
    result = result.replace('put_artist', data[0])
    dictionary = requests.get(result).json()
    title = dictionary["results"][0]["title"]
    artists = dictionary["results"][0]["artists"][0]
    title_list.append(title)
    artist_list.append(artists)


echowe_dic = {"title" : title_list, "artist" : artist_list, "percentage" : percentage_list}


with open('echowe.json', 'w') as fp:
    	json.dump(echowe_dic, fp)
