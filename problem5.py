#/usr/bin/python3

import time

name = input(" Please Enter Your Name : ")
hour = int(time.strftime('%H'))
print("current time in your system is :->"+time.strftime('%H'))
print(hour)

if hour>=0 and hour<=12:
	print("hiii.. {} very Good Morning".format(name))
elif hour>=12 and hour<=5:
	print("hiii.. {} very Good Afternoon".format(name))
elif hour>5 and hour<=7:
	print("hiii.. {} very Good Evening",format(name))
else: 
	print("hiii.. {} very Good Night",format(name))


