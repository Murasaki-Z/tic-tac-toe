def draw(board=['__', '__', '__','__', '__', '__','__', '__', '__']):
	board_str = ''
	for index, i in enumerate(board):
		board_str = board_str + (('| {i} ').format(i=i))
		if (index+1) % 3 == 0:
			print('  \t' +board_str+'|')
			print('  \t-------------')
			board_str = ''
