import random
while True:
	a=input("enter r to roll dice:")
	if (a =='r'):
		r=random.randint(1,6)
		print(r)
	else:
		print('try again')
		break
