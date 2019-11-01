from flask import Flask
from flask import request
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(str(os.environ.get('MONGOHOST')), int(os.environ.get('MONGOPORT')))
database = client['money_leakst']
collection = database['money_leakst']


@app.route('/money_leakst/')
def index():
    return 'money leakst api'

@app.route('/money_leakst/', methods=['POST'])
def create():
    try:
        money = request.get_json()
        insert = collection.insert_one(money)
        if insert.acknowledged:
            return str(money)
        else:
            return "error obteniendo datos."
    except:
        return "error creando registro."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)
