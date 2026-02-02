card_num, limit_sum = map(int, input().split())
num_list = list(map(int, input().split()))[:card_num]
ans = 0

for i in range(card_num):
	for j in range(i + 1, card_num):
		for k in range(j + 1, card_num):
			temp = num_list[i] + num_list[j] + num_list[k]
			if (temp <= limit_sum) and (temp > ans):
				ans = temp

print(ans)