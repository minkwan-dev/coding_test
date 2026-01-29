
while True:
	data = list(map(int, (input().split())))
	data.sort()
	result = (data[0])**2 + (data[1])**2
	if result == 0:
		break
	if ((data[2])**2 == result):
		print("right")
	else:
		print("wrong") 

