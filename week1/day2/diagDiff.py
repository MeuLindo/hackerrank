def diagonalDifference(arr):
	primeiraDiagonal = []
	segundaDiagonal = []
	indexP = 0
	indexS = len(arr) - 1
	for linha in arr:
		primeiraDiagonal.append(linha[indexP])
		indexP = indexP + 1

		segundaDiagonal.append(linha[indexS])
		indexS = indexS - 1

	somaPrimeiraD = sum(primeiraDiagonal)
	somaSegundaD = sum(segundaDiagonal)

	diferencaAbsoluta = abs((somaPrimeiraD - somaSegundaD))


	print(primeiraDiagonal)
	print(segundaDiagonal)
	print(somaPrimeiraD)
	print(somaSegundaD)
	print(diferencaAbsoluta)
arr = [[11,2,4],[4,5,6],[10,8,-12]]



diagonalDifference(arr)


