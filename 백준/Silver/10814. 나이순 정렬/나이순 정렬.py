import sys

input = sys.stdin.readline

N = int(input())
sorted_list = []

for _ in range(N):
    data = input().split()
    sorted_list.append(data)

sorted_list.sort(key=lambda x: int(x[0]))

for member in sorted_list:
    print(member[0], member[1])