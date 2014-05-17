"""
@author: Leonid Shalimov
5/17/2014

Mock Interview Problems Prep Series [pt. 1]

Problem:
-------------
Suppose you have a weight on one side of a scale. 
Given an array of other weights, see if the scale will balance. 
You can use weights on either side, and you don't have to use all the weights.

	* Rules:
	---------
	* Direct matching allowed
	* Addition of weights in array to balance allowed

example variables:
	weights 	= [6, 1, 4, 3]
	left		= 0
	right 		= 5
"""

def balance_weights(left=0, right=0, weights=list):
	# Set a key to note original weight location [left or right]
	balance_key_init = 0 if left else 1

	init_weight = left + right;
	print "Init weight: " + str(init_weight)

	for item in weights:
		# This takes care of any direct balancing matches
		if item == init_weight:
			if balance_key_init:
				left = left + item
			else:
				right = right + item
			return True

	# we get here because no direct weights match 5

	# ALGO:
	# Start by ordering the weights from smallest -> largest
	weights.sort()
	# > [1, 3, 4, 6]
	
	# Move from the smallest to largest an 'add them' to the next item
	# 1 + 3 = 4 != 5
	# 1 + 4 = 5 MATCH!!!
	# 1 + 6 = NO MATCH!
	for (counter, item) in enumerate(weights):
		for additionItem in weights[counter:]:
			if(item + additionItem == init_weight):
				if balance_key_init:
					left = left + (item + additionItem)
				else:
					right = right + (item + additionItem)
				return True
		# IF MATCH, DONE
		# IF NO MATCH, MOVE ON TO NEXT NUMBER
		# 3 + 4 != 5
		# 3 + 6 != 5, etc

	# Solution is to have left - right == 0
	

if balance_weights(0, 5, [6, 1, 4, 3]):
	print 'we are able to balance the scale!'
else:
	print 'we are UNABLE to balance the scale! :('