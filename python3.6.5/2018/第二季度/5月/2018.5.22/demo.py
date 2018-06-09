
#!/usr/bin/env python3
#coding:utf-8

# from urllib import request
# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
# 	data = f.read()
# 	data = data.decode()
# 	print(data)
# 	for k,v in f.getheaders():
# 		print('%s:%s'%(k,v))
# 	print('Status:',f.status,f.reason)
from tkinter import *

class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.helloLabel = Label(self,text = 'Hello,world!')
		self.helloLabel.pack()
		self.quitButton = Button(self,text = 'Quit',command = self.quit)
		self.quitButton.pack()
app = Application()
app.master.title('Hello World')
app.mainloop()