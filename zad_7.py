import requests
import json


class Brewery:
    def __init__(self, obj: dict):
        self.id = obj['id']
        self.name = obj['name']
        self.brewery_type = obj['brewery_type']
        self.street = obj['street']
        self.address_2 = obj['address_2']
        self.address_3 = obj['address_3']
        self.city = obj['city']
        self.state = obj['state']
        self.county_province = obj['county_province']
        self.postal_code = obj['postal_code']
        self.country = obj['country']
        self.longitude = float(obj['longitude']) if obj['longitude'] is not None else 0
        self.latitude = float(obj['latitude']) if obj['latitude'] is not None else 0
        self.phone = obj['phone']
        self.website_url = obj['website_url']
        self.updated_at = obj['updated_at']
        self.created_at = obj['created_at']

    def __str__(self):
        return f'This is a brewery named {self.name} located at {self.country} {self.state} {self.city} {self.street}.' \
               f' Specifically at cords {self.latitude},{self.longitude}'


req = requests.get('https://api.openbrewerydb.org/breweries?per_page=20')
data = json.loads(req.text)

breweries = [Brewery(b) for b in data]

for b in breweries:
    print(b)
