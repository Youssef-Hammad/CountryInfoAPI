import requests

def test_valid_api_call():
    url = 'http://localhost:5000/country/egypt?info=name,region,population'
    response = requests.get(url)
    assert response != None
    assert response.json() ==   {
                                    "name": "Egypt",
                                    "region": "Africa",
                                    "population": 91290000
                                } 

def test_invalid_api_call():
    url = 'http://localhost:5000/co/egypt'
    response = requests.get(url)
    assert response != None
    assert response.status_code == 404

def test_one_info_field():
    url = 'http://localhost:5000/country/egypt?info=name'
    response = requests.get(url)
    assert response != None
    assert response.json() ==   {
                                    "name": "Egypt",
                                }

def test_multiple_info_field():
    url = 'http://localhost:5000/country/egypt?info=name,region'
    response = requests.get(url)
    assert response != None
    assert response.json() ==   {
                                    "name": "Egypt",
                                    "region": "Africa",
                                } 

def test_invalid_country_name():
    url = 'http://localhost:5000/co/egypt?info=name,region'
    response = requests.get(url)
    assert response != None
    assert response.status_code == 404



def test_valid_country_name():
    url = 'http://localhost:5000/country/egypt?info=name,region'
    response = requests.get(url)
    assert response != None
    assert response.json() ==  {
                                        "name": "Egypt",
                                        "region": "Africa",
                                    }

def test_no_info_field():
    url = 'http://localhost:5000/country/egypt'
    response = requests.get(url)
    assert response != None
    assert response.json() ==   {
    "name": "Egypt",
    "topLevelDomain": [
        ".eg"
    ],
    "alpha2Code": "EG",
    "alpha3Code": "EGY",
    "callingCodes": [
        "20"
    ],
    "capital": "Cairo",
    "altSpellings": [
        "EG",
        "Arab Republic of Egypt"
    ],
    "region": "Africa",
    "subregion": "Northern Africa",
    "population": 91290000,
    "latlng": [
        27.0,
        30.0
    ],
    "demonym": "Egyptian",
    "area": 1002450.0,
    "gini": 30.8,
    "timezones": [
        "UTC+02:00"
    ],
    "borders": [
        "ISR",
        "LBY",
        "SDN"
    ],
    "nativeName": "\u0645\u0635\u0631\u200e",
    "numericCode": "818",
    "currencies": [
        {
            "code": "EGP",
            "name": "Egyptian pound",
            "symbol": "\u00a3"
        }
    ],
    "languages": [
        {
            "iso639_1": "ar",
            "iso639_2": "ara",
            "name": "Arabic",
            "nativeName": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"
        }
    ],
    "translations": {
        "de": "\u00c4gypten",
        "es": "Egipto",
        "fr": "\u00c9gypte",
        "ja": "\u30a8\u30b8\u30d7\u30c8",
        "it": "Egitto",
        "br": "Egito",
        "pt": "Egipto",
        "nl": "Egypte",
        "hr": "Egipat",
        "fa": "\u0645\u0635\u0631"
    },
    "flag": "https://restcountries.eu/data/egy.svg",
    "regionalBlocs": [
        {
            "acronym": "AU",
            "name": "African Union",
            "otherAcronyms": [],
            "otherNames": [
                "\u0627\u0644\u0627\u062a\u062d\u0627\u062f \u0627\u0644\u0623\u0641\u0631\u064a\u0642\u064a",
                "Union africaine",
                "Uni\u00e3o Africana",
                "Uni\u00f3n Africana",
                "Umoja wa Afrika"
            ]
        },
        {
            "acronym": "AL",
            "name": "Arab League",
            "otherAcronyms": [],
            "otherNames": [
                "\u062c\u0627\u0645\u0639\u0629 \u0627\u0644\u062f\u0648\u0644 \u0627\u0644\u0639\u0631\u0628\u064a\u0629",
                "J\u0101mi\u02bbat ad-Duwal al-\u02bbArab\u012byah",
                "League of Arab States"
            ]
        }
    ],
    "cioc": "EGY"
} 

