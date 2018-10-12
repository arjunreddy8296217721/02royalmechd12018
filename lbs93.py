import os
from time import sleep

def mymail():
	return

def takesnap():
	os.system("fswebcam -F 4 img/tmp.jpg")
	return

for i in range (10):
	takesnap()
	mymail()
	sleep(5)

