import sys
from threading import Thread
import pathlib
import json
import os

from Odroid_arduino_client.monitor import Monitor, rospy

class MonitorManager():
    def __init__(self):
        self.ros_th = Thread(target = self.run_node).start()
        self.monitor = Monitor()
    
    def run_node(self):
        rospy.init_node('status_checker', disable_signals=True)

    def get_status(self):
        return self.monitor.get_status()

    def get_nav_state(self):
        return self.monitor.get_nav_state()

def get_param():
    path = os.path.dirname(__file__)
    with open(path + "/rate_config_ws.json") as f:
        data = json.load(f)

    return data['rate_internal'], data['rate_slam_param']
