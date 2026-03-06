word =list(input())
new_word = []

for elem in word:
	if elem.islower():
		new_word.append(elem.upper())
	elif elem.isupper():
		new_word.append(elem.lower())

print(''.join(new_word))