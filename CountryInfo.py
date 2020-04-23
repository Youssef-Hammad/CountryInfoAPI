import requests

countries = {}

class CountryInfo:
    def get(Self, name):
        if name in countries:
            return countries[name]
        url = 'https://restcountries.eu/rest/v2/name/' + name
        req = requests.get(url)
        if req.status_code == 404:
            return {}
        countries[name] = req.json()[0]
        return req.json()[0]
