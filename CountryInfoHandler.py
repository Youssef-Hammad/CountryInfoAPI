from CountryInfo import CountryInfo
from flask_restful import Resource, reqparse

class CountryInfoHandler(Resource):
    def __get_data(Self, name, info):
        countryInfo = CountryInfo()
        data = countryInfo.get(name)
        if info == None:
            return data
        info = info.split(',')
        result = {}
        for currentInfo in info:
            result[currentInfo] = data[currentInfo]
        return result

    def __get_info(Self):
        parser = reqparse.RequestParser()
        parser.add_argument('info')
        return parser.parse_args()['info']
            
    def get(Self, name):
        info = Self.__get_info()
        return Self.__get_data(name, info)

