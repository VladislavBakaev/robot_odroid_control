from flask import Flask
from flask_sockets import Sockets
from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer

server = Flask(__name__)

geventOpt = {'GATEWAY_INTERFACE': 'CGI/1.1',
                'SCRIPT_NAME': '',
                'wsgi.version': (1, 0),
                'wsgi.multithread': True, # XXX: Aren't we really, though?
                'wsgi.multiprocess': True,
                'wsgi.run_once': False}

def create_app(port):
    sockets = Sockets(server)
    http_server = WSGIServer(('',port), server, handler_class=WebSocketHandler, environ=geventOpt)
    from robot_ws_control.controllers import server as server_ws
    sockets.register_blueprint(server_ws)

    return http_server