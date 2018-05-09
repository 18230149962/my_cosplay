import requests
import json

r = requests.post('http://equity.chengantech.com/personal/web/v1/api/createproject')


# print(r.status_code)     #响应状态码
# print(r.content)           #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
# print(r.headers)         #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
# print(r.json())             #Requests中内置的JSON解码器(报错)
# print(r.url)                 # 获取url
# print(r.encoding)         # 编码格式
# print(r.cookies)           # 获取cookie
# print(r.raw)                #返回原始响应体
# print(r.text)               #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# print(r.raise_for_status())    #失败请求(非200响应)抛出异常

