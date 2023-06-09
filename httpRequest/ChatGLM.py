import pickle

import requests
from redisClient import RedisClient
import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/app.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)



class ChatGLMClient:
    def __init__(self):
        self.url = "http://pub.dqyuan.top:8003"
        self.redisClient = RedisClient.RedisClient("127.0.0.1")

    def sendRequest(self, data):
        res = requests.post(self.url, json=data)
        logger.info("|%s|%s|", data, res.text)
        res = json.loads(res.content)
        return res

    def sendPrompt(self, text: str, imgs: list, staffID: str):
        his_re = self.redisClient.get(staffID)
        if his_re is None:
            his_re = []
        else:
            his_re = pickle.loads(his_re)
        data = {"text": text, "history": his_re}
        if len(imgs) > 0:
            data["imageUrl"] = imgs[0]
        res = self.sendRequest(data)
        if res['status'] != 200:
            return "这个问题我不知道该怎么回答。"
        else:
            this_his = []
            this_his.append(text)
            this_his.append(res['result'])
            his_re.append(this_his)
            self.redisClient.set(staffID, pickle.dumps(his_re))
            return res['result']

