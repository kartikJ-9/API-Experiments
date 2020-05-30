import requests
from flask import Flask, request, jsonify
import os
import traceback
import pandas as pd
url = "https://jobs.github.com/positions.json"

headers= {}

app = Flask(__name__)

@app.route('/')
def seek_job():
    try:
        #url = "https://jobs.github.com/position.json"
        response = requests.request("GET", url, headers=headers, data = payload)
        j = response.json()
        t = response.text.encode('utf8')
        return jsonify(j),200
    except:
        return jsonify({'trace': traceback.format_exc()})

@app.route('/job',methods=['GET'])
def desc():
    try:
        json_ = request.get_json()
		bot_id=json_['bot_id']
		user_id=json_['user_id']
		module_id=json_['module_id']
		channel=json_['channel']
		incoming=json_['incoming_message']
        url = "https://jobs.github.com/positions.json?description="+incoming
        response = requests.request("GET", url, headers=headers, data = incoming)
        j = response.json()
        t = response.text.encode('utf8')
        return jsonify(j),200
    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__=='__main__':
    app.run( debug=True)