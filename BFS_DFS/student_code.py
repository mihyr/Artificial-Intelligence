"""
**Info**: This code takes an array "map", and returns path using BFS and DFS algorithm
"""

from common import constants

def df_search(map):
	""" Function which uses DFS algorithm to find a path (5) betn start (2) and goal (3), by exploring empty space (0) in the map and avoiding walls (1)
		The function updates the input map nodes as it iterates (with (4) when explored and (5) when path is found)
	Args: 
		map: an array of ones and zeros where (1) represent wall and (0) represent free space

	Returns: 
		found (var): True/False, if path is found
	"""
	found = False;
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	#Declare init and current vars
	initial_x = None
	initial_y = None
	current_x = None
	current_y = None

	width = constants.MAP_WIDTH
	height = constants.MAP_HEIGHT

	#init maps for visited and parent
	visited = [[False for x in range(width)] for y in range(height)]
	parent = [[-1 for x in range(width)] for y in range(height)]

	#init empty frontier array
	Frontier = []
	Parent = []

	#Find start location and append to frontier array
	for y in range(constants.MAP_HEIGHT - 1):
		for x in range(constants.MAP_WIDTH - 1):
			if map[y][x] == 2:
				initial_x, initial_y = x, y
				Frontier.append([initial_y, initial_x])
				Parent.append([initial_y, initial_x])
				#print("initial location", initial_x, initial_y)

	
	
	while len(Frontier) !=0:
		#pop first node of frontier
		current_y ,current_x = Frontier[0]
		Frontier.pop(0)
		#print(width,height)

		#check if current node is goal
		if map[current_y][current_x] == 3:
			found = True
			Frontier = []
			#print('found')
			#print(parent)
			map[current_y][current_x] = 5
			#print(current_y,current_x)

			#trace back the path
			while parent[current_y][current_x] !=-1:
				#print(parent[current_y][current_x])
				current_y, current_x = parent[current_y][current_x]
				map[current_y][current_x] = 5
			break

		else:
			#mark node as visited
			map[current_y][current_x] = 4
			visited[current_y][current_x] =True

			#Parent.append((current_y,current_x))

			#expand to next
			order = 0
			#print(order)
			if 0<= current_x+1 <= width-1 and map[current_y][current_x+1] !=1 and  visited[current_y][current_x+1] ==False:
				Frontier.insert(order,[current_y, current_x+1])
				visited[current_y][current_x+1] =True
				parent[current_y][current_x+1] = [current_y, current_x]
				order +=1
				#print(order)
				#if map[current_y][current_x+1] !=3:
				#	map[current_y][current_x+1] =4

			if 0<= current_y+1 <= height-1 and map[current_y+1][current_x] !=1 and  visited[current_y+1][current_x]==False:
				Frontier.insert(order,[current_y+1, current_x])
				visited[current_y+1][current_x] = True
				parent[current_y+1][current_x] = [current_y, current_x]
				order +=1
				#print(order)
				#if map[current_y+1][current_x] !=3:
				#	map[current_y+1][current_x] = 4

			if 0<= current_x-1 <= width-1 and map[current_y][current_x-1] !=1 and  visited[current_y][current_x-1] ==False:
				Frontier.insert(order,[current_y, current_x-1])
				visited[current_y][current_x-1] =True
				parent[current_y][current_x-1] = [current_y, current_x]
				order +=1
				#print(order)
				#if map[current_y][current_x-1] !=3:
				#	map[current_y][current_x-1] =4

			if 0<= current_y-1 <= height-1 and map[current_y-1][current_x] !=1 and  visited[current_y-1][current_x]==False:
				Frontier.insert(order,[current_y-1, current_x])
				visited[current_y-1][current_x] = True
				parent[current_y-1][current_x] = [current_y, current_x]
				order +=1
				#print(order)
				#if map[current_y-1][current_x] !=3:
				#	map[current_y-1][current_x] = 4

			#print (Frontier)
	return found

def bf_search(map):
	""" Function which uses BFS algorithm to find a path (5) betn start (2) and goal (3), by exploring empty space (0) in the map and avoiding walls (1)
		The function updates the input map nodes as it iterates (with (4) when explored and (5) when path is found)
	Args: 
		map: an array of ones and zeros where (1) represent wall and (0) represent free space

	Returns: 
		found (var): True/False, if path is found
	"""
	found = False;
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	#Declare init and current vars
	initial_x = None
	initial_y = None
	current_x = None
	current_y = None

	width = constants.MAP_WIDTH
	height = constants.MAP_HEIGHT

	#init maps for visited and parent
	visited = [[False for x in range(width)] for y in range(height)]
	parent = [[-1 for x in range(width)] for y in range(height)]
	Frontier = []
	Parent = []

	#Find start location and append to frontier array
	for y in range(constants.MAP_HEIGHT - 1):
		for x in range(constants.MAP_WIDTH - 1):
			if map[y][x] == 2:
				initial_x, initial_y = x, y
				Frontier.append([initial_y, initial_x])
				Parent.append([initial_y, initial_x])
				#print("initial location", initial_x, initial_y)

	
	while len(Frontier) !=0:
		#pop first node of frontier
		current_y ,current_x = Frontier[0]
		Frontier.pop(0)
		#print(Frontier)
		#print(width,height)

		#check if current node is goal
		if map[current_y][current_x] == 3:
			found = True
			Frontier = []
			#print('found')
			#print(parent)
			map[current_y][current_x] = 5
			#print(current_y,current_x)

			#trace back the path
			while parent[current_y][current_x] !=-1:
				#print(parent[current_y][current_x])
				current_y, current_x = parent[current_y][current_x]
				map[current_y][current_x] = 5
			break

		else:
			#mark node as visited
			map[current_y][current_x] = 4
			visited[current_y][current_x] =True
			#Parent.append((current_y,current_x))

			#expand to next
	
			if 0<= current_x+1 <= width-1 and map[current_y][current_x+1] !=1 and  visited[current_y][current_x+1] ==False:
				Frontier.append([current_y, current_x+1])
				visited[current_y][current_x+1] =True
				parent[current_y][current_x+1] = [current_y, current_x]

			if 0<= current_y+1 <= height-1 and map[current_y+1][current_x] !=1 and  visited[current_y+1][current_x]==False:
				Frontier.append([current_y+1, current_x])
				visited[current_y+1][current_x] = True
				parent[current_y+1][current_x] = [current_y, current_x]

			if 0<= current_x-1 <= width-1 and map[current_y][current_x-1] !=1 and  visited[current_y][current_x-1] ==False:
				Frontier.append([current_y, current_x-1])
				visited[current_y][current_x-1] =True
				parent[current_y][current_x-1] = [current_y, current_x]

			if 0<= current_y-1 <= height-1 and map[current_y-1][current_x] !=1 and  visited[current_y-1][current_x]==False:
				Frontier.append([current_y-1, current_x])
				visited[current_y-1][current_x] = True
				parent[current_y-1][current_x] = [current_y, current_x]


	return found