#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administ
import sys
import socket
import time
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('localhost',9999))
    time.sleep(3)
    s.send('1')
    print(s.recv(1024))
    s.close()

