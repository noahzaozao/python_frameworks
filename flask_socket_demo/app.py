import time
import json
from flask_sockets import Sockets
from flask import Flask
from gevent import monkey
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler
monkey.patch_all()

import sys
sys.path.append('.')

from config import config


app = Flask(__name__)
app.config.from_object(config['dev'])
sockets = Sockets(app)

now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))


@sockets.route('/test')
def echo_socket(ws):
    while not ws.closed:
        ws.send(str("message sent"))

        message = ws.receive()
        if message is not None:
            print("%s receive msg==> " % now, str(json.dumps(message)))
            ws.send(str(json.dumps(message)))
        else:
            print(now, "no receive")


@app.route('/')
def hello():
    return 'Hello World! server start!'


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 9000), app, handler_class=WebSocketHandler)
    print('server start')
    server.serve_forever()
