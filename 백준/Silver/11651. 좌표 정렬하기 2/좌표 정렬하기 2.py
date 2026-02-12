import sys

input = sys.stdin.readline

n = int(input())
temp = []

for _ in range(n):
    data = input().split()
    temp.append(data)

temp.sort(key=lambda x: (int(x[1]), int(x[0])))

for num in temp: 
    print(num[0], num[1])