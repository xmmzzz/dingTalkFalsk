import requests
import json

if __name__ == '__main__':
    url = "http://pub.dqyuan.top:8003"
    data = {}
    data["prompt"] = "你是谁"
    data["history"] = []
    res = requests.post(url=url, json=data)
    res = json.loads(res.content)
    print(res)