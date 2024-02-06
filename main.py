import requests
import json

url = "http://api.tvmaze.com/search/shows?q=friends"
data = requests.get(url).text

print(data)