#coding:utf-8

# 读取文件
def fileRead(filename):
	with open(filename,"r") as f:
		content = f.read()
		# print(content)
		return content
#保存文件
def fileSave(filename,content):
	with open(filename,"w") as f:
		f.write(content)
		f.close()

if __name__ == "__main__":
	content = fileRead("1111.txt")
	listDate_Telephone = []
	listDate = []
	listTelephone = []
	listTelephoneTimes = {}
	listContent = [x for x in content.split("\n") if x != ""]
	for line in listContent:
		listline = line.split('|')
		listDate.append(listline[3])
		listTelephone.append(listline[0])
		listDate_Telephone.append (listline[3] + '_' + listline[0])
	listDate_Telephone = list(set(listDate_Telephone))
	listDate = list(set(listDate))
	listTelephone = list(set(listTelephone))
	print("len(listTelephone) = %s\nlen(listDate) = %s\nlen(listDate_Telephone) = %s\nlen(listContent) = %s" %(len(listTelephone),len(listDate),len(listDate_Telephone),len(listContent)))
	for telephone in listTelephone:
		count = 0
		for line in listDate_Telephone:
			if line.find(telephone) != -1:
				count = count + 1
		listTelephoneTimes[telephone] = count
	listTimesOver3 = []
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
