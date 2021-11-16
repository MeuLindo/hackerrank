import math, os, random, re, sys

def plusMinus(arr):
	total = len(arr)
	positivos = 0.0
	negativos = 0.0
	zeros = 0.0
	for num in arr:
		if (num == 0):
			zeros = zeros + 1
		elif (num < 0):
			negativos = negativos + 1
		elif (num > 0):
			positivos = positivos + 1
	rpos = positivos/total
	rneg = negativos/total
	rzero = zeros/total

	print("{0:.6f}".format(rpos))
	print("{0:.6f}".format(rneg))
	print("{0:.6f}".format(rzero))


ex = [1,1,0,-1,-1]
plusMinus(ex)

