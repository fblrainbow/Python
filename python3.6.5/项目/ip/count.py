import sys


def readFile(fileName):
	with open(fileName,"r") as f:
		content = f.read()
		f.close()
		return content
def saveFile(fileName,content):
	with open(fileName,"w") as f:
		f.write(content)
		f.close()

if __name__ == "__main__":
	content = readFile("IP.txt")
	ipList = [line.split("\t")[0][3:] for line in content.split("\n") if line != ""]
	print(len(ipList))
	ipListUnique = list(set(ipList))
	DictIpCount = {}
	for line in ipListUnique:
		DictIpCount[line] = 0
	for line in ipList:
		if line in ipListUnique:
			DictIpCount[line] = DictIpCount[line] + 1
	saveContent = ''
	for k,v in DictIpCount.items():
		saveContent = saveContent + str(k) + '\t Count:' + str(v) + '\n'
	print(saveContent)
	saveFile("IPContent.txt",saveContent)
	