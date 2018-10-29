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
	totleTelephone = fileRead("Totle.txt")
	listTelephone = [x for x in fileRead("Telephone.txt").split("\n") if x != ""]
	dictTelephoneTimes = {}
	for count,line in enumerate(listTelephone):
		dictTelephoneTimes[line] = totleTelephone.count(line)
		if count % 1000 == 0:
			print("进度：%0.6s%%" %(count/len(listTelephone) * 100))
	printList = []
	for k,v in items(dictTelephoneTimes):
		if v >= 5:
			printList.append(k)
	printStr = '\n'.join(printList)
	fileSave("OutPut.txt",printStr)
