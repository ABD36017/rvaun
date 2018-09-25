def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mult(a,b):
	return a*b
def divide(a,b):
	return a/b

i=int(input("Enter value of a:"))
j=int(input("Enter value of b:"))
o=input("What do you want to do? +,-,*,/:")

if(o=='+'):
	res=add(i,j)
elif(o=='-'):
	res=sub(i,J)
elif(o=='*'):
	res=mult(i,j)
elif(o=='/'):
	res=divide(i,j)

print(res)


dl212@soetcse:~/varunr$ python3 cal.py
Enter value of a:30
Enter value of b:20
What do you want to do? +,-,*,/:+
50
dl212@soetcse:~/varunr$ python3 cal.py
Enter value of a:15
Enter value of b:16
What do you want to do? +,-,*,/:*
240
dl212@soetcse:~/varunr$ python3 cal.py
Enter value of a:30
Enter value of b:60
What do you want to do? +,-,*,/:/
0.5

