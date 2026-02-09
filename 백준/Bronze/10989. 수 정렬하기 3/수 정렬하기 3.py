import sys

input = sys.stdin.readline

T = int(input())

count_list = [0] * 10001

for _ in range(T):
    num = int(input())
    count_list[num] += 1

for i in range(10001):
    if count_list[i] != 0:
        for _ in range(count_list[i]):
            print(i)