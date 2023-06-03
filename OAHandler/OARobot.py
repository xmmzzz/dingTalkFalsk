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
    text = req["text"]["content"] + "\n"+ "历史对话(3min以内): "
    for i in range(len(his_re)):
        text += "{}\n".format(','.join(his_re[i]))
    res["text"] = {"content": text}
    his_re.append([req["text"]["content"]])
    redisClient.set(staffID, json.dumps(his_re).encode('gbk'))
    return res
