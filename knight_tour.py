import pyautogui as pg

#(763,200) : first cell,row 0	}							}
#(818,200) : second cell 		}=> delta x,y = 55 			}
#(763,255) : first cell row 1	}							} => only on a specific device (every device has its own height and width) 
#(964,148) : automove (if only one move possible) button	}
board = [[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0]]
count = 0

def print_board():
	for i in range(8):
		for j in range(8):
			print(board[i][j], end = ' ')
		print()

def auto_complete():
	global count
	for i in range(8):
		for j in range(8):
			if board[i][j] == count+1:
				pg.click(763+(55*j),200+(55*i))
	count += 1
	if count == 64:
		return True
	auto_complete()			


def get_possibilities(x,y):
	move_x = (2, 1, -1, -2, -2, -1, 1, 2)
	move_y = (1, 2, 2, 1, -1, -2, -2, -1)
	possibilities = []
	for i in range(8):
		if x+move_x[i] >= 0 and x+move_x[i] <= 7 and y+move_y[i]>= 0 and y+move_y[i] <= 7 and board[x+move_x[i]][y+move_y[i]] == 0:
			possibilities.append([x+move_x[i],y+move_y[i]])
	return possibilities

def solve():
	row = int(input("Start row: "))
	col = int(input("Start column: "))
	onclick_automove = input("click automove button? (y/n): ")
	if onclick_automove == "y":
		pg.click(964,148)
	board[row][col] = 1
	counter = 2
	for i in range(63):
		pos = get_possibilities(row, col)
		minimum = pos[0]
		for p in pos:
			if len(get_possibilities(p[0],p[1])) <= len(get_possibilities(minimum[0], minimum[1])):
				minimum = p
		row = minimum[0]
		col  = minimum[1]
		board[row][col] = counter
		counter += 1

solve()
print_board()
auto_complete()
