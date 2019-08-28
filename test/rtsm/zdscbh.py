# 这个是自动生成受试者编号的功能
i = 0
def sy():
    global i
    i += 1
    n = "01"+"%03d" % i
    import requests
    import json
    import random
    list_str = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    veri_str = random.sample(list_str, 4)
    center = ''.join(veri_str)
    my_data ={
            "subjectInfo": {
                "siteid": "01",
                "studyid": "P01",
                "subjid": n,
                "subjinit": center,
                "subtrialid": "15237121",
                "subtrialname": "区组随机"
            },
            "entrycriteria": []
    }

    print(my_data)
if __name__ == "__main__":
    sy()