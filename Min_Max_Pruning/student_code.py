"""
**Info**: This code takes an array of tictactoe (1 for X, 2 for Y and 0 for empty position), and returns prediction who will win (1 for X, 2 for Y and 0 for tie)
		  Prediction is made using min-max method, as well as alpha-beta pruning method
		  Asssumption: players play optimally
"""

import common

def minmax_tictactoe(board, turn):
	""" This Fn calls sub function min_max and maps its output to as desired for evaluation
	Args: 
		board [array]: an array of 9 elements, with value 1 for X, 2 for Y and 0 for empty position
		turn (int): 1 for X turn, 2 for O turn

	Returns: 
		constant (int): 1 for X, 2 for Y and 0 for tie
	"""
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

	#init counter which checks recursive fn calls
	minmax_tictactoe.counter =0

	#call sub fn
	output = min_max(board,turn)
	#print(minmax_tictactoe.counter)

	#if output is 1, return 1
	if output == 1:
		print("x won")
		#return 1
		return common.constants.X

	#if output is 0, return 0
	if output == 0:
		print("its a tie")
		#return 0
		return common.constants.NONE
	
	#if output is -1, return 2
	if output == -1:
		print("y won")
		#return 2 (convert to -1)
		return common.constants.O

	#if output is 3, game is pending
	if output == 3:
		print("game not over yet!")


	
def min_max(board,turn):
	""" Recursive function for min-max method
	Args: 
		board [array]: an array of 9 elements, with value 1 for X, 2 for Y and 0 for empty position
		turn (int): 1 for X turn, 2 for O turn

	Returns: 
		constant (int): 1 for X, 2 for Y and 0 for tie
	"""
	#check status of game
	game_status = common.game_status(board)

	#init empty positions var and list containing index of it for current board
	empty_positions = 0
	empty_positions_list = []
	#count number of time recursive function is called
	minmax_tictactoe.counter +=1

	#check game status, if completed or not
	if game_status == 1:
		#print("x won")
		#return 1
		return 1
		
	if game_status == 2:
		#print("y won")
		#return 2 (convert to -1)
		return -1

	if game_status == 0:
		#check if its a tie or not
		for index, i in enumerate(board):
			if i ==0:
				#find number of empty positions and add its index to list
				empty_positions +=1
				empty_positions_list.append(index)

		if empty_positions ==0:
			#print("its a tie")
			#return 0
			return 0
		else:				
			#print(empty_positions)
			#for x turn
			if turn== 1:
				value = -10000

				#populate child boards
				for i in empty_positions_list:
					#make copy of board add add x at empty position
					temp_board = board.copy()
					temp_board[i] =1
					#print(temp_board)

					#call recursive Fn with new board and turn for O
					temp_val = min_max(temp_board,2)
					if temp_val > value:
						value = temp_val
				return value
			
			#for O turn 
			if turn== 2:
				value = 10000

				#populate child boards
				for i in empty_positions_list:
					#make copy of board add add O at empty position
					temp_board = board.copy()
					temp_board[i] =2
					#print(temp_board)

					#call recursive Fn with new board and turn for X
					temp_val = min_max(temp_board,1)
					if temp_val < value:
						value = temp_val
				return value




def abprun_tictactoe(board, turn):
	""" This Fn calls sub function ab_min_max and maps its output to as desired for evaluation
	Args: 
		board [array]: an array of 9 elements, with value 1 for X, 2 for Y and 0 for empty position
		turn (int): 1 for X turn, 2 for O turn

	Returns: 
		constant (int): 1 for X, 2 for Y and 0 for tie
	"""
	#put your code here:
	#it must return common.constants.X(1), common.constants.O(2) or common.constants.NONE(0) for tie.
	#use the function common.game_status(board), to evaluate a board
	#it returns common.constants.X(1) if X wins, common.constants.O(2) if O wins or common.constants.NONE(0) if tie or game is not finished
	#the program will keep track of the number of boards evaluated
	#result = common.game_status(board);

	#init alpha and beta
	a = -10000
	b = 10000

	#init counter which checks recursive fn calls
	abprun_tictactoe.counter =0

	#call sub fn
	output = ab_min_max(board,turn,a,b)
	#print(abprun_tictactoe.counter)

	#if output is 1, return 1
	if output == 1:
		#print("x won")
		#return 1
		return common.constants.X

	#if output is 0, return 0
	if output == 0:
		#print("its a tie")
		#return 0
		return common.constants.NONE

	#if output is -1, return 2
	if output == -1:
		#print("y won")
		#return 2 (convert to -1)
		return common.constants.O

	#if output is 3, game is pending
	if output == 3:
		print("game not over yet!")


	
def ab_min_max(board,turn,a,b):
	""" Recursive function for alpha-beta pruning method
	Args: 
		board [array]: an array of 9 elements, with value 1 for X, 2 for Y and 0 for empty position
		turn (int): 1 for X turn, 2 for O turn
		a (int): Alpha value
		b (int): Beta value

	Returns: 
		constant (int): 1 for X, 2 for Y and 0 for tie
	"""
	#check status of game
	game_status = common.game_status(board)

	#init empty positions var and list containing index of it for current board
	empty_positions = 0
	empty_positions_list = []
	#count number of time recursive function is called
	abprun_tictactoe.counter +=1

	#check game status, if completed or not
	if game_status == 1:
		#print("x won")
		#return 1
		return 1
		
	if game_status == 2:
		#print("y won")
		#return 2 (convert to -1)
		return -1

	if game_status == 0:

		#check if its a tie or not
		for index, i in enumerate(board):
			if i ==0:
				#find number of empty positions and add its index to list
				empty_positions +=1
				empty_positions_list.append(index)

		if empty_positions ==0:
			#print("its a tie")
			#return 0
			return 0
		else:				
			#print(empty_positions)

			#for x turn
			if turn== 1:
				value = -10000

				#populate child boards
				for i in empty_positions_list:
					#make copy of board add add x at empty position
					temp_board = board.copy()
					temp_board[i] =1
					#print(temp_board)

					#call recursive Fn with new board and turn for O
					temp_val = ab_min_max(temp_board,2,a,b)

					#update a, value based on conditions below
					if temp_val > value:
						value = temp_val
					if value >= b:
						return value
					if value > a:
						a = value
				return value
			
			#for O turn 
			if turn== 2:
				value = 10000

				#populate child boards
				for i in empty_positions_list:
					#make copy of board add add O at empty position
					temp_board = board.copy()
					temp_board[i] =2
					#print(temp_board)

					#call recursive Fn with new board and turn for X
					temp_val = ab_min_max(temp_board,1,a,b)

					#update a, value based on conditions below
					if temp_val < value:
						value = temp_val
					if value <= a:
						return value
					if value < b:
						b = value
				return value
