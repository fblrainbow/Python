#!/usr/bin/env python3
#coding=utf-8
from email.mime.text import MIMEText
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart


msg = MIMEMultipart()
# from_addr = input('From:')
# password = input('Password:')
# to_addr = input('To:')
# smtp_server = input('SMTP server:')
from_addr = '18271676080@163.com'
password = 'FBLATPX4869'
to_addr = '846058904@qq.com'
smtp_server = 'smtp.163.com'

msg['From'] = from_addr
msg['To'] = to_addr
msg['Author'] = 'fanbinglin'
subject = u'Python SMTP'
msg['Subject'] = Header(subject)
msg.attach(MIMEText('这是python3脚本邮件'))
att1 = MIMEText(open(r'K:\vip\001.jpg','rb').read(),'base64','utf-8')
att1 = MIMEText(open(r'H:\百度云\职业生涯\简历材料\51Job\Python开发工程师-2年.html','rb').read(),'html','utf-8')

att1['Content-Type']='application/octet-stream'
# att1['Content-Disposition']='attachment;filename="Python开发工程师-2年.html"'
att1['Content-Disposition']='attachment;filename="Python开发工程师-2年.html"'

msg.attach(att1)



server = smtplib.SMTP_SSL(smtp_server)
server.set_debuglevel(4)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()