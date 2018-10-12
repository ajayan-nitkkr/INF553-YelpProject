import requests
import urllib
from bs4 import BeautifulSoup

YELP_BUSINESS_SEARCH_URL = 'https://api.yelp.com/v3/businesses/search'


"""
Get restaurant details and url from yelp by sending server request,
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


"""
Scrap restaurant data from yelp website based on restaurant url
"""
def scrap_yelp_restaurant_data(restaurant_url):
    yelp_path = urllib.urlopen(restaurant_url).read()
    soup = BeautifulSoup(yelp_path, "html.parser")

    # my_dict = {}
    basic_data = soup.find('script', type='application/ld+json')