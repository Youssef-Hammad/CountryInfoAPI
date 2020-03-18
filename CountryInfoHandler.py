from CountryInfo import CountryInfo
from flask_restful import Resource, reqparse

class CountryInfoHandler(Resource):
    def __init__(Self):
        Self.parser = reqparse.RequestParser()
        Self.parser.add_argument('info')
        Self.countryInfo = CountryInfo()
        super().__init__()

    def __get_data(Self, name, info):
        data = Self.countryInfo.get(name)
        if info == None:
            return data
        info = info.split(',')
        result = {}
        for currentInfo in info:
            if currentInfo in data:
                result[currentInfo] = data[currentInfo]
            else:
                result[currentInfo] = None
        return result

    def __get_info(Self):
        return Self.parser.parse_args()['info']
            
    def get(Self, name):
        info = Self.__get_info()
        return Self.__get_data(name, info)

