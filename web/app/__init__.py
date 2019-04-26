from flask import Flask
from pymongo import MongoClient


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')

    mongo = MongoClient('mongodb://db')
    db = mongo.aNewDb
    user_num = db['usernum']

    user_num.insert({
        'num_users': 0
    })

    if config:
        app.config.update(config)

    @app.route('/')
    def home():
        prev_num = user_num.find({})[0]['num_users']
        new_num = prev_num + 1
        user_num.update({}, {'$set': { 'num_users': new_num }})
        return str('Hello user {}.'.format(new_num))

    return app
