#!/usr/bin/env python3
#coding:utf-8
# class Dict(dict):
# 	def __init__(self,**kw)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.
#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)

#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

#     def __setattr__(self, key, value):
#         self[key] = value

# if __name__=='__main__':
#     import doctest
#     doctest.testmod()
# import os
# print(os.name)
# # print(os.environ)
# # print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# # print(dir(os.system))
# os.path.join(r'D:/SVN/Python/trunk/python3.6.5/2018.5.15','qml')
# # os.mkdir(r'D:/SVN/Python/trunk/python3.6.5/2018.5.15/fbl/qml/asf')
# os.rmdir(r'D:/SVN/Python/trunk/python3.6.5/2018.5.15/fbl/qml')


# f = open('fbl.txt','r')
# tmp=f.read()
# t = open('t.txt','w+',encoding='bytes')
# t.close()
# # print(tmp)
# # t.write(tmp)
# import os
# from multiprocessing import Process
# def run_proc(name):
# 	print('Run child process %s (%s).'%(name,os.getpid()))
# if __name__=='__main__':
# 	print('Parent process %s.'%os.getpid())
# 	p = Process(target = run_proc,args = ('test',))
# 	print('Child process will start.')
# 	p.start()
# 	p.join()
# 	print('Child process end.')
# from multiprocessing import Pool
# import os,time,random
# def long_time_task(name):
# 	print('Run task %s (%s)'%(name,getpid()))
# 	start = time.time()
# 	time.sleep(random.random()*3)
# 	end = time.time()
# 	print('Task %s runs %0.2f seconds.'%(name,(end,start)))
# if __name__ == '__main__':
# 	print('Parent process %s.'%os.getpid())
# 	p = Pool(9)
# 	for i in range(9):
# 		p.apply_async(long_time_task,args=(i,))
# 	print('Waiting for all subprocesses done...')
# 	p.close()
# 	p.join()
# 	print('All subprocesses done.')
import subprocess
print('$nslookup www.fanbinglin.com')
r = subprocess.call(['nslookup','www.fanbinglin.com'])
print('Exit code:',r)