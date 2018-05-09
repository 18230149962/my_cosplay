import unittest
import json
import requests
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
import HTMLTestRunner_jpg
from BeautifulReport import BeautifulReport


# ====定义发送邮件====
def send_mail(file_new):
    # 找到html复制到邮件上
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEMultipart()
    msg["subject"] = "接口测试报告"    #主题
    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)
    # 附件
    att=MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename=" '+ now +' 测试报告.html"'
    msg.attach(att)
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('18230149962@163.com','qwe123456.')
    smtp.sendmail('18230149962@163.com','18230149962@163.com',msg.as_string())
    smtp.quit()

    print('邮件已发送')

# ===查找测试目录，找到最新报告===
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key = lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    test_dir = './test_case'
    test_report = './test_report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'test*.py')
    # 按照一定的格式获取当前的时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    # 定义报告存放路径
    filename = './test_report/' + now + '_result.html'
    fp = open(filename, 'wb')
    # # 定义测试报告
    # runner = HTMLTestRunner_jpg.HTMLTestRunner(stream = fp,title = "Web B端接口测试报告", description = "测试用例执行情况：")
    # # 运行测试
    # runner.run(discover)
    result = BeautifulReport(discover)
    result.report(filename=filename, description='Web B端接口测试报告', log_path='test_report')
    fp.close()
    new_report = new_report(test_report)
    send_mail(new_report)
