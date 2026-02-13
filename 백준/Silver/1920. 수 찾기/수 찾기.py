import sys

n = int(sys.stdin.readline())
set_a = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
list_b = list(map(int, sys.stdin.readline().split()))

for target in list_b:
    if target in set_a:
        print(1)
    else:
        print(0)