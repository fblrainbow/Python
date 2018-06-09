#!/usr/bin/env python3
#coding:utf-8
import time
import smtplib
from email.header import Header
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
import requests

mail_host = 'smtp.163.com'           #邮箱服务器名
mail_user = '18271676080@163.com'      #邮箱用户名
mail_pass = 'FBLATPX4869'            #登录密码（授权码）
sender = '18271676080@163.com'            #发送者
receivers = ['18271676080@163.com','204206705@qq.com','846058904@qq.com','qinmeilin25@163.com']    #收件人
# receivers = ['18271676080@qq.com','204206705@qq.com','846058904@qq.com']  

headers = {
"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
}

url = 'https://www.baidu.com/s?ie=utf8&oe=utf8&wd=ip%E6%9F%A5%E8%AF%A2&tn=98010089_dg&ch=1'
def getIpAdress(url):
    page = requests.get(url,headers = headers)
    page.encoding = 'UTF-8-SIG'
    txt = page.text
    flag1 = txt.find("我的ip地址")
    tmp = txt[flag1:flag1+40]
    flag2 = tmp.find("地址")
    flag3 = tmp.find(" ")
    ip = tmp[flag2+2:flag3]
    adress = tmp[flag3+4:tmp.find("市")+1]
    return ip,adress
    
localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
(ip,adress) = getIpAdress(url)
content = """
您的电脑已经开机
开机时间是:%s
网络IP:%s
位于:%s
"""%(localtime,ip,adress)

message = MIMEMultipart()
message['From'] = sender
message['To'] = '846058904@qq.com'
subject = u'开机提醒'
message['Subject'] = Header(subject)
message.attach(MIMEText(content))

try:
    print('Connecting...')
    smtpobj = smtplib.SMTP_SSL(mail_host) #连接服务器
    print("登录账户")
    smtpobj.login(mail_user,mail_pass)    #登录账户
    print("发送邮件")
    smtpobj.sendmail(sender,receivers,message.as_string())   #发送邮件
    print("""
        发送人:%s
        接收人:%s
        邮件内容:%s
        """%(sender,receivers,message.as_string()))
    smtpobj.quit()                        #退出登录
    print('邮件发送成功')
except smtplib.SMTPException :
    print('Error:无法发送邮件')
