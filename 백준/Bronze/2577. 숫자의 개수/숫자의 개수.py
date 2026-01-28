a = int(input())
b = int(input())
c = int(input())
result = a*b*c
str_result = str(result)
for num in range(10):
	count = 0
	for elem in str_result:
		if int(elem) == num:
			count += 1
	print(count)