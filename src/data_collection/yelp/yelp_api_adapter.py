"""
Author: Ajay Anand
"""

import json
import requests

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # TODO: remove this - we are not using python 2
    # Fall back to Python 2's urllib2 and urllib
    # from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

from src.data_collection.yelp.yelp_credential import API_KEY

API_HOST = "https://api.yelp.com"
SEARCH_PATH = "/v3/businesses/search"
BUSINESS_PATH = '/v3/businesses/'
SEARCH_LIMIT = 5


"""
Search restaurant in yelp based on business id
Reference Link: https://github.com/Yelp/yelp-fusion/blob/master/fusion/python/sample.py#L116
"""
def search_yelp_restaurant(business_id):
    business_path = BUSINESS_PATH + business_id
    url = '{0}{1}'.format(API_HOST, quote(business_path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }
    response = requests.request('GET', url, headers=headers)
    if response and response.text:
        json_response = json.loads(response.text)
        # print(json_response)
    else:
        json_response = None
    return json_response

