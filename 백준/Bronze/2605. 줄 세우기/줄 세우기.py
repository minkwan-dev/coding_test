import sys

N = int(sys.stdin.readline())

picked_num_list = list(map(int, sys.stdin.readline().split()))

result = []

for i in range(N):
    result.insert(len(result) - picked_num_list[i], i + 1)

print(*result)