n1, n2, n3, n4, n5, n6, n7, n8 = list(map(int, (input().split())))
num_list = [n1, n2, n3, n4, n5, n6, n7, n8]
major_dict = {'1':'c', '2':'d', '3':'e', '4':'f', '5':'g', '6':'a', '7':'b', '8':'C'}

str_result = ''

for elem in num_list:
	str_index = str(elem)
	char_val = major_dict[str_index]
	str_result += char_val
	
if str_result == 'cdefgabC':
	print('ascending')
elif str_result == 'Cbagfedc':
	print('descending')
else:
	print('mixed')