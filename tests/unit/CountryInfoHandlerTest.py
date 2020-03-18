import sys
sys.path.append('../..')

import unittest
from ParserStub import ParserStub
from CountryInfoStub import CountryInfoStub
from CountryInfoHandler import CountryInfoHandler

class TestCountryInfoHandler(unittest.TestCase):
    def test_get_field_exist(Self):
        Self.countryInfoHandler = CountryInfoHandler()
        Self.countryInfoHandler.parser = ParserStub({'info' : 'name'})
        Self.countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa'
            })
        result = Self.countryInfoHandler.get('egypt')
        Self.assertEqual({'name' : 'Egypt'}, result)

    def test_get_no_info(Self):
        Self.countryInfoHandler = CountryInfoHandler()
        Self.countryInfoHandler.parser = ParserStub({})
        Self.countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa'
            })
        result = Self.countryInfoHandler.get('egypt')
        Self.assertEqual({'name' : 'Egypt', 'region' : 'Africa'}, result)

if __name__ == '__main__':
    unittest.main()
