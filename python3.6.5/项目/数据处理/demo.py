#coding:utf-8
import time
# 读取文件
def fileRead(filename):
	with open(filename,"r") as f:
		content = f.read()
		# print(content)
		return content
#保存文件
def fileSave(filename,content):
	with open(filename,"w") as f:
		startTime = time.time()
		print("开始写内容到%s文件中！--start:%s" % (filename,startTime))
		f.write(content)
		endTime = time.time()
		print("文件写入结束！---End:%s" % endTime)
		f.close()

if __name__ == "__main__":
	content = fileRead("139邮箱-通话时长查询aspire_14113.txt")
	listDate_Telephone = []
	listDate = []
	listTelephone = []
	listTelephoneTimes = {}
	print(1,time.time())
	listContent = [x for x in content.split("\n") if x != ""]
	print(2,time.time())
	for line in listContent:
		listline = line.split('|')
		listDate.append(listline[3])
		listTelephone.append(listline[0])
		listDate_Telephone.append (listline[3] + '_' + listline[0])
	listDate_Telephone = list(set(listDate_Telephone))
	listDate = list(set(listDate))
	listTelephone = list(set(listTelephone))
	print("len(listTelephone) = %s\nlen(listDate) = %s\nlen(listDate_Telephone) = %s\nlen(listContent) = %s" %(len(listTelephone),len(listDate),len(listDate_Telephone),len(listContent)))
	string = ""
	init = time.time()
	totle = len(listDate_Telephone)
	for k,v in enumerate(listDate_Telephone):
		string = string + v
		if k % 100000 == 0:
			print("拼接-进度%.5f%%" %(k / totle * 100))
	end = time.time()
	print("拼接字符串完成！",end - init)
	totle_1 = len(listTelephone)
	for k,telephone in enumerate(listTelephone):
		listTelephoneTimes[telephone] = string.count(telephone)
		if k % 100000 == 0:
			print("查找-进度%.5f%%" %(k / totle_1 * 100))
	listTimesOver3 = []
	e2nd = time.time()
	print(3,e2nd - end)
	# print(listTelephoneTimes)
	# print(listTimesOver2)
	for k,v in listTelephoneTimes.items():
		if v >= 3:
			listTimesOver3.append(k)
	stringUnion = ''
	for x in listTimesOver3:
		stringUnion = x + "\n" + stringUnion
	print(stringUnion)
	fileSave("Over3.txt",stringUnion)
