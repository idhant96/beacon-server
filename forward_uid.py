from flask import Flask
import requests
import time
import atexit





app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'root hello'

@app.route('/getcode')
def getcode():
    url = "http://13.52.76.220:8080/beaconuid"
    seconds = 5
    r = requests.get(url)
    return r.text