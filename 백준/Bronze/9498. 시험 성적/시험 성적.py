n = int(input())

condition_a = 90 <= n <= 100
condition_b = 80 <= n < 90
condition_c = 70 <= n < 80
condition_d = 60 <= n < 70

if condition_a:
    print('A')
elif condition_b:
    print('B')
elif condition_c:
    print('C')
elif condition_d:
    print('D')
else:
    print('F')
