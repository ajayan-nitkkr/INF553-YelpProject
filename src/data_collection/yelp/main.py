"""
Author: Ajay Anand
"""

from src.data_collection.yelp.yelp_api_adapter import search_yelp_restaurant

from src.data_collection.yelp.yelp_scraper import scrap_yelp_restaurant_data

if __name__ == '__main__':
    business_id = 'hTzcHtk4-0QJnFUbkKpd5Q'
    name = 'Citi Trends'
    latitude = '36.1783477'
    longitude = '-115.1769162'
    business_data = search_yelp_restaurant(business_id)
    scraped_data = scrap_yelp_restaurant_data(business_data['url'])
    print(scraped_data)