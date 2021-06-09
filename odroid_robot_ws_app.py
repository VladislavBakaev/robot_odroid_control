import argparse
from ws_control import create_app

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--bind", type=str,
                help="config file")
    
    args = parser.parse_args()

    if args.bind != None:
        port = int(args.bind)
    else:
        port = 5001

    server = create_app(port)
    print("Web socket server start on port: {}".format(port))
    server.serve_forever()