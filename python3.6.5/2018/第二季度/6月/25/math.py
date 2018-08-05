#!/usr/bin/env python3
#conding:utf-8
'''
abcd * 9 = dcba

'''
for a in range(1,10):
	for b in range(0,10):
		for c in range(0,10):
			for d in range(1,10):
				if ( 9000 * a + 900 * b + 90 * c + 9 * d == 1000 * d + 100 * c + 10 * b + 1 * a):
					print('abcd = %d%d%d%d' %(a,b,c,d))