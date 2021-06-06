"""
**Info**: This code takes training and testing dataset for single and multi-classifier perceptron.
"""
import common

def part_one_classifier(data_train, data_test):
	""" Binary classifier perceptron
	Args: 
		data_train: training data
		data_test: testing data
	"""
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1

	#Import constants
	feature_size = common.constants.NUM_FEATURES
	training_size = common.constants.TRAINING_SIZE
	testing_size = common.constants.TEST_SIZE

	#Init all weights to zero
	weights = [0,0,0]
	#print(data_train)
	count = 0
	trigger = True
	
	#training
	while trigger:
		error_counter = 0

		#Iterate through all training data
		for i in range(training_size):

			#add bias 1 as 3rd element
			bias_feature = [data_train[i][0],data_train[i][1],1]
			label = data_train[i][2]
			#print(label, data_train[i])
			count +=1

			#prediction
			w_sum = weighted_sum(bias_feature,weights)
			output = activation(w_sum)
			
			#evaluation
			if output != label:
				#print(output,label)

				#update weights and error counter
				error_counter+=1
				error = label - output

				for i in range(feature_size):
					weights[i] += error*bias_feature[i]
				
				#if output:
				#	for i in range(feature_size):
				#		weights[i] -= bias_feature[i]
				#else:
				#	for i in range(feature_size):
				#		weights[i] += bias_feature[i]
				#print(bias_feature,w_sum,output)

		#If no error, break the loop, training is completed
		if error_counter==0:
			#print correct weights
			#print(f'Correct weights {weights}')
			trigger = False

	#Testing
	for i in range(testing_size):
		bias_feature = [data_test[i][0],data_test[i][1],1]

		#prediction
		w_sum = weighted_sum(bias_feature,weights)
		output = activation(w_sum)

		#update output to dataset
		data_test[i][2] = output
	#print('Testing Done')
	return


def part_two_classifier(data_train, data_test):
	""" multi-classifier perceptron
	Args: 
		data_train: training data
		data_test: testing data
	"""
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8

	#Import constants
	feature_size = common.constants.NUM_FEATURES
	training_size = common.constants.TRAINING_SIZE
	testing_size = common.constants.TEST_SIZE
	class_size = common.constants.NUM_CLASSES

	#Init weights
	weights = [[0 for x in range(feature_size)] for x in range(class_size)]
	#print(weights)

	count = 0
	trigger = True

	#training
	while trigger:
		error_counter = 0

		#Iterate through all training data
		for i in range(training_size):

			#add bias 1 as 3rd element
			bias_feature = [data_train[i][0],data_train[i][1],1]
			label = data_train[i][2]
			#print(bias_feature, data_train[i])
			count +=1

			#Prediction
			w_sum = multi_class_weighted_sum(bias_feature,weights)
			output = multi_class_activation(w_sum)

			#Evaluation
			if output != label:

				#Update weights and error counter
				error_counter+=1
				
				for i in range(feature_size):

					#subtract feature from incorrect weight and add feature to correct weight
					weights[output][i] -= bias_feature[i]
					label_int = int(label)
					weights[label_int][i] +=  bias_feature[i]
		
		#If no error, break the loop, training is completed
		if error_counter==0:
			#print correct weights
			#print(f'Correct weights {weights}')
			trigger = False

	#Testing
	for i in range(testing_size):
		#print(data_test[i][2])
		bias_feature = [data_test[i][0],data_test[i][1],1]

		#prediction
		w_sum = multi_class_weighted_sum(bias_feature,weights)
		output = multi_class_activation(w_sum)

		#update output to dataset
		data_test[i][2] = output
		#print(data_test[i][2])
	#print('Testing Done')

	return



#Helper functions

def weighted_sum(bias_feature,weights):
	weighted_sum = 0
	for i in range(common.constants.NUM_FEATURES):
		weighted_sum+= weights[i] * bias_feature[i]
	
	return weighted_sum

def multi_class_weighted_sum(bias_feature,weights):
	weighted_sum = [0 for x in range(common.constants.NUM_CLASSES)]
	
	for index, weight in enumerate(weights):
		#print(index, weight)
		for i in range(common.constants.NUM_FEATURES):
			weighted_sum[index]+= weight[i] * bias_feature[i]
	
	return weighted_sum

def activation(weighted_sum):
	if weighted_sum>=0:
		return 1
	if weighted_sum<0:
		return 0

def multi_class_activation(weighted_sum):
	max_weight = max(weighted_sum)
	index = weighted_sum.index(max_weight)

	return index