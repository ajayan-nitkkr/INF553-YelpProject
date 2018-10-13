
import urllib
from bs4 import BeautifulSoup

"""
Scrap restaurant data from yelp website based on restaurant url
"""
def scrap_yelp_restaurant_data(restaurant_url):
    yelp_path = urllib.urlopen(restaurant_url).read()
    soup = BeautifulSoup(yelp_path, "html.parser")

    # my_dict = {}
    basic_data = soup.find('script', type='application/ld+json')