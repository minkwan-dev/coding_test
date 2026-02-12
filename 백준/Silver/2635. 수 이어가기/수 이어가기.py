# WWF: 가장 숫자가 많은 리스트의 갯수 + 그 리스트

N = int(input())

temp_len = 1
final_list = []

for i in range(0, N+1):
    num_list = [N]
    num_list.append(i)
    while True:
        j = num_list[-2] - num_list[-1]
        if j >= 0:
            num_list.append(j)

        else:
            break


    if len(num_list) > temp_len:
        temp_len = len(num_list)
        final_list = num_list


print(temp_len)
print(*final_list)

