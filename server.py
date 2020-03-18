from flask import Flask
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/country/<name>', methods=['GET'])
def home(name):
    r = requests.get(
            'https://restcountries.eu/rest/v2/name/' + name
            )
    return r.text;


app.run()
