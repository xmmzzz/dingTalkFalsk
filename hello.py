import logging
from flask import Flask
from flask import request
import json

import OAHandler.OARobot

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/app.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

@app.get("/")
def hello():
    logger.info("input hello")
    return "Hello World!"

@app.post("/")
def OAHello():
    req = request.get_json()
    logger.info("|OArobot|%s", str(req))
    return json.dumps(OAHandler.OARobot.sayHello(req))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 1213)