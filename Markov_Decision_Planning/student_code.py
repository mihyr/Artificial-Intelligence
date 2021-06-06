"""
**Info**: This code uses markov decision planning MDP to find optimal values and policies for drone based on input map, delivery_fee, battery_drop_cost, dronerepair_cost and discount
"""
import common

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	""" This function finds values and policies for each block in the map based on occupancy using MDP
	Args: 
		map: Input map of size 6x6, with 0 (empty), 1 (pizza), 2 (customer), 3 (rival)
		policies: empty array of size 6x6 to be updated by function with optimal policy
		values: empty array of size 6x6 to be updated by function with optimal values
		delivery_fee: reward of delivery
		battery_drop_cost: reward for each movement
		dronerepair_cost:reward for repair
		discount: gamma value

	Returns:
		value: value starting position
	"""
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	# 	
	
	#Define actions array (order is important when finding max, prior is considered if equal)
	actions = ['s','w','n','e','S','W','N','E']

	#Init start, goal, rival, empty states
	start_state = None
	goal_state = None
	rivals = []
	empty = []

	#find start state, goal state, rivals in the map
	for y_index, y in enumerate(map):
		for x_index, x in enumerate(map[y_index]):
			#print(x)

			#Start State
			if x == 1:
				start_state = (x_index,y_index)

			#Goal state
			if x ==2:
				goal_state = (x_index,y_index)
				#update value and policy Goal state
				values[y_index][x_index] = delivery_fee
				policies[y_index][x_index] = 0
			
			#Rivals
			if x ==3:
				rivals.append((x_index,y_index))
				#update value and policy for Rivals
				values[y_index][x_index] = -dronerepair_cost
				policies[y_index][x_index] = 0

			#Empty state
			else:
				empty.append((x_index,y_index))

	#print(f'start_state {start_state}')
	#print(f'goal_state {goal_state}')
	#print(f'rivals {rivals}')
	#print(f'empty {empty}')
	#print(f'battery_drop_cost {battery_drop_cost}')
	#print(f'dronerepair_cost {dronerepair_cost}')
	#print(f'delivery_fee {delivery_fee}')
	

	while_counter = 0
	#Init Iteration loop
	while True:
		while_counter+=1
		#Deep copy old values for reference
		old_values = deep_copy(values)
		
		#loop through all positions in map
		for y_index, y in enumerate(map):
			for x_index, x in enumerate(map[y_index]):
				
				#only check for non goal and rival states, goal and rival p and v are already assigned
				if x!= 2 and x!=3:
					#print(x)
					#Def state as index tuple
					state = (x_index,y_index)
					
					#init list of values for given state (it will have 8 values)
					state_value_list = []
					
					#Loop through all possible actions in given state
					for index, action in enumerate(actions):
						value = 0
						
						#print(action)

						#Calculate reward
						reward = reward_fn(action,battery_drop_cost)

						#Thruster ON
						if action =='N' or action =='S' or action =='E' or action =='W':
							
							#Add values and append to list
							value += 0.8*(reward + discount*v_star(probability_action(action,0), state, array = values))
							value += 0.1*(reward + discount*v_star(probability_action(action,-1), state,array = values))
							value += 0.1*(reward + discount*v_star(probability_action(action,1), state, array =values))
							state_value_list.append(value)
						
						#Thruster OFF
						elif action =='n' or action =='s' or action =='e' or action =='w':
							
							#Add values and append to list
							value += 0.7*(reward + discount*v_star(probability_action(action,0), state, array = values))
							value += 0.15*(reward + discount*v_star(probability_action(action,-1), state,array = values))
							value += 0.15*(reward + discount*v_star(probability_action(action,1), state, array =values))
							state_value_list.append(value)

					#Find max value and its index from value list (already priotized list)
					max_q = max(state_value_list)
					max_q_index = state_value_list.index(max_q)
					values[y_index][x_index] = max_q

					#Update policy
					policies[y_index][x_index] = action_translate(max_q_index)

		#Check for convergence
		count = 0
		for y_index in range(6):
			for x_index in range(6):			
				if abs(values[y_index][x_index] - old_values[y_index][x_index]) >0.01:
					count +=1
		#If converge reached, break
		if count == 0:
			#print(while_counter)
			return values[start_state[1]][start_state[0]]

#Helper Functions
def reward_fn(action,battery_drop_cost):
	if action == 'n' or action =='e' or action == 'w' or action =='s':
		return -battery_drop_cost
	if action == 'N' or action =='E' or action == 'W' or action =='S':
		return -2* battery_drop_cost

def deep_copy(board):
	new_board = [[0 for x in range(6)] for y in range(6)]
	for i in range(6):
		for j in range(6):
			new_board[i][j] = board[i][j]
	
	return new_board


def v_star(action,current_state,array):
	current_x =  current_state[0]
	current_y =  current_state[1]
	#print('val',action,current_state,array)
	if action =='s' or action == 'S':
		if current_y+1 >5:
			return array[current_y][current_x]
		else:
			#print(current_y,values[0][0])
			return array[current_y+1][current_x]

	if action =='w' or action == 'W':
		if current_x -1 <0:
			return array[current_y][current_x] 
		else:
			return array[current_y][current_x -1]

	if action =='n' or action == 'N':
		if current_y -1<0:
			return array[current_y][current_x] 
		else:
			return array[current_y -1][current_x]

	if action =='e' or action == 'E':
		if current_x+1>5:
			return array[current_y][current_x] 
		else:
			return array[current_y][current_x + 1]


def probability_action(action,direction):
	#direction 0 is fwd, -1 is left and 1 is right
	if action =='N' and direction == 0:
		return 'N'
	if action =='N' and direction == -1:
		return 'W'
	if action =='N' and direction == 1:
		return 'E'

	if action =='S' and direction == 0:
		return 'S'
	if action =='S' and direction == -1:
		return 'E'
	if action =='S' and direction == 1:
		return 'W'
	
	if action =='E' and direction == 0:
		return 'E'
	if action =='E' and direction == -1:
		return 'N'
	if action =='E' and direction == 1:
		return 'S'
	
	if action =='W' and direction == 0:
		return 'W'
	if action =='W' and direction == -1:
		return 'S'
	if action =='W' and direction == 1:
		return 'N'

	#without propulsion
	if action =='n' and direction == 0:
		return 'n'
	if action =='n' and direction == -1:
		return 'w'
	if action =='n' and direction == 1:
		return 'e'

	if action =='s' and direction == 0:
		return 's'
	if action =='s' and direction == -1:
		return 'e'
	if action =='s' and direction == 1:
		return 'w'
	
	if action =='e' and direction == 0:
		return 'e'
	if action =='e' and direction == -1:
		return 'n'
	if action =='e' and direction == 1:
		return 's'
	
	if action =='w' and direction == 0:
		return 'w'
	if action =='w' and direction == -1:
		return 's'
	if action =='w' and direction == 1:
		return 'n'


def action_translate(max_q_index):
	return max_q_index+1


def new_states(current_state):
	new_states_list = []
	current_x =  current_state[0]
	current_y =  current_state[1]
	if current_y-1 >=0: #N
		#print(1)
		new_states_list.append((current_x,current_y-1,'n'))
	if current_y-1 <0: #N
		#print(2)
		new_states_list.append((current_x,current_y,'nb'))
	if current_x+1 <=5: #E
		#print(3)
		new_states_list.append((current_x+1,current_y,'e'))
	if current_x+1 >5:
		#print(4)
		new_states_list.append((current_x,current_y,'eb'))
	if current_y+1 <=5: #S
		#print(5)
		new_states_list.append((current_x,current_y+1,'s'))
	if current_y+1 >5: #S
		#print(6)
		new_states_list.append((current_x,current_y,'sb'))
	if current_x-1 >=0: #W
		#print(7)
		new_states_list.append((current_x-1,current_y,'w'))
	if current_x-1 <0: #W
		#print(8)
		new_states_list.append((current_x,current_y,'wb'))
	
	return new_states_list
