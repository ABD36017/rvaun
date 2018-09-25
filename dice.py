import random 
while True:
	a=input("press y to roll")
	if(a=="y"):
		r=random.randint(1,6)
		print(r)
	else:
		print("bye")
		break


dl212@soetcse:~/varunr$ python3 dice.py
press y to rolly
4
press y to rolly
1
press y to rolly
1
press y to rolly
3
press y to rolly
2
press y to rolly
3
press y to rolly
2
press y to rolly
5
press y to rollt
bye

