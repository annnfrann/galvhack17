from flask import Flask, send_file, request, jsonify
import os
import requests
import re
import numpy as np
from netCDF4 import Dataset

app = Flask(__name__)
mag = None

rootgrp = None

fp = '/Users/brentn/github/galvhack17/data.remss.com/ccmp/v02.0/Y2016/M01/CCMP_Wind_Analysis_20160130_V02.0_L3.0_RSS.nc'
rootgrp = Dataset(fp, 'r', format='NETCDF4')
mag = np.sqrt(rootgrp.variables['uwnd'][0,:,:]**2 + rootgrp.variables['vwnd'][0,:,:]**2)


def decay_scorer(lat, lon, speed, l=.9):
    w_diff = mag-speed
    lats = rootgrp.variables['latitude']
    lons = rootgrp.variables['longitude']
    #dist_matrix = np.sqrt((rootgrp.variables['latitude']-lat)**2 + (rootgrp.variables['longitude']-lon)**2)
    dist_matrix = np.ones((len(lats), len(lons)))
    
    # for i in np.arange(len(lats)):
    #     for j in np.arange(len(lons)):
    #         dist_matrix[i,j] = np.sqrt((lats[i]-lat)**2 + (lons[j]-lon)**2)
    score_matrix = w_diff / (dist_matrix**l)
    best_lat_idx, best_lon_idx = (np.argmax(score_matrix.max(axis=1).T), np.argmax(score_matrix.max(axis=0)))
    best_lat = lats[best_lat_idx]
    best_lon = lons[best_lon_idx] - 360
    best_score = np.max(mag)
    print(best_lat, best_lon, best_score)
    return (best_lat, best_lon, best_score)

@app.route('/rack')
@app.route('/')
def mainroute():
    return send_file('rack.html')


@app.route('/game')
def game():
    return send_file('game.html')
@app.route('/howto')
def howto():
    return send_file('howto.html')

@app.route('/score/<coords>')
def score(coords):
    lat, lon = [ float(x) for x in  re.sub('[()]', '', coords).split(',')]
    url = 'https://api.planetos.com/v1/datasets/rss_ccmp_winds_v2/point'
    api_key = '522d9c3837084486a88444b8bd0d62e0'
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
        score['user_speed'] = round(np.sqrt(u**2 + v**2), 3)
    else: 
        score['user_speed'] = 0.0
    
    best_lat, best_lon, best_speed = decay_scorer(lat, lon, score['user_speed'])
    score['best_lat'] = str(best_lat)
    score['best_lon'] = str(best_lon)
    score['best_speed'] = str(best_speed)
    #print(best_lat, best_lon, best_score)
    return jsonify(score)
    
    

if __name__ == "__main__":
    #init()

    app.run()
    
