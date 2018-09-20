a=int(input("enter value of a" ))
if(a>=90):
	print("grade=A+")
elif(a>=80):
	print("grade=A")
elif(a>=70):	
	print("grade=B+")
elif(a>=60):
	print("grade=B")
elif(a>=40):
	print("grade=C")			
elif(a<40):
	print("fail")

dl212@soetcse:~/varunr$ python marks.py
enter value of a65
grade=B
dl212@soetcse:~/varunr$ python marks.py
enter value of a85
grade=A
dl212@soetcse:~/varunr$ python marks.py
enter value of a98
grade=A+
dl212@soetcse:~/varunr$ python marks.py
enter value of a35
fail
dl212@soetcse:~/varunr$ python marks.py
enter value of a77
grade=B+
dl212@soetcse:~/varunr$ python marks.py
enter value of a57
grade=C

