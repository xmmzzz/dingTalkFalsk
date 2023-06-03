import json

from redisClient.RedisClient import RedisClient

redisClient = RedisClient("39.107.143.174")

def sayHello(req):
    staffID = req["senderStaffId"]
    his_re = redisClient.get(staffID)
    if his_re is None:
        his_re = []
    else:
        his_re = json.loads(his_re)
    res = {}
    res["msgtype"] = "text"
    res["text"] = {"content": "收到消息: " + req["text"]["content"] + "\n"
                   + "历史对话(3min以内): " + json.dumps(his_re)}
    his_re.append([req["text"]["content"]])
    redisClient.set(staffID, json.dumps(his_re))
    return res
