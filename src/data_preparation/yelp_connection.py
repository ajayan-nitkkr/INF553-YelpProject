import requests
from src.configuration.yelp_credential import YELP_CLIENT_SECRET, YELP_CLIENT_ID

YELP_BUSINESS_SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'


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


"""
Get restaurant details from yelp by sending server request,
based on restaurant name, location and zip code
"""
def get_yelp_restaurant_data_using_token(token, name, location, zip):
    headers = {'Authorization': 'bearer %s' % token}
    params = {
        'location': name,
        'term': location,
        'zip_code': zip
    }
    resp = requests.get(url=YELP_BUSINESS_SEARCH_URL, params=params, headers=headers)
    return resp.content