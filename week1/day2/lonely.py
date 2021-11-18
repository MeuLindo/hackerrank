def lonelyInteger(a):
	for number in a:
		if a.count(number) == 1:
			return number

a = [1,2,3,4,3,2,1]


print(lonelyInteger(a))
