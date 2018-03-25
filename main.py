import config
import requests
import sys
import json

search_word = "chicken"
api_call = f"https://api.edamam.com/search?q={search_word}&app_id={config.app_id}&app_key={config.app_key}"

print(api_call)
#response = requests.get("http://api.open-notify.org/iss-now.json")

with open("chicken.json", 'r') as f:
  chicken_result = json.load(f)