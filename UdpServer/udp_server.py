#!/usr/bin/env python  
# -*- coding:UTF-8 -*-  

import socket 

bind_ip = "127.0.0.1"  
bind_port = 999
  
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
server.bind((bind_ip, bind_port))

while True:  
    print 'wating for message...'  
    data, addr = server.recvfrom(4096)  
    server.sendto('ack!', addr)  
    print  addr 
    print  data 
  
server.close()  