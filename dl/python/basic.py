##first program
#test = "Hello World"
#print("test :" + test)

# #sigmoid impl with basic math module
# import math
# def sigmoid(x):
# 	#1 / 1 + e-x
# 	a  = math.exp(-x);
# 	a = 1 + a
# 	a = 1 / a
# 	return a

# def doPrint(mehtodName, parameter, result):
# 	print(mehtodName + "(" + str(parameter) + ") = " + str(result))

# def doSigTest():
# 	bP = 0
# 	b = sigmoid(bP)
# 	cP = 1
# 	c = sigmoid(cP)
# 	dP = 3
# 	d = sigmoid(dP)
# 	eP = [1, 2, 3];
# 	e = sigmoid(eP)
# 	mehtod = "doSigTest"
# 	doPrint(mehtod, bP, b)
# 	doPrint(mehtod, cP, c)
# 	doPrint(mehtod, dP, d)
# 	doPrint(mehtod, eP, e)

# doSigTest()


# #numpy use for sigmoid
# import numpy as np
# def sigmoid_py(x):
# 	y = 1 / (1 + np.exp(-x))
# 	return y
# # s' = s(1 - s)
# def derive_sigmoid(x):
# 	a = sigmoid_py(x);
# 	b = 1 - a;
# 	return a*b
# def test_sigmoid_np():
# 	x = np.array([1, 2, 3])
# 	print(x)
# 	print(np.exp(x))
# 	print(x + 3)
# 	print(x * 3)
# 	print(1 - x)
# 	print(sigmoid_py(x))
# 	print(derive_sigmoid(x))
# test_sigmoid_np()

# #reshape
# import numpy as np
# def image2Vector(image):
# 	s = image.shape
# 	totalLen = s[0] * s[1] * s[2]
# 	v = image.reshape(totalLen)
# 	print(str(v))
# def testShape():
# 	img = np.array([[[ 0.67826139,  0.29380381],
# 	        [ 0.90714982,  0.52835647],
# 	        [ 0.4215251 ,  0.45017551]],

# 	       [[ 0.92814219,  0.96677647],
# 	        [ 0.85304703,  0.52351845],
# 	        [ 0.19981397,  0.27417313]],

# 	       [[ 0.60659855,  0.00533165],
# 	        [ 0.10820313,  0.49978937],
# 	        [ 0.34144279,  0.94630077]]])
# 	image2Vector(img)
# testShape()

# #normal
# import numpy as np
# def normalizeRows(x):
# 	print("x shape is " + str(x.shape))
# 	v = np.sum(x*x, axis=1)
# 	print("sum of row shape is " + str(v.shape))
# 	print("sum of row is " + str(v))
# 	v = v.reshape(v.shape[0],1)
# 	print("sum of row shape is " + str(v.shape))
# 	print("sum of row is " + str(v))
# 	v = np.sqrt(v)
# 	print("sqrt is " + str(v))
# 	print("shape of sqrt is " + str(v.shape))
# 	# y = v.reshape(2, 3)
# 	z = x / v;
# 	print(str(z))
# 	return z
# def testNormalizeRows():
# 	x = np.array([
# 	    [0, 3, 4],
# 	    [1, 6, 4]])
# 	print("normalizeRows(x) = " + str(normalizeRows(x)))
# testNormalizeRows()

#normal
def printObj(x):
	print("shape is " + str(x.shape))
	print("x is " + str(x))

import numpy as np
def softmax(x):
	x_exp = np.exp(x);
	printObj(x_exp)
	x_sum = np.sum(x_exp, axis=1, keepdims=True);
	printObj(x_sum)
	s = x_exp / x_sum;
	printObj(s)
	return s;
	# print("sum of row shape is " + str(v.shape))
	# print("sum of row is " + str(v))
def testSoftmax():
	x = np.array([
	    [9, 2, 5, 0, 0],
	    [7, 5, 0, 0 ,0]])
	print("softmax(x) = " + str(softmax(x)))
testSoftmax()