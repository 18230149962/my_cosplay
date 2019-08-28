def xlssx():
    import requests
    import json
    import random
    list_str = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    veri_str = random.sample(list_str, 4)
    center = ''.join(veri_str)
    my_data ={
                "subjectInfo": {
                "siteid": "03",
                "studyid": "P03",
                "subjinit": center,
                "subtrialid": "15237123",
                "subtrialname": "仅随机"},
                 "entrycriteria": []
    }

    url = 'http://39.98.161.93:18002/rtsm/subject/add.do'
    headers = {
        "Accept":	"application/json, text/plain, */*",
        "Accept-Encoding"	: "gzip, deflate",
        "Accept-Language"	: "zh-CN,zh;q=0.9",
        "Cache-Control":	"no-cache",
        "Connection":	"keep-alive",
        "l": "zh_CN",
        "Pragma": "no-cache",
        "User-Agent":	"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        "token": "0d2f5f477419437081b94b57bc78d760",
    }

    r = requests.post(url, headers=headers, json=my_data)
    print(r)
if __name__ == "__main__":
    xlssx()
