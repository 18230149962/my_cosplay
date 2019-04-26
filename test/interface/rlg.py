import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(file_new):
    # 找到html复制到邮件上
    f = open(file_new)
    mail_body = f.read()
    f.close()
    msg=MIMEMultipart()
    msg["subject"] = "接口测试报告"    #主题
    # # 正文
    # body = MIMEText(mail_body, "html", "utf-8")
    # msg.attach(body)
    # 附件
    att=MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="测试报告.html"'
    msg.attach(att)
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('18230149962@163.com','qwe123456.')
    smtp.sendmail('18230149962@163.com','18230149962@163.com',msg.as_string())
    smtp.quit()

    print('邮件已发送')




if __name__ == '__main__':
    file_path = "D:\\chengan\\doraemon\src\\report\\测试报告.html"
    lists = os.path.dirname(file_path)
    file_new = os.path.split(file_path)[-1]
    send_mail(file_new)