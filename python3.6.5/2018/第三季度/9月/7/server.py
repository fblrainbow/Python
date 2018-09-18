#!/usr/bin/env python
#coding=utf-8
#__author__ = 'Administrator'
# server.socket
import socket
import sys
if __name__ == '__main__':
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    print(host)
    port = 9999
    serversocket.bind((host,port))
    serversocket.listen(5)
    while True:
        connection,addr = serversocket._accept()
        print(connection ,addr)
        try:
            connection.settimeout(5)
            buf = connection.recv(1024)
            if buf == '1':
                connection.send('Welcome to server!')
            else:
                connection.send('Please go out!')
        except serversocket.timeout:
            print('Time out!')
        connection.close()