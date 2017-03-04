from flask import Flask, send_file, request
import os
import requests
import numpy as np

app = Flask(__name__)


@app.route('/')
def mainroute():
    return send_file('index.html')


@app.route('/game')
def game():
    return send_file('game.html')

@app.route('/score/<lat>/<lon>'):
def score():
    url = 'https://api.planetos.com/v1/datasets/rss_ccmp_winds_v2/point'
    api_key = os.environ['PLANET_OS_API_KEY']
    lat = float(lat)
    lon = float(lon)
    payload = {'apikey':api_key,
               'lat':lat,
               'lon':lon}
    response = requests.request('GET', url, params=payload)
    if response.ok:
        data = response.json()
        u = data['entries'][0]['data']['uwnd']
        v = data['entries'][0]['data']['vwnd']
        score = np.sqrt(u**2 + v**2)
    else: score = 0
    return score
    

if __name__ == "__main__":
    app.run()
