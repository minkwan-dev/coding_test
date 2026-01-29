n = int(input())
strings = [input() for _ in range(n)]

for i in strings:
	cur_sum = 0
	final_sum = 0
	for j in i:
		if j == 'O':
			cur_sum = cur_sum + 1
			final_sum += cur_sum
		elif j == 'X':
			cur_sum = 0
	print(final_sum)