#!/usr/bin/env python3
#coding:utf-8
import smtplib
from email.header import Header
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
import time
mail_host = 'smtp.qq.com'           #邮箱服务器名
mail_user = '846058904@qq.com'      #邮箱用户名
mail_pass = 'hrukwfbytyqubecg'            #登录密码（授权码）
sender = '846058904@qq.com'            #发送者
receivers = ['18271676080@163.com','204206705@qq.com']    #收件人

message = MIMEMultipart()
message['From'] = sender
message['To'] = '18271676080@163.com'
subject = 'Python SMTP'
message['Subject'] = Header(subject,'utf-8').encode()
message.attach(MIMEText('send with file...','plain','utf-8'))
att1 = MIMEText(open(r'K:\vip\001.jpg','rb').read(),'base64','utf-8')
att1['Content-Type']='application/octet-stream'
att1['Content-Disposition']='attachment;filename="001.jpg"'
message.attach(att1)
try:
    print('Connecting...')
    smtpobj = smtplib.SMTP_SSL(mail_host)
    smtpobj.login(mail_user,mail_pass)
    smtpobj.sendmail(sender,receivers,message.as_string())
    smtpobj.quit()
    print('邮件发送成功')
except smtplib.SMTPException :
    print('Error:无法发送邮件')
