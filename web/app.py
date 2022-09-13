from flask import Flask, jsonify, request
from flask_restful import Api, Resources
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# connecting to database
client = MongoClient('localhost', 27017)
db = client.BrainDumpDB
users = db["Users"]

# running app
if __name__=="__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

