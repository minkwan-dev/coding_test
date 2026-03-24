N = int(input())

for _ in range(N):
    str_data = input()

    if len(str_data) >= 6 and len(str_data) <= 9:
        print('yes')
    else:
        print('no')