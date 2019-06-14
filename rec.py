#/usr/bin/python2

import socket

recv_ip="127.0.0.1"
recv_port=4444 # 0-1024 -- you can check free udp port netstat -nulp

# creating udp socket
#     ip type v4 , v6 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# FITTING IP AND PORT with udp socket


s.bind((recv_ip,recv_port))

#reciving data from sender
while(1):
	data = s.recvfrom(100) #that is maxmimum data receive chracter
	print(data)

s.sendeto("ok got it",data[1])


