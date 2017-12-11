#!/usr/bin/python

import socket
import threading

#绑定ip：这里代表任何ip地址 
bind_ip = "0.0.0.0"
bind_port = 8888

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

# 最大连接数为5 
server.listen(5)

print "[*] Listening on %s:%d" % (bind_ip, bind_port)


def handle_client(client_socket):
    request = client_socket.recv(1024)
    #打印出客户端发送得到的内容  
    print "[*] Received: %s" % request

     #发送一个数据包 
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client,addr = server.accept()

    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    #挂起客户端线程，处理传人的数据  
    client_handler = threading.Thread(target=handle_client, args=(client,))  
    client_handler.start() 