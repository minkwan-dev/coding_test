T = int(input())

for _ in range(T):
    N = int(input())
    result = {}
    total = 1
    for _ in range(N):
        data = list(map(str, input().split()))
        
        cnt = 0

        if data[1] not in result:
            cnt = 1
            result[data[1]] = cnt
        else:
            result[data[1]] = result[data[1]] + 1

    for value in result.values():
        total *= (value + 1)

    total = total - 1
    
    print(total)