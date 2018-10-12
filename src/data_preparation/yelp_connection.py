import requests
from src.configuration.yelp_credential import *

"""
Get the access token for yelp
"""
def get_access_token():
    app_id = YELP_CLIENT_ID
    app_secret = YELP_CLIENT_SECRET
    data = {'grant_type': 'client_credentials',
            'client_id': app_id,
            'client_secret': app_secret}
    token = requests.post('https://api.yelp.com/oauth2/token', data=data)
    access_token = token.json()['access_token']
    return access_token