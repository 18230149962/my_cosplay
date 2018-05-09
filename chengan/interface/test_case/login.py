import requests
import json

class Blog():

    def __init__(self, s):
        # s = requests.session()#全局参数
        self.s = s
    def login(self):
        """test first: username password is normal"""
        url = 'http://test.chengantech.cn:8888/center/web/v1/api/login'
        headers={
            "Accept":"application/json, text/plain, */*",
            "Origin":"http://equity.chengantech.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Content-Type":"application/json;charset=UTF-8",
            "Referer":	"http://equity.chengantech.com/login",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9"
        }
        json_data = {
                    "account_type":"company",
                    "username":"zhangpengfei",
                    "password":"1234567890"
                    }
        res = self.s.post(url,headers=headers,json=json_data,verify=False)
        result1 = res.content
        # print(result1)
        return res.json()

if __name__ == '__main__':
    s = requests.session()
    Blog(s).login()
