"""Webserver
"""

import os
import sys


from flask import Flask

from bbox_predictor import config
from bbox_predictor.predictor.simple import Simple as Predictor
from bbox_predictor.server.flask import init_flask
from bbox_predictor.server.jsonrpc import init_jsonrpc


if __name__ == '__main__':
    # Arguments:
    #  1 path to the model.
    if len(sys.argv) != 2:  # Number of arguments correct
        print("Usage: {} <path model>".format(sys.argv[0]))
        exit(0)
    path_model = sys.argv[1]

    # Model file exists
    if not os.path.exists(path_model):
        print("ERROR: cannot find model at {}".format(path_model))
        exit(0)
    print("Model: {}".format(os.path.abspath(path_model)))
    predictor = Predictor(path_model)

    # set the project root directory as the static folder, you can set others.
    app = Flask(__name__, static_url_path='')
    init_flask(app)
    init_jsonrpc(app, predictor)
    app.run(
        host=config.SERVER_HOST,
        port=config.SERVER_PORT,
        debug=config.SERVER_DEBUG
    )
