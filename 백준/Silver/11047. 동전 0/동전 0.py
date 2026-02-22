N, K = map(int, input().split())
asc_val = [int(input()) for _ in range(N)]
min_cnt = 0

asc_val.reverse()

for coin in asc_val:
    if K == 0:
        break

    min_cnt += K // coin
    K %= coin

print(min_cnt)