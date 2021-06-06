"""
**Info**: This code takes an array "map", and returns shortest path using A* algorithm
"""
import common
from common import constants
def astar_search(map):
	""" Function which uses A* algorithm to find a path (5) betn start (2) and goal (3), by exploring empty space (0) in the map and avoiding walls (1)
		The function updates the input map nodes as it iterates (with (4) when explored and (5) when path is found.
			- Fn uses f(n)=g(n)+h(n), where g is the distance from start to node n and h is the estimated distance from node n to goal
			- Here h is calculated using Manhatten distance formula, h is always less than actual distance
	Args: 
		map: an array of ones and zeros where (1) represent wall and (0) represent free space

	Returns: 
		found (var): True/False, if path is found
	"""
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1

	#Declare init and current vars
	initial_x = None
	initial_y = None
	final_x = 0
	final_y = 0
	current_x = None
	current_y = None
	increment_dist =1
	width = constants.MAP_WIDTH
	height = constants.MAP_HEIGHT
	#print(width)
	
	#init maps for visited and parent
	visited = [[False for x in range(width)] for y in range(height)]
	parent = [[-1 for x in range(width)] for y in range(height)]

	#f(n)=g(n)+h(n),
	f = [[0 for x in range(width)] for y in range(height)]
	g = [[0 for x in range(width)] for y in range(height)]
	h = [[0 for x in range(width)] for y in range(height)]
	#print(g)
	Frontier = []
	Parent = []
	

	#Find start location and wnd location
	for y in range(0,constants.MAP_HEIGHT):
		for x in range(0,constants.MAP_WIDTH):
			if (map[y][x] == 2):
				initial_x, initial_y = x, y
				
				#append location to frontier and parent array
				Frontier.append([initial_y, initial_x])
				Parent.append([initial_y, initial_x])
				#print("initial location", initial_x, initial_y)
				#init g and h
				
				#h[initial_y][initial_x] = 0
				#mark init location as 4
				map[initial_y][initial_x] = 4
				
	for y in range(0,constants.MAP_HEIGHT):
		for x in range(0,constants.MAP_WIDTH):
			if map[y][x] == 3:
				final_y, final_x = y, x
				#init g and h
				#g[initial_y][initial_x] = 0
				h[initial_y][initial_x] = abs(final_y - initial_y) + abs(final_x - initial_x)

	#eval f(n)=g(n)+h(n)
	#print(initial_x,initial_y)
	
	#print(g[initial_y][initial_x])
	g[initial_y][initial_x] = 0
	f[initial_y][initial_x] = g[initial_y][initial_x] + h[initial_y][initial_x]
	
	while len(Frontier) !=0:

		#print(Frontier)

		#pop element from frontier who has least f(n)
		if len(Frontier) <= 1:
			current_y, current_x = Frontier.pop(0)
			#print(Frontier)
		else:
			#find min h(n) for n elements in frontier and pop it
			min_h = 500000
			min_x = None
			min_y = None
			for i in range(len(Frontier)):
				x1 = Frontier[i][1]
				y1 = Frontier[i][0]
				#print(y1,x1,"cost",f[y1][x1] )

				#if cost of two frontier is equal, open whose x is smaller, if that is also same, open whose y is smaller
				if f[y1][x1] == min_h:
					if x1 == min_x:
						if y1 <min_y:
							min_h = f[y1][x1]
							min_y = y1
							min_x = x1
							index = i
						#else:
						#	print('hello')

					elif x1<min_x:
						min_h = f[y1][x1]
						min_y = y1
						min_x = x1
						index = i
					#else:
					#		print('hello')
					
				elif f[y1][x1]<min_h:
					min_h = f[y1][x1]
					min_y = y1
					min_x = x1
					index = i
				
				#else:
				#	print('hello')

			#print(Frontier)
			current_y, current_x = Frontier.pop(index)
			#print("current",current_y,current_x)

		
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
			#expand to next
			order = 0
			if 0<= current_x+1 <= width-1 and map[current_y][current_x+1] !=1 and  visited[current_y][current_x+1] ==False:
				Frontier.insert(order,[current_y, current_x+1])
				#visited[current_y][current_x+1] =True
				parent[current_y][current_x+1] = [current_y, current_x]
				order +=1
				h[current_y][current_x+1] = abs(final_y - current_y) + abs(final_x - (current_x+1))
				g[current_y][current_x+1] = g[current_y][current_x] + increment_dist
				f[current_y][current_x+1] = g[current_y][current_x+1] + h[current_y][current_x+1]

			if 0<= current_y+1 <= height-1 and map[current_y+1][current_x] !=1 and  visited[current_y+1][current_x] ==False:
				Frontier.insert(order,[current_y+1, current_x])
				#visited[current_y+1][current_x] = True
				parent[current_y+1][current_x] = [current_y, current_x]
				order +=1
				h[current_y+1][current_x] = abs(final_y - (current_y+1)) + abs(final_x - current_x)
				g[current_y+1][current_x] = g[current_y][current_x] + increment_dist
				f[current_y+1][current_x] = g[current_y+1][current_x] + h[current_y+1][current_x]

			if 0<= current_x-1 <= width-1 and map[current_y][current_x-1] !=1 and   visited[current_y][current_x-1]==False :
				Frontier.insert(order,[current_y, current_x-1])
				#visited[current_y][current_x-1] =True
				parent[current_y][current_x-1] = [current_y, current_x]
				order +=1
				h[current_y][current_x-1] = abs(final_y - current_y) + abs(final_x - (current_x-1))
				g[current_y][current_x-1] = g[current_y][current_x] + increment_dist
				f[current_y][current_x-1] = g[current_y][current_x-1] + h[current_y][current_x-1]

			if 0<= current_y-1 <= height-1 and map[current_y-1][current_x] !=1 and  visited[current_y-1][current_x]==False:
				Frontier.insert(order,[current_y-1, current_x])
				#visited[current_y-1][current_x] = True
				parent[current_y-1][current_x] = [current_y, current_x]
				order +=1
				h[current_y-1][current_x] = abs(final_y - (current_y-1)) + abs(final_x - current_x)
				g[current_y-1][current_x] = g[current_y][current_x] + increment_dist
				f[current_y-1][current_x] = g[current_y-1][current_x] + h[current_y-1][current_x]
	#print(map)
	#print(found)
	return found

