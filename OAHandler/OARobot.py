def sayHello(req):
    res = {}
    res["msgtype"] = "text"
    res["text"] = {"content": "收到消息: " + req["text"]["content"]}
    return res
