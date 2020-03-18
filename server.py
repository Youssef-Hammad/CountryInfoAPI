from flask import Flask
from flask_restful import Api
from CountryInfoHandler import CountryInfoHandler

app = Flask(__name__)
api = Api(app)

api.add_resource(CountryInfoHandler, '/country/<name>')

app.run(debug=True)
