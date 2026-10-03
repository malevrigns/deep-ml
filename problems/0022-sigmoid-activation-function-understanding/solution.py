import math

def sigmoid(z: float) -> float:
	#Your code here
	raw_result = 1/ (1+math.exp(-z))
	result = round(raw_result,4)
	return result