n = int(input())
data = list(map(int, input().split()))
count = 0

for elem in data:
	is_prime = True
	if elem < 2:
		is_prime = False
		
	for i in range(2, elem):		
		if elem % i == 0:
			is_prime = False
			break
	if is_prime:
		count += 1

print(count)