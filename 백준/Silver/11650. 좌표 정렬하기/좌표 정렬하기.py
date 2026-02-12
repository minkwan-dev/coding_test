import sys

input = sys.stdin.readline
n = int(input())
sorted_list = []

for _ in range(n):
    data = input().split()
    sorted_list.append(data)

sorted_list.sort(key=lambda x: (int(x[0]), int(x[1])))

for num in sorted_list:
    print(num[0], num[1])