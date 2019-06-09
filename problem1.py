#!usr/bin/python3
import datetime
now=datetime.datetime.now()
name=input("  Enter Your Name=>")
age=int(input("\n  Enter Your Age=>"))
n=(95-age)
year=int(now.year)+n
print("hii {} year when you are 95 year old:-> {} ".format(name,year))
