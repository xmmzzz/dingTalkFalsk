from httpRequest import ChatGLM
import logging

chatGPTClient = ChatGLM.ChatGLMClient()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/app.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

def sayHello(req):
    staffID = req["senderStaffId"]
    res = {}
    res["msgtype"] = "text"
    resText = chatGPTClient.sendPrompt(req["text"]["content"], staffID)
    res["text"] = {"content": resText}
    return res
