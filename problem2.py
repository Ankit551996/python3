#!/usr/bin/python3
#import time
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
	print('Speak AnyThing...')
	audio = r.listen(source)
	
	try:
		text = r.recognize_google(audio)
		print('you said :{}'.format(text))
	except:
		print('source could not recognize your voice')

'''
from googlesearch import search
web=input(" Plz enter topic-->> ")
f=open("TopTenUrl.txt","w")
for i in search(web,tld='com',lang='en',num=20,start=0,stop=10,pause=2.0):
	f.write(i+"\n")

#f=open("hello.txt",'w')
#f.write(i+"\n")
'''

