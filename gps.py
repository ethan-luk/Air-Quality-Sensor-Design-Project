import requests
import os
from dotenv import load_dotenv
# import geocoder
import json

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GEOLOCATION_URL = os.getenv('GEOLOCATION_URL')

def find_current_location():
    data = {"key": GOOGLE_API_KEY}
    try:
        req = requests.post(url=GEOLOCATION_URL, json=data)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    results = req.text
    results_dict = json.loads(results)
    print(results_dict)
    return results_dict

find_current_location()


# def find_current_location():
#     loc = geocoder.ip('me')
#     coord = {
#         "lat": loc.latlng[0], 
#         "long": loc.latlng[1]
#     }
#     return coord

# loc = geocoder.ip('me')
# g = loc.latlng
# print(g)