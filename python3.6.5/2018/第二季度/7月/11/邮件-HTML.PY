#!/usr/bin/env python3
#coding=utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
# from email.mime.multipart import MIMEMultipart
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))

from_addr = '18271676080@163.com'
password = 'FBLATPX4869'
to_addr = '846058904@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('''<html><body><h1>Hello,</h1>
	<p>Send by <a href = "http://www.fanbinglin.com">我的阿里云服务器</a></p> 
	</body></html>
	''','html','utf-8')
# from_addr = input('From:')
# password = input('Password:')
# to_addr = input('To:')
# smtp_server = input('SMTP server:')
msg['From'] = _format_addr('Python爱好者<%s>' % from_addr)
msg['To'] = _format_addr('管理员<%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候....','utf-8').encode()


server = smtplib.SMTP_SSL(smtp_server)
server.set_debuglevel(2)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()