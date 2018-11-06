#coding:utf-8
import os
import os.path

#UI文件所在的路径
# class Student(object):
	# def __init__(self,id,school):
		# self.id = id 
		# self.school = school
	# def readID(self):
		# print("ID : %s" %self.id)
	# def readSchool(self):
		# print("School : %s" %self.school)
# class Person(object):
	# def __init__(self,name,age,sex):
		# self.name = name
		# self.age = age
		# self.sex = sex
	# def talk(self):
		# print("Person")
		# print("name : %s\nage : %s\nsex : %s\nI can speaking!"%(self.name,self.age,self.sex))

# class Chinese(Person,Student):
	# def __init__(self,name,age,sex,language,id,school):
		# super(Person,self).__init__(name,age,sex)
		# Person.__init__(self,name,age,sex)
		# Student.__init__(self,id,school)
		# self.language =language
	# def walk(self):
		# print("我是中国人！")
	# def talk(self):
		# print("我被重构了")
class SchoolMember(object):
	member = 0
	listMember = []
	# print("member") #只调用一次
	def __init__(self,name,age):
		self.name = name
		self.age = age
		self.calcMember()
	def addMember(self):
		SchoolMember.member += 1
		self.printMember()
	def printMember(self):
		print("-----------------------\n总人数:%s"% SchoolMember.member)
		print("新增人员信息\n姓名:%s\n年龄:%s\n-----------------------"%(self.name,self.age))
	def calcMember(self):
		if self.name not in SchoolMember.listMember:
			SchoolMember.listMember.append(self.name)
			self.addMember()
	def tell(self):
		for k,v in self.__dict__.items():
			print(k,v)
			

class Student(SchoolMember):
	def __init__(self,name,age,grade,subject,course):
		SchoolMember.__init__(self,name,age)
		# super(SchoolMember,self).__init__(name,age)
		self.grade = grade
		self.subject = subject
		self.course = course
class Teacher(SchoolMember):
	def __init__(self,name,age,position,salary):
		SchoolMember.__init__(self,name,age)
		self.position = position
		self.salary = salary
	
	


		
if __name__ == "__main__":
	# fbl = Chinese("范炳林",26,"M","Chinese",421126,"蕲春一中")
	# fbl.talk()
	# fbl.walk()
	# fbl.readID()
	# fbl.readSchool()
	s1 = Student("范炳林",26,12,68,"python")
	s1.tell()
	
	t1 = Teacher("秦美琳",23,"主任",15000)
	t2 = Teacher("秦美琳",23,"主任",15000)
	t1.tell()