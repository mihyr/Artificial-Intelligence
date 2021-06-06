"""
**Info**: This code takes an array of sudoku and returns solution using backtracking as well as backtracking combined with forward tracking approach
"""
import common
#helpful, but not needed
class variables:
	counter=0

def sudoku_backtracking(sudoku):
	variables.counter = 0
	#print(sudoku)
	output = recursive_sudoku_backtracking(sudoku)
	if output ==1:
		#print(variables.counter)
		return variables.counter


def recursive_sudoku_backtracking(sudoku):
	variables.counter +=1
	#put your code here
	count=0
	width = len(sudoku)
	height = len(sudoku[0])
	empty_positions = 0
	empty_positions_list = []
	#Check if sudoku is solved
	#print(sudoku)
	for y_index, y in enumerate(sudoku):
		for x_index, x in enumerate(sudoku[y_index]):
			#print(x)
			count +=1
			if x==0:
				#find number of empty positions and add its index to list
				empty_positions +=1
				empty_positions_list.append([y_index,x_index])

	if empty_positions ==0:
		#print("No empty positions")
		#return true
		#print(sudoku)
		return 1
	else:
		#print(empty_positions_list)
		for positions in empty_positions_list:
			#print(positions[0],positions[1])
			for value in range(1,10):
				y = positions[0]
				x = positions[1]
				test = common.can_yx_be_z(sudoku,y,x,value)
				if test ==True:
					#test_sudoku = sudoku.copy()
					sudoku[y][x]= value
					test_backtracking = recursive_sudoku_backtracking(sudoku)
					if test_backtracking ==True:
						return True
					else:
						sudoku[y][x]= 0
			return False
	#print("empty_positions",empty_positions_list)
	return variables.counter

def sudoku_forwardchecking(sudoku):
	variables.counter = 0
	#put your code here
	#make a domain array
	width = len(sudoku)
	height = len(sudoku[0])

	#init a domain array which contains all possible values empty positions can take
	domainz = [[[] for x in range(height)] for y in range(width)]
	#print(sudoku)

	#Find empty positions and add all possible values to corresponding index in domain array
	for y_index, y in enumerate(sudoku):
		for x_index, x in enumerate(sudoku[y_index]):
			#print(x)
			if x==0:
				#find number of empty positions in sudoku and add all possible values list to domain array
				possible_values = [1,2,3,4,5,6,7,8,9]
				domainz[y_index][x_index] = possible_values
			else:
				#assign [-1] to filled positions to keep track as occupied
				domainz[y_index][x_index] = [-1]
	
	#find occupied positions and remove values from domain which doesnt satisfy constraint
	for y in range(9):
		for x in range(9):
			if sudoku[y][x] !=0:
				z= sudoku[y][x]
				for i in range(9):
					#x-line
					try:
						domainz[i][x].remove(z)
					except ValueError:
						pass
					#y-line
					try:
						domainz[y][i].remove(z)
					except ValueError:
						pass
					#box
					try:
						domainz[int(y/3)*3+int(i/3)][int(x/3)*3+i%3].remove(z)
					except ValueError:
						pass

	#Now Init domain is ready to iterate
	#print(domainz)

	#call recursive function with sudoku and domain input
	output = recursive_sudoku_forwardchecking(sudoku,domainz)
	if output ==1:
		#print(variables.counter)
		return variables.counter

def recursive_sudoku_forwardchecking(sudoku,domain):
	variables.counter +=1
	#print(variables.counter)
	#put your code here
	count=0
	width = len(sudoku)
	height = len(sudoku[0])
	empty_positions = 0
	empty_positions_list = []
	
	#print(sudoku)
	for y_index, y in enumerate(sudoku):
		for x_index, x in enumerate(sudoku[y_index]):
			#print(x)
			count +=1
			if x==0:
				#find number of empty positions and add its index to list
				empty_positions +=1
				empty_positions_list.append([y_index,x_index])

	#Check if sudoku is solved
	if empty_positions ==0:
		#print("No empty positions")
		return 1

	else:
		#iterate for list of empty positions
		for positions in empty_positions_list:
			y = positions[0]
			x = positions[1]

			#get values available in domain list
			for value in domain[y][x]:
				
				#test if value works for current sudoku
				test = common.can_yx_be_z(sudoku,y,x,value)

				if test ==True:
					#make a copy of domain
					domain_copy = deep_copy(domain)

					#update domain and sudoku
					sudoku[y][x]= value
					domain[y][x] = [-1]

					#remove variables from domain which no longer satisfy constraint after assigning value
					for i in range(9):
						
						#x-line
						try:
							domain[i][x].remove(value)
						except ValueError:
							pass
						#y-line
						try:
							domain[y][i].remove(value)
						except ValueError:
							pass
						#box
						try:
							domain[int(y/3)*3+int(i/3)][int(x/3)*3+i%3].remove(value)
						except ValueError:
							pass
					
					#Check if any unoccupied domain sub-list is empty after updating domain list
					if not_empty(domain)==0:
						
						test_backtracking = recursive_sudoku_forwardchecking(sudoku,domain)
						if test_backtracking ==True:
							return True
						else:
							#revert original sudoku and domain because test returned false
							sudoku[y][x]= 0
							domain = domain_copy
					else:
						#revert original sudoku and domain because some domain sub-list is empty
						sudoku[y][x]= 0
						domain = domain_copy
			return False			
			
	return variables.counter

def not_empty(board):
	empty_count = 0
	for i in range(9):
		for j in range(9):
			#if domain is empty, update counter
			if len(board[i][j])==0:
				empty_count+=1
	return  empty_count

def deep_copy(board):
    new_board = [[[] for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            for k in range(len(board[i][j])):
                new_board[i][j].append(board[i][j][k])
    return new_board
				