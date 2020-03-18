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
            'region' : 'Africa',
            'capital' : 'Cairo'
            })
        result = countryInfoHandler.get('egypt')
        Self.assertEqual({'name' : 'Egypt'}, result)

    def test_get_field_doesnt_exist(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.parser = ParserStub({'info' : 'name'})
        countryInfoHandler.countryInfo = CountryInfoStub({
            'region' : 'Africa',
            'capital' : 'Cairo'
            })
        result = countryInfoHandler.get('egypt')
        Self.assertEqual({'name' : None}, result)

    def test_get_no_field(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.parser = ParserStub({'info' : None})
        countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa',
            'capital' : 'Cairo'
            })
        result = countryInfoHandler.get('egypt')
        Self.assertEqual({'name' : 'Egypt', 'region' : 'Africa', 
            'capital' : 'Cairo'}, result)

    def test_get_data_no_info(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa',
            'capital' : 'Cairo'
            })
        result = countryInfoHandler.get_data('egypt', None)
        Self.assertEqual({'name' : 'Egypt', 'region' : 'Africa', 
            'capital' : 'Cairo'}, result)

    def test_get_data_one_info_exist(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa',
            'capital' : 'Cairo'
            })
        result = countryInfoHandler.get_data('egypt', 'name')
        Self.assertEqual({'name' : 'Egypt'}, result)

    def test_get_data_multiple_info_exist(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa',
            'capital' : 'Cairo'
            })
        result = countryInfoHandler.get_data('egypt', 'name,capital')
        Self.assertEqual({'name' : 'Egypt', 'capital' : 'Cairo'}, result)

    def test_get_data_info_doesnt_exist(Self):
        countryInfoHandler = CountryInfoHandler()
        countryInfoHandler.countryInfo = CountryInfoStub({
            'name' : 'Egypt', 
            'region' : 'Africa',
            'capital' : 'Cairo'
            })
        result = countryInfoHandler.get_data('egypt', 'name,xyz')
        Self.assertEqual({'name' : 'Egypt', 'xyz' : None}, result)

if __name__ == '__main__':
    unittest.main()
