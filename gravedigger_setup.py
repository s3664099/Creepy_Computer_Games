from random import randint

player = "*"
stone = "+"
hole = "O"
wall = ":"
skeleton = "X"
space = " "
player_position = (2,2)
skeleton_position = [(4,18),(3,18),(2,18)]

def create_board():

	board = [[0 for x in range(20)] for y in range(10)] 

	for x in range(10):
		for y in range(20):
			board[x][y] = space

	return populate_board(board)

def place_player(board):

	board[player_position[0]][player_position[1]] = player

def place_skeletions(board):

	for x in skeleton_position:
		board[x[0]][x[1]] = skeleton

def add_stones(board):

	for x in range(20):
		f=randint(1,8)
		g=randint(1,18)
		board[f][g] = stone	

def place_walls(board):

	for x in range(20):
		board[0][x] = wall
		board[9][x] = wall

	for x in range(10):
		board[x][0] = wall
		board[x][19] = wall

	#Sets the exit
	board[8][19] = " "

def populate_board(board):

	place_walls(board)
	add_stones(board)
	place_player(board)
	place_skeletions(board)

	return board