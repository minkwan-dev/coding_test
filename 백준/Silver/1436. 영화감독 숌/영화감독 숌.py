n = int(input())

cnt = 0
num = 666

while True:
    str_data = str(num)

    if '666' in str_data:
        cnt += 1

    if n == cnt:
        break

    num += 1

print(num)
