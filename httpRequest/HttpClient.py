import requests
import json

class DingHttpClient:
    def __init__(self):
        self.data = {"appKey" : "dingn3zcecfk2kthtyvl",
            "appSecret" : "ncqxkxYwAu_oWj-xvq8TJrvn8HO5XyzXJhJMz269gnbt1c6L0exfdsD8pWoIEUAz"}
        self.tokenURL = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
        for i in range(3):
            res = requests.post(self.tokenURL, json=self.data)
            if res.status_code == 200:
                break
        if res.status_code == 200:
            self.token = json.loads(res.content)['accessToken']
        else:
            self.token = ""

    def _renew_token(self):
        res = requests.post(self.tokenURL, json=self.data)
        if res.status_code == 200:
            self.token = json.loads(res.content)['accessToken']
        else:
            self.token = ""

    def getDownLoadURL(self, downloadCode: str, robotCode: str) -> str:
        url = "https://api.dingtalk.com/v1.0/robot/messageFiles/download"
        header = {"x-acs-dingtalk-access-token": self.token}
        data = {"downloadCode": downloadCode, "robotCode": robotCode}
        for i in range(3):
            res = requests.post(url, json=data, headers=header)
            if res.status_code == 200:
                break
            else:
                if json.loads(res.content)['code'] == 'InvalidAuthentication':
                    self._renew_token()
                continue
        if res.status_code == 200:
            return json.loads(res.content)['downloadUrl']
        else:
            return None

    def getImage(self, downloadCode: str, robotCode: str) -> bytes:
        url = self.getDownLoadURL(downloadCode, robotCode)
        res = requests.get(url)
        if res.status_code == 200:
            return res.content
        else:
            return None


