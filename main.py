from flask import Flask, send_file, request, jsonify
import os
import requests
import numpy as np
from netCDF4 import Dataset

app = Flask(__name__)
mag = None
def init():
    fp = '/home/cully/Downloads/CCMP_Wind_Analysis_20160530_V02.0_L3.0_RSS.nc'
    rootgrp = Dataset(fp, 'r', format='NETCDF4')
    mag = np.sqrt(rootgrp.variables['uwnd'][0,:,:]**2 + rootgrp.variables['vwnd'][0,:,:]**2)
    

@app.route('/')
def mainroute():
    return send_file('index.html')


@app.route('/game')
def game():
    return send_file('game.html')

@app.route('/score/<lat>/<lon>')
def score(lat, lon):
    url = 'https://api.planetos.com/v1/datasets/rss_ccmp_winds_v2/point'
    api_key = os.environ['PLANET_OS_API_KEY']
    lat = float(lat)
    lon = float(lon)
    payload = {'apikey':api_key,
               'lat':lat,
               'lon':lon}
    response = requests.request('GET', url, params=payload)
    score = {}
    if response.ok:
        data = response.json()
        u = data['entries'][0]['data']['uwnd']
        v = data['entries'][0]['data']['vwnd']
        score['user_speed'] = np.sqrt(u**2 + v**2)
    else: 
        score['user_speed'] = 0.0
    
    
    return jsonify(score)
    
    

if __name__ == "__main__":
    init()

    app.run()
    
