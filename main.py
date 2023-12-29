from random import randint
import time

from util.draw import draw
from util.helper import indices, search

board = []

player = 'O'

def init_board():
	global board

	board = ['_', '_', '_','_', '_', '_','_', '_', '_']

def set_player(Player):

	if Player == 'O':
		Player = 'X'
	else:
		Player = 'O'

	return Player


def prompt(Player):

	print('\n\n')
	print(('\t Player {Player}').format(Player=Player))
	print('\t Enter Row and Column to draw \n')
	
	print('\n \t Or Select from the following options (Case Insensitive)')
	print('\n \t    1. Random Moves - R (Enter number to select number of games to play)')
	print('\n \t    2. Quit - Q')

	new_move = input()

	validate_move(new_move, Player)


def validate_move(new_move, Player):

	if new_move[0] in ('R', 'r'):
		if len(new_move) >= 2: # pass number of iterations
			random_move(Player, new_move[1:])
		else:
			random_move(Player)
		return None

	if new_move[0] in ('Q', 'q'):
		exit()

	print(int(new_move[0]), int(new_move[2]))

	if (0 <= int(new_move[0]) <= 3) and (0 <= int(new_move[2]) <= 3):
		update_board(new_move, Player)
	else:
		print("\t ---Invalid Move. Please Retry---")

def update_board(new_move, Player):

	global board


	index_y = (int(new_move[0])-1)*3

	index = index_y + (int(new_move[2])-1)

	
	board[index] = Player


def check_result():

	global board

	X_count, Y_count = board.count('X'), board.count('O')

	if  X_count >= 3 or Y_count >= 3:


		winner = search(board)

		if winner == 'X':
			print('\n\t---X Wins!---')
			return -1

		elif winner == 'O':
			print('\n\t---O Wins!---')
			return -1
		
		elif X_count + Y_count >= 9:
			print('\n\t---Tie!---')
			return -1

def random_move(Player, iteration = 1):

	global board

	index = 100

	while(index == 100 or (index < len(board) and board[index] in ('X', 'O'))):

		
		
		rand_move = [randint(1, 3), 0, randint(1, 3)]

		index_y = (int(rand_move[0])-1)*3

		index = index_y + (int(rand_move[2])-1)

		# print(rand_move[0], rand_move[2])


	update_board((rand_move), Player)

	draw(board)

	if check_result() == -1:

		print(('\t---{iteration} Games left---').format(iteration=int(iteration)-1))
		time.sleep(5)
		init_board()
		
		if iteration == 1:
			exit()
		else:
			iteration = int(iteration) - 1

	print(Player)
	Player = set_player(Player)

	time.sleep(1)

	random_move(Player, iteration)


init_board()
while(True):
	

	player = set_player(player)

	prompt(player)

	draw(board)

	if check_result() == -1:
		exit()

# To DOs
# board_state - init all then append vals to this - Done
# UI
# Validation and Result check. Option to enable random player(R) or Quit(Q)- Done 
# type "checks"
# auto player - random valid moves
# data capture and storage.
# unsupervised? - (C)