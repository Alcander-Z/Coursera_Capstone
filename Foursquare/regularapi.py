import os
import json
import requests
from datetime import datetime
from . import secret


URL = 'https://api.foursquare.com/v2/'
CLIENT_ID = os.getenv('FOURSQUARE_ID')
CLIENT_SECRET = os.getenv('FOURSQUARE_SECRET')


def id():
    now = datetime.now().strftime('%Y%m%d')
    return {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'v': now,
    }


def venues(endpoint, **kwargs):
    url = URL + 'venues/'
    param = id()
    param = {
        **param,
        **kwargs
    }

    try:
        result = requests.get(url=url+endpoint, params=param).json()['response']['groups'][0]['items']
    except Exception as e:
        print(e)
        result = None

    if result:
        venues_list = []
        for v in result:
            venues_list.append([
                v['venue']['name'],
                v['venue']['location']['lat'],
                v['venue']['location']['lng'],
                v['venue']['categories'][0]['name']
            ])
        return venues_list
