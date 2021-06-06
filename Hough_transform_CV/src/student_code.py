"""
**Info**: This code takes images and returns slope and intercept of line (in fn detect_slope_intercept) as well as count the number of circles present in the image (in fn detect_circles)
"""
import common
import math #note, for this lab only, your are allowed to import math

def detect_slope_intercept(image):
	""" This function calculates m and b value of line in the image
	Args: 
		image: image of size 200x200
	Returns:
		line: updates the m and b value of the line
	"""
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"

	#Init Line instance
	line=common.Line()
	line.m=0
	line.b=0
	#line.theta = 0
	#line.r = 0

	#Get Image constants
	image_height = common.constants.HEIGHT
	image_width = common.constants.WIDTH

	#init voting array
	voting_array = [[0 for x in range(2001)] for x in range(2001)]
	#print(voting_array)

	#init m and b range arrays
	m_range = [x/100 for x in range(-1000,1001)]
	b_range = [x for x in range(-1000,1000)]
	
	#Loop through all pixels in image
	for y_index, y in enumerate(image):
		for x_index, x in enumerate(image[y_index]):

			#Check if pixel is black
			if image[y_index][x_index] ==0:

				#m method
				'''
				#Iterate through all possible m values and find b
				for m in m_range:
					#print(m)
					b = y_index - m*x_index

					if -1000< b <1000:
						b_convert = int(round(b))+1000
						m_convert = int(m*100)+1000
						#print(b_convert,m_convert)
						#print(m_convert)
						voting_array[b_convert][m_convert] +=1
				'''

				#b method

				#check if x>0, for x=0, line slope is undefined
				if x_index>0:

					#Iterate through all possible b values and find m
					for b in b_range:
						
						try:
							m = (y_index - b)/x_index
						except ZeroDivisionError:
							print(f'ZeroDivisionError, { y_index, x_index}')
							m = -10000
							
						if -10 <= m <=10:
							#print(m)

							#increment m and b index in voting array
							b_convert = int(round(b))+1000
							m_convert = int(m*100)+1000
							#print(b_convert,m_convert)
							#print(m_convert)
							voting_array[b_convert][m_convert] +=1

	#print(voting_array[1000][1500])

	#init max output with minimum
	max_output = -1
	max_x = None
	max_y = None

	#loop across all possible values in voting array
	for y_index, y in enumerate(voting_array):
		for x_index, x in enumerate(voting_array[y_index]):
			#print(x)
			#find max value in voting array

			if x >= max_output:
				max_output = x
				max_x = x_index
				max_y = y_index
				#print(x_index)


	op_array = []
	for y_index, y in enumerate(voting_array):
		for x_index, x in enumerate(voting_array[y_index]):
			if x == max_output:
				op_array.append(((x_index - 1000)/100,y_index - 1000))
	print(op_array)

	#update line's m and b value
	line.b = max_y - 1000
	line.m = (max_x - 1000)/100
	#print(f'm {line.m},b {line.b}')
	return line

def detect_circles(image):
	""" This function detects number of circles in an image
	Args: 
		image: Image of size 200x200
	Returns: number of circles detected
	"""
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"

	#Get Image constants
	image_height = common.constants.HEIGHT
	image_width = common.constants.WIDTH

	#init radius size = 30
	radius = 30

	#Init voting array of size 200x200
	voting_array = [[0 for x in range(image_height)] for x in range(image_width)]

	#print(voting_array)
	#print(len(voting_array))

	#init b array 0 to 200
	b_range = [x for x in range(image_height)]
	#print(len(b_range))

	#loop through all pixel in image
	for y_index, y in enumerate(image):
		for x_index, x in enumerate(image[y_index]):

			#check if pixel is black
			if image[y_index][x_index] ==0:

				#Loop for all values of b
				for b in b_range:

					#Check if radius^2 is greater than (y_index - b)^2, otherwise sqrt is not possible
					if (radius**2 >= (y_index - b)**2):
						#print((radius**2, -(y_index - b)**2))

						#find a, round it
						a = x_index - math.sqrt(radius**2 - (y_index - b)**2)
						#print(a)
						a_round = int(round(a))
						#print(a_round)

						if a >=0:
							#increment a,b index in voting array by 1
							voting_array[b][a_round] +=1

	#Init max output with minimum
	max_output = -1
	number_of_circles = 0
	output_array = []
	#print(voting_array)

	#Loop across all values in voting array
	for y_index, y in enumerate(voting_array):
		for x_index, x in enumerate(voting_array[y_index]):
			#print(output_array)

			#check for threshold (hard-coded value based on output array)
			if x >38:
				#Increment number of circles
				number_of_circles +=1
				#print(y_index,x_index,x)

			if x > max_output:
				max_output = x
				output_array.append(x)

	#print(output_array)
	return number_of_circles
				