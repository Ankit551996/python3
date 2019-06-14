#/usr/bin/python2

import socket
recv_ip="127.0.0.1"
recv_port=4444 # 0-1024 -- you can check free udp port netstat -nulp

# creating udp socket
#     ip type v4 , v6 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# sending data to target
while(1):
	msg = raw_input("enter your msg")
	s.sendto(msg,(recv_ip,recv_port))
	print(s.recvfrom(10))
