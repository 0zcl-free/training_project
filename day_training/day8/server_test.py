#!/usr/bin/env python
# -*- coding:utf-8 -*-


import socket

ip_port = ('127.0.0.1',8888)
sk = socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    conn,address =  sk.accept()
    conn.sendall('欢迎致电 10086，请输入1xxx,0转人工服务.'.encode("utf_8"))
    Flag = True
    while Flag:
        data = conn.recv(1024)
        if data == 'exit':
            Flag = False
        elif data == '0':
            conn.sendall('通过可能会被录音.balabala一大推'.encode("utf-8"))
        else:
            conn.sendall('请重新输入.'.encode("utf-8"))
    conn.close()
