from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

reqs = parse_requirements('requirements.txt')

setup(
    name="robot_odroid_control",
    version="1.0.0",
    description="Web server for robot corol",
    py_modules=["odroid_robot_ws_app"],
    packages=["robot_ws_control"],
    package_data={"robot_ws_control": ["rate_config_ws.json"]},
    install_requires=reqs,
    scripts=['odroid_robot_ws_app.py']
)
