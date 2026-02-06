T = int(input())

for i in range(1, T + 1):
	K = int(input())
	N = int(input())	

	matrix_data = [[0] * (N + 1) for _ in range(K + 1)]

	for row in range(K + 1):
		for column in range(1, N + 1):

			if row == 0:
				matrix_data[0][column] = column 		
			else:			
				matrix_data[row][column] = matrix_data[row][column-1] + matrix_data[row-1][column]

	resident_num = matrix_data[K][N]


	print(resident_num)