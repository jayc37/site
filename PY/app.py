from flask import Flask
from flask import render_template, request,jsonify
from flask_restful import Api
from flask_cors import CORS
import json
import os.path
import logging
from Get_dataJson import sendRequest
# ------------------------------------------------------------------------------
app = Flask(__name__)
# for develop
app.debug = True
api = Api(app)
CORS(app)
# for develop
logging.basicConfig(level = logging.INFO)

# thesis

@app.route("/")
def home():
    

    return render_template("index.html")
    
@app.route("/getdata")
def get_bot_response():
    try:
        URL = "http://data.fixer.io/api/latest?access_key=fe3a9b3f9ac173a3e51d8ea22951cf95"
        dataSet = sendRequest(URL)
        return jsonify(dataSet)
    except Exception as e:
            logging.error('<file app.py>:' + str(e))
if __name__ == "__main__":
  app.run(port=4000)
