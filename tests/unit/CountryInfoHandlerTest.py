import sys
sys.path.append('../..')

import unittest
from ParserStub import ParserStub
from CountryInfoStub import CountryInfoStub
from CountryInfoHandler import CountryInfoHandler

class TestCountryInfoHandler(unittest.TestCase):
    def test_get_field_exist(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.parser = ParserStub({'info' : 'name'})
        countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa'
            })
        result = countryInfoHandler.get('egypt')
        Self.assertEqual({'name' : 'Egypt'}, result)

    def test_get_no_info(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.parser = ParserStub({'info' : None})
        countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa'
            })
        result = countryInfoHandler.get('egypt')
        Self.assertEqual({'name' : 'Egypt', 'region' : 'Africa'}, result)

    def test_get_field_doesnt_exist(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.parser = ParserStub({'info' : 'name'})
        countryInfoHandler.countryInfo = CountryInfoStub({
            'region' : 'Africa'
            })
        result = countryInfoHandler.get('egypt')
        Self.assertEqual({'name' : None}, result)

if __name__ == '__main__':
    unittest.main()
