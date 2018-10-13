import urllib
import requests
from bs4 import BeautifulSoup

"""
Scrap restaurant data from yelp website based on restaurant url
"""
def scrap_yelp_restaurant_data(restaurant_url):
    # yelp_path = urllib.urlopen(restaurant_url).read()
    yelp_path = requests.get(restaurant_url, verify=False)
    soup = BeautifulSoup(yelp_path.text)
    print(soup.title)
    # my_dict = {}
    basic_data = soup.find('script', type='application/ld+json')
    print(basic_data)