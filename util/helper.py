from random import randint

def indices(board):
    Xs = []
    Os = []
    for index, cell in enumerate(board):
        row = index // 3 
        col = index % 3  

        if cell == 'X':
            Xs.append((row + 1, col + 1)) 

        elif cell == 'O':
            Os.append((row + 1, col + 1))

    return Xs, Os

def search(board):


	for i in range(0, 6, 3):
		
		#row	

		if board[i] == board[i+1] == board[i+2]:
			return board[i]

	for i in range(0, 3):

		#col 

		if board[i] == board[i+3] == board[i+6]:
			return board[i]

	
	#leading diagonal

	if board[0] == board[4] == board[8]:
		return board[0]

	#trailing diagonal

	elif board[2] == board[4] == board[6]:
		return board[2]





# def search(Moves, original_list = None):

# 	if original_list is None:
# 		original_list = Moves

# 	node = Moves.pop(0)


# 	if (node[0], node[1] + 1) in Moves and (node[0], node[1] + 2) in Moves \
# 	and Moves[Moves.index((node[0], node[1] + 1))] is not None \
# 	and Moves[Moves.index((node[0], node[1] + 2))] is not None:
# 		return 1

# 	elif (node[0] + 1, node[1]) in Moves and (node[0] + 2, node[1]) in Moves \
# 	and Moves[Moves.index((node[0] + 1, node[1]))] is not None \
# 	and Moves[Moves.index((node[0] + 2, node[1]))] is not None:
# 		return 1

# 	elif (node[0] + 1, node[1] + 1) in Moves and (node[0] + 2, node[1] + 2) in Moves \
# 	and Moves[Moves.index((node[0] + 1, node[1] + 1))] is not None \
# 	and Moves[Moves.index((node[0] + 2, node[1] + 2))] is not None:
# 		return 1

# 	elif (node[0] + 1, node[1] - 1) in Moves and (node[0] + 2, node[1] - 2) in Moves \
# 	and Moves[Moves.index((node[0] + 1, node[1] - 1))] is not None \
# 	and Moves[Moves.index((node[0] + 2, node[1] - 2))] is not None:
# 		return 1

# 	else:
# 		try:
# 			search(Moves, original_list)
# 		except:
# 			return False
# 	# if len(Moves) < 2:
# 	#     return 0
# 	# else:
# 	#     return search(Moves)

















