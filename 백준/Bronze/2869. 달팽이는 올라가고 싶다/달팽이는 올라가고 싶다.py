day_move, night_move, height = list(map(int, input().split()))

target = height - day_move

net_move = day_move - night_move

days = target // net_move

if target % net_move != 0:
	days += 1

result = days + 1

print(result)