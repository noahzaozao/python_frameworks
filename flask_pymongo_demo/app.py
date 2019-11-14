from flask import Flask
from flask_pymongo import PyMongo
import json

import sys
sys.path.append('.')

from config import config


app = Flask(__name__)
app.config.from_object(config['dev'])
mongo = PyMongo(app)


@app.route('/insert')
def test_insert():
    user = {
        'id': 1,
        'online': True
    }
    mongo.db.users.insert_one(user)
    online_user = mongo.db.users.find_one({'id': 1})
    online_user_data = {
        '_id': str(online_user.pop('_id')),
        'id': online_user.pop('id'),
        'online': online_user.pop('online'),
    }
    return {
        'data': json.dumps(online_user_data)
    }


@app.route('/list')
def test_list():
    online_users = mongo.db.users.find({'online': True})
    online_users_data = []
    for online_user in online_users:
        online_users_data.append({
            '_id': str(online_user.pop('_id')),
            'id': online_user.pop('id'),
            'online': online_user.pop('online'),
        })
    return {
        'data': json.dumps(online_users_data)
    }


if __name__ == '__main__':
    app.run(debug=True, port=8000)
