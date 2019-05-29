from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        cf = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs0bj = BeautifulSoup(cf.read())
        HS = bs0bj.h1
    except AttributeError as e:
        return None
    return HS
HS = urlopen("http://localhost/edc_zpf_test")
job = BeautifulSoup(HS, 'lxml')
if HS == None:
    print("出错了")
else:
    print(HS)
print(job)
