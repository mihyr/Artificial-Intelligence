QUEENS = 10

def gradient_search(board):
	#put yor code here
	def attack1(trial_board):
		#heuristic_board = [[0 for x in range(0,10)] for x in range(0,10)]
		board_row = len(trial_board)
		board_col = len(trial_board[0])

		attack_counter = 0
		attack_counter_line = 0
		attack_counter_line_half = 0
		attack_counter_diagonal = 0
		attack_counter_diagonal_half = 0
		for current_row in range(board_row):
			#print(trial_board[current_row])
			for current_col in range(board_col):
				
				
				if trial_board[current_row][current_col] ==1:
					#print(trial_board[current_row])
					
					#line attack counter
					for element in range(board_row):
						if element !=current_col and trial_board[current_row][element] ==1:
							attack_counter_line +=1
							#print(attack_counter_line)
							#print(trial_board[current_row])
							#print(trial_board[current_col][current_row])

					attack_counter_line_half = attack_counter_line/2

					row = max(current_row-current_col,0)
					col = max(current_col-current_row,0)

					for i in range(min((len(trial_board), len(trial_board[0]))) - max((row, col))):

						if (row+i) != current_row and (col + i) != current_col and trial_board[row+i][col+i] ==1:
							attack_counter_diagonal +=1
							#print(attack_counter_diagonal_half)
					attack_counter_diagonal_half = attack_counter_diagonal/2

		attack_counter = attack_counter_line_half + attack_counter_diagonal_half
		#print(attack_counter,attack_counter_line_half,attack_counter_diagonal_half )

		return attack_counter
		
	def queen_locations(board):
		locations = []
		for current_row in range(board_row):
			for current_col in range(len(board[current_row])):
				if board[current_col][current_row] != 0:
					locations.append((current_col,current_row))
		return locations

	def attack(locations):
		attack_counter = 0
		attack_counter_line = 0
		attack_counter_diagonal = 0
		trial_board = len(locations)
		unit = 1
		for current_row in range(trial_board):
			for current_col in range(current_row+1, trial_board):
				if locations[current_row][0] == locations[current_col][0]: 
					attack_counter_line += 1

		for current_row in range(trial_board):
			for current_col in range(current_row+unit, trial_board):
				a = locations[current_row][0]-locations[current_col][0]
				b = locations[current_row][1]-locations[current_col][1]
				if abs(a/b*unit)==1:
					attack_counter_diagonal += 1
				#if (row+i) != current_row and (col + i) != current_col and trial_board[row+i][col+i] ==1:
				#	attack_counter_diagonal +=1
		attack_counter = attack_counter_line + attack_counter_diagonal
		return attack_counter

	def heuristic(board, attacks):
		board_row = len(board)
		board_col = len(board[0])
		current_locations = [0]*board_row
		iteration = 200
		elem = 2
		for current_row in range(board_row):
			for current_col in range(board_col):

				new_locations = queen_locations(board)
				#print(new_locations)
				new_locations[current_row] = (current_col, current_row)
				heuristic_board.append((current_col, current_row))

				if iteration < attack(new_locations):
					pass
				elif  iteration > attack(new_locations):
					iteration = attack(new_locations)
					for element in range(len(new_locations)):
						#print(new_locations)
						current_locations[element] = new_locations[element]

		if iteration < attacks:
			return current_locations
		else:
			return queen_locations(board)

	#######################################
	board_row = len(board)
	board_col = len(board[0])
	count = 0
	
	#heuristic_board = [[-1 for x in range(0,10)] for x in range(0,10)]
	heuristic_board = []
	trigger = True
	#print(board)
	#print(heuristic_board)
	#print(attack(board))
	#print(board)
	#print(board[-4][3])

	while (trigger):
		locations = queen_locations(board)

		if attack(locations)<=0:
			trigger = False

		new_board = heuristic(board, attack(locations))
		attack_test = attack1(board)

		#update board
		for current_row in range(0,board_row):
			for current_col in range(0,board_col):
				if (current_row,current_col) in new_board:
					board[current_row][current_col]=1
				else:
					board[current_row][current_col]=0

		if new_board == locations:
			if (attack(locations)<=0):
				return True
			else:
				return False
		else:
			locations = queen_locations(board)

