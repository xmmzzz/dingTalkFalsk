import logging
from flask import Flask

app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/app.log", maxBytes=1024*1024*100, backupCount=100)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

@app.get("/")
def hello():
    logger.info("input hello")
    return "Hello World!"

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)