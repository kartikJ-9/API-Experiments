import requests
from flask import Flask, request, jsonify
import os
import traceback
import pandas as pd
import requests
url = "https://api.spotify.com/v1/search?q="
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'XXXXXXXyour-spotify-auth-keyXXXXXXXX',
}

params = (
    ('q', '"work from home"'),
    ('type', 'playlist'),
)

response = requests.get(url, headers=headers, params=params)

@app.route('/song',methods=['GET'])
def songs():
    try:
        json_ = request.get_json()
		bot_id=json_['bot_id']
		user_id=json_['user_id']
		module_id=json_['module_id']
		channel=json_['channel']
		incoming=json_['incoming_message']
        url = url+incoming
        response = requests.request("GET", url, headers=headers, data = incoming)
        j = response.json()
        t = response.text.encode('utf8')
        return jsonify(j),200
    except:
        return jsonify({'trace': traceback.format_exc()})
#response = requests.get('https://api.spotify.com/v1/search?q=%22work%20from%20home%22&type=playlist', headers=headers)
if __name__=='__main__':
    app.run( debug=True)