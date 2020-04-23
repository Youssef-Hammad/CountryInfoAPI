import sys
sys.path.append('..')

from mock import Mock
from ParserStub import ParserStub
from CountryInfoStub import CountryInfoStub
from CountryInfoHandler import CountryInfoHandler

def test_get_field_exist():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.parser = ParserStub({'info' : 'name'})
    countryInfoHandler.countryInfo = CountryInfoStub({
        'name' : 'Egypt', 
        'region' : 'Africa',
        'capital' : 'Cairo'
        })
    result = countryInfoHandler.get('egypt')
    assert({'name' : 'Egypt'} == result)

def test_get_field_doesnt_exist():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.parser = ParserStub({'info' : 'name'})
    countryInfoHandler.countryInfo = CountryInfoStub({
        'region' : 'Africa',
        'capital' : 'Cairo'
        })
    result = countryInfoHandler.get('egypt')
    assert({'name' : None} == result)

def test_get_no_field():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.parser = ParserStub({'info' : None})
    countryInfoHandler.countryInfo = CountryInfoStub({
        'name' : 'Egypt', 
        'region' : 'Africa',
        'capital' : 'Cairo'
        })
    result = countryInfoHandler.get('egypt')
    assert({'name' : 'Egypt', 'region' : 'Africa', 
        'capital' : 'Cairo'} == result)

def test_get_data_no_info():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.countryInfo = CountryInfoStub({
        'name' : 'Egypt', 
        'region' : 'Africa',
        'capital' : 'Cairo'
        })
    result = countryInfoHandler.get_data('egypt', None)
    assert({'name' : 'Egypt', 'region' : 'Africa', 
        'capital' : 'Cairo'} == result)

def test_get_data_one_info_exist():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.countryInfo = CountryInfoStub({
        'name' : 'Egypt', 
        'region' : 'Africa',
        'capital' : 'Cairo'
        })
    result = countryInfoHandler.get_data('egypt', 'name')
    assert({'name' : 'Egypt'} == result)

def test_get_data_multiple_info_exist():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.countryInfo = CountryInfoStub({
        'name' : 'Egypt', 
        'region' : 'Africa',
        'capital' : 'Cairo'
        })
    result = countryInfoHandler.get_data('egypt', 'name,capital')
    assert({'name' : 'Egypt', 'capital' : 'Cairo'} ==  result)

def test_get_data_info_doesnt_exist():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.countryInfo = CountryInfoStub({
        'name' : 'Egypt', 
        'region' : 'Africa',
        'capital' : 'Cairo'
        })
    result = countryInfoHandler.get_data('egypt', 'name,xyz')
    assert({'name' : 'Egypt', 'xyz' : None} == result)


def test_get_data_not_cached():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.parser = ParserStub({'info' : None})
    data = {
        'name' : 'Egypt', 
        'region' : 'Africa',
        'capital' : 'Cairo'
        }
    countryInfoHandler.countryInfo = CountryInfoStub(data)
    countryInfoHandler.cachedData = {}

    countryInfoHandler.countryInfo.get = Mock(return_value=data)
    result = countryInfoHandler.get('egypt')
    countryInfoHandler.countryInfo.get.assert_called_with('egypt')
    assert(countryInfoHandler.countryInfo.get.call_count == 1)

def test_get_data_cached():
    countryInfoHandler = CountryInfoHandler()
    countryInfoHandler.parser = ParserStub({'info' : None})
    data = {
        'name' : 'Egypt', 
        'region' : 'Africa',
        'capital' : 'Cairo'
        }
    countryInfoHandler.countryInfo = CountryInfoStub(data)
    countryInfoHandler.cachedData = {('egypt', None) : data}

    countryInfoHandler.countryInfo.get = Mock(return_value=data)
    result = countryInfoHandler.get('egypt')
    assert(countryInfoHandler.countryInfo.get.call_count == 0)
