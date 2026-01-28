t = int(input())

for i in range(t):
	r, s = input().split()
	for elem in s:
		print(elem*int(r), end='')
	print()