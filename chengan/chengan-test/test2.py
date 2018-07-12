import requests
import json
url = 'http://test.chengantech.cn:8888/center/web/v1/api/login'
my_data = {
"account_type":"personal",
"username":"zhangpengfei1",
"password":"1234567890"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}
# body = {
#
# }
# data_json = json.dumps(my_data)
r = requests.post(url, headers=headers, data=my_data)



print(r.text)