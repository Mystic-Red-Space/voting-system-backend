import json

from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv(override=True)
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/voting"
mongo = PyMongo(app)


def json_resp(content, resp_code=200):
    return app.make_response(
        (json.dumps(content, ensure_ascii=False, default=str),
         resp_code, {'Content-type': 'application/json; charset=utf-8'}))


@app.route('/')
def voting_list():
    vote_list = mongo.db.list.find()
    return json_resp(list(vote_list))


if __name__ == '__main__':
    app.run()
