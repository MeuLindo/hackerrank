import math, os, random, re, sys


def miniMaxSum(array):
	array.sort()
	minSumArray = array.copy()
	minSumArray.pop()
	minSum = sum(minSumArray)

	maxSumArray = array.copy()
	maxSumArray.pop(0)
	maxSum = sum(maxSumArray)

	print(array)
	print(minSumArray)
	print(minSum)
	print(maxSumArray)
	print(maxSum)
	print(minSum," ",maxSum)




array = [2,1,4,3,5]


miniMaxSum(array)
