from httpRequest import ChatGLM, HttpClient
import logging

chatGPTClient = ChatGLM.ChatGLMClient()
dingHttpClient = HttpClient.DingHttpClient()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/app.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def sayHello(req):
    staffID = req["senderStaffId"]
    text, imgs = _handle_content(req)
    text = text.replace('@啊哈', '')
    resText = chatGPTClient.sendPrompt(text, imgs, staffID)
    res = {}
    res["msgtype"] = "text"
    res["text"] = {"content": resText}
    return res

def _handle_content(req):
    if req['msgtype'] == 'text':
        return req["text"]["content"], []
    elif req['msgtype'] == 'picture':
        img = dingHttpClient.getDownLoadURL(req['content']['downloadCode'], req['robotCode'])
        return "", [img]
    elif req['msgtype'] == 'richText':
        return _handle_richText(req)
    else:
        return "", []

def _handle_richText(req):
    richText = req['content']['richText']
    text = ""
    imgs = []
    for part in richText:
        if 'text' in part:
            text += part["text"]
        elif part['type'] == 'picture':
            imgs.append(dingHttpClient.getDownLoadURL(part['downloadCode'], req['robotCode']))

    return text, imgs
