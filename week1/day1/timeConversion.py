
import math, os, random, re, sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
	if s[-2:] == "PM":
		print(s[:-2])
		hhmmss = s[:-2].split(":")
		if not hhmmss[0] == '12':
			hora = int(hhmmss[0]) + 12
			hhmmss[0] = str(hora)
			militarPM = ":".join(hhmmss)
			return militarPM
		else:
			return s[:-2]

	if s[-2:] == "AM":

		hhmmss = s[:-2].split(":")
		if hhmmss[0] == '12':
			hhmmss[0] = '00'
			return ":".join(hhmmss)
		return s[:-2]




s = "12:45:54PM"
s2 = "12:40:22AM"

timeConversion(s)
#print(timeConversion(s2))
