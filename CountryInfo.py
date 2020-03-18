import requests

class CountryInfo:
    def get(Self, name):
        url = 'https://restcountries.eu/rest/v2/name/' + name
        req = requests.get(url)
        if req.status_code == 404:
            return {}
        return req.json()[0];
