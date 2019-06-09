#!usr/bin/python3
import os
import crypt
uname=input("Enter User Name")
upass= "hello"+uname

list1=[0,1,2,3,4,5,6,7,8,9]

flag=1
for i in uname:
	if i in str(list1):
		flag=0

if flag==0:
	print("!!!username does not contain [0-9] number ")
else :
	pass_ucrypt=crypt.crypt(upass,"123")
	os.system("useradd -m -p"+pass_ucrypt+" "+uname)
	print("User and passwd is created sucessfully!!!\n")
	print("username = >"+uname)
	print("passwd   = >"+upass)			
