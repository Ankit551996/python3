#!/usr/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
list1=[]
list2=[]
for i in adhoc:
	if i>5:
		list1.append(i)
for i in adhoc:
	if i<=2:
		list2.append(i)
		

print(list1)
print(list2) 
