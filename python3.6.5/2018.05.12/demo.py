#!/usr/bin/env python3
#coding:utf-8
# class Student(object):
# 	def get_score(self):
# 		return self._score
# 	def set_score(self,score):
# 		if not isinstance(score,int):
# 			raise ValueError('score must be an integer!')
# 		if score < 0 or score > 100:
# 			raise ValueError('score must between 0 ~ 100!')
# 		self._score = score
# s = Student()
# s.set_score(666)

import sqlite3
query = '''
CREATE TABLE TEST
(
	a VARCHAR(20),
	b VARCHAR(20),
	c REAL,
	d INTEGER
	);
	'''
con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()
data = [('atlanta','Georgia',1.25,6),
('TASDFA','Florida',2.6,3),
('sdfdf','hubei',1.5,3)]
stmt = 'INSERT INTO TEST VALUES(?,?,?,?)'
con.executemany(stmt,data)
con.commit()
cursor = con.execute('select * from TEST')
rows = cursor.fetchall()
print(rows)
print(cursor.description)