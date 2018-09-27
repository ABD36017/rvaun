import random
count=0
while(count<=100):
		a=input("press y to roll")
		if(a=="y"):
			r=random.randint(1,6)
			print(r)
			count=count+r
			print("score is",count)
		if(count==100):
			print("you win")
			print ("your score is",count)
		elif(count==8):
		count=37
		elif(count==11):
		count=2
		elif(count==13):
		count=34
		elif(count==25):
		count=4
		elif(count==38):
		count=9
		elif(count==40):
		count=68
		elif(count==52):
		count=81
		elif(count==65):
		count=46
		elif(count==76):
		count=97
		elif(count==89):
		count=70
		elif(count==93):
		count=64
			break





			
	


