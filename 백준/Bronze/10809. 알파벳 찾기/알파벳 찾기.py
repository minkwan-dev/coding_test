s = input()
alphabet_list = [chr(i) for i in range(97,123)]

for elem in alphabet_list:
	result = s.find(elem)
	print(result, end = ' ')