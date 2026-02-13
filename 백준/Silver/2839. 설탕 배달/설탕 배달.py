import sys

n = int(sys.stdin.readline())
bag_cnt = 0

while n >= 0:
    if n % 5 == 0:
        bag_cnt += (n // 5)
        print(bag_cnt)
        break

    n -= 3
    bag_cnt += 1

else:
    print(-1)
