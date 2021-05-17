
from flask import Blueprint, request
import time
import gevent
import json
import pathlib
import sys

from ws_control.until import MonitorManager, get_param

server = Blueprint('ws', __name__, url_prefix=r'/ws/robot')

rate_internal, rate_slam_param = get_param()
monitor_manager = MonitorManager()

@server.route('/internal')
def internal_state(ws):
    while not ws.closed:
        try:
            data = monitor_manager.get_status()
        #     data = {'laser': [time.time(), False],
		# 'odom': [time.time(), False],
		# 'serial': [time.time(), False]}

            ws.send(json.dumps(data))
            gevent.sleep(1/rate_internal)
        except Exception as e:
            print(e)
            ws.close()

@server.route('/slam/param')
def slam_param(ws):
    while not ws.closed:
        try:
            data = monitor_manager.get_nav_state()
        #     data = {'state': 'none', 
		# 'x_target': 0.0, 
		# 'y_target': 0.0, 
		# 'theta_target': 0.0,
		# 'x_real': 0.0,
		# 'y_real': 0.0,
		# 'theta_real': 0.0}
            ws.send(json.dumps(data))
            gevent.sleep(1/rate_internal)
        except Exception as e:
            print(e)
            ws.close()
