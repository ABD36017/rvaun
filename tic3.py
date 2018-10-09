a=['1','2','3','4','5','6','7','8','9']
def player_Board():
	print('|',a[0],'|',a[1],'|',a[2],'|')
	print("------------")
	print('|',a[3],'|',a[4],'|',a[5],'|')
	print("------------")
	print('|',a[6],'|',a[7],'|',a[8],'|')
player_Board()

playerOneturn = True
while True:
	player_Board()
	p=input("choose an available place : ")

	if(p in a):
		if(a[int(p)-1]=='X' or a[int(p)-1]=='O'):
			print("place taken,choose another place...")
			continue
		else:
			if playerOneturn:
				print("player 1 >>")
				a[int(p)-1] = 'X'
				playerOneturn = not playerOneturn
			else:
				print("player 2 >>")
				a[int(p)-1] = 'O'
				playerOneturn = not playerOneturn
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
					print("Game Over")
					exit()
			for i in range(3):
				if(a[i]==a[i+3] and a[i]==a[i+6]):
					print("Game Over...")
					exit()
				if(a[0]==a[4] and a[0]==a[8]):
					print("Game Over....")
					exit()
				if(a[2]==a[4] and a[2]==a[6]):
					print("Game Over....")
					exit()

				
	else:
		print("you have entered an invalid position")
		continue


dl212@soetcse:~/varunr$ python3 tic3.py
| 1 | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| 7 | 8 | 9 |
| 1 | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| 7 | 8 | 9 |
choose an available place : 7
player 1 >>
| 1 | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| X | 8 | 9 |
choose an available place : 3
player 2 >>
| 1 | 2 | O |
------------
| 4 | 5 | 6 |
------------
| X | 8 | 9 |
choose an available place : 9
player 1 >>
| 1 | 2 | O |
------------
| 4 | 5 | 6 |
------------
| X | 8 | X |
choose an available place : 5
player 2 >>
| 1 | 2 | O |
------------
| 4 | O | 6 |
------------
| X | 8 | X |
choose an available place : 8
player 1 >>
Game Over
dl212@soetcse:~/varunr$ python3 tic3.py
| 1 | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| 7 | 8 | 9 |
| 1 | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| 7 | 8 | 9 |
choose an available place : 1
player 1 >>
| X | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| 7 | 8 | 9 |
choose an available place : 6
player 2 >>
| X | 2 | 3 |
------------
| 4 | 5 | O |
------------
| 7 | 8 | 9 |
choose an available place : 7
player 1 >>
| X | 2 | 3 |
------------
| 4 | 5 | O |
------------
| X | 8 | 9 |
choose an available place : 3
player 2 >>
| X | 2 | O |
------------
| 4 | 5 | O |
------------
| X | 8 | 9 |
choose an available place : 4
player 1 >>
Game Over...
dl212@soetcse:~/varunr$ python3 tic3.py
| 1 | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| 7 | 8 | 9 |
| 1 | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| 7 | 8 | 9 |
choose an available place : 9
player 1 >>
| 1 | 2 | 3 |
------------
| 4 | 5 | 6 |
------------
| 7 | 8 | X |
choose an available place : 5
player 2 >>
| 1 | 2 | 3 |
------------
| 4 | O | 6 |
------------
| 7 | 8 | X |
choose an available place : 4
player 1 >>
| 1 | 2 | 3 |
------------
| X | O | 6 |
------------
| 7 | 8 | X |
choose an available place : 7
player 2 >>
| 1 | 2 | 3 |
------------
| X | O | 6 |
------------
| O | 8 | X |
choose an available place : 1
player 1 >>
| X | 2 | 3 |
------------
| X | O | 6 |
------------
| O | 8 | X |
choose an available place : 3
player 2 >>
Game Over....

