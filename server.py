from flask import Flask, request
import requests
import json

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/country/<name>', methods=['GET'])
def home(name):
    queries = request.args.get('info');
    url = 'https://restcountries.eu/rest/v2/name/' + name
    if queries != None:
        queries = queries.split(',')
        url += '?fields='
        for n in queries:
            url = url + n + ';'
    r = requests.get(url)
    return r.json()[0]

app.run()
