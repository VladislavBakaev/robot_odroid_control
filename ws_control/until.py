import sys
from threading import Thread
import pathlib
import json
import os

pkg_path = os.environ['ROS2_PKG_PATH']

module_path = pkg_path + '/Odroid_arduino_client/src'
sys.path.insert(0, module_path)

from monitor import Monitor, rospy

class MonitorManager():
    def __init__(self):
        self.ros_th = Thread(target = self.run_node).start()
        self.monitor = Monitor()
    
    def run_node(self):
        rospy.init_node('status_checker', disable_signals=True)
        # #rospy.init_node("status_checker")
        # self.monitor = Monitor()

        # while not rospy.is_shutdown():
        #     try:
        #         print("update")
        #         rospy.sleep(0.1)
        #     except Exception as e:
        #         print(e)

    def get_status(self):
        return self.monitor.get_status()

    def get_nav_state(self):
        return self.monitor.get_nav_state()

def get_param():
    wifi_path = pathlib.Path(__file__).parent.parent.absolute()
    file_name = os.path.join(str(wifi_path), 'config_ws.json')

    with open(file_name) as f:
        data = json.load(f)

    return data['rate_internal'], data['rate_slam_param']