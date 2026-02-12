N = int(input())

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

str_data = str(factorial(N))
cnt = 0

for i in range(len(str_data) - 1, -1, -1):
    if str_data[i] == '0':
        cnt += 1
    else:
        break 

print(cnt)