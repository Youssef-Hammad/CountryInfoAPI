from CountryInfo import CountryInfo
from flask_restful import Resource, reqparse

class CountryInfoHandler(Resource):
    def __init__(Self):
        Self.parser = reqparse.RequestParser()
        Self.parser.add_argument('info')
        Self.countryInfo = CountryInfo()
        Self.cachedData = {}
        super().__init__()

    def get_data(Self, name, info):
        requestHash = (name, info)
        if requestHash in Self.cachedData:
            return Self.cachedData[requestHash]
        data = Self.countryInfo.get(name)
        if data == {} or info == None:
            return data
        info = info.split(',')
        result = {}
        for currentInfo in info:
            if currentInfo in data:
                result[currentInfo] = data[currentInfo]
            else:
                result[currentInfo] = None
        Self.cachedData[requestHash] = result
        return result

    def get_info(Self):
        return Self.parser.parse_args()['info']
            
    def get(Self, name):
        info = Self.get_info()
        return Self.get_data(name, info)

