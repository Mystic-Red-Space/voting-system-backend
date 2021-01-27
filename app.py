from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv(override=True)
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/voting"
mongo = PyMongo(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
