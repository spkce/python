#!/usr/bin/python

import socket

target_host = "127.0.0.1"
target_port = 999

ntp_package = {
    'LI':,
    'VN':
}

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("SEND MESSAGE", (target_host, target_port))

data, addr = client.recvfrom(4096)

print data
print addr