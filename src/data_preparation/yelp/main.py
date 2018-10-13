from src.data_preparation.yelp.yelp_api_adapter import search_yelp_restaurant

if __name__ == '__main__':
    business_id = 'hTzcHtk4-0QJnFUbkKpd5Q'
    name = 'Citi Trends'
    latitude = '36.1783477'
    longitude = '-115.1769162'
    data = search_yelp_restaurant(business_id)
    print(data)