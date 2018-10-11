#coding:utf-8
import os
import os.path

#UI文件所在的路径

dir = './'

#列出目录下所有的文件
def listUiFile():
    list = []
    files = os.listdir(dir)
    for filename in files:
        # print(dir + os.sep + filename)
        if os.path.splitext(filename)[1] == '.ui':
            list.append(filename)
    # print(list)
    return list
def transPyFile(filename):
    # print(os.path.splitext(filename)[0] + '.py')
    return os.path.splitext(filename)[0] + '.py'

def runMain():
    list = listUiFile()
    for uifile in list:
        pyfile = transPyFile(uifile)
        cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)
        print(cmd)
        os.system(cmd)
if __name__ == "__main__":
    runMain()