n = int(input())
shirts_list = list(map(int, input().split()))
t, p = list(map(int, input().split()))


count = 0

for elem in shirts_list:
	if elem == 0:
		continue
	if elem <= t:
		count += 1
	if elem > t:
		if (elem % t) == 0:
			count += elem // t
		else:	
			count += (elem // t) + 1

print(count)
print(n // p, end=' ')
print(n % p)