from flask import Flask, render_template, request, jsonify

# import ls
import os
import sys

import pywhatkit
import datetime
app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/<name>")
def hello_name(name):
    now = datetime.datetime.now()
    print(now.hour, now.minute+1)
    pywhatkit.sendwhatmsg('+6586687676', 'I need service for '+name, now.hour,now.minute+1,15)
    return "Hello there, we have whatsapp your query to our Project V2D department"



if __name__ == "__main__":
    app.run(debug=True, port=8080)
    # app.run(debug=True, host='127.0.0.1', port=5001)
#https://github.com/bhavaniravi/flask-tutorial/tree/master/app
