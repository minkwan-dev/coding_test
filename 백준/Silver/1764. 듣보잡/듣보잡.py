import sys
input = sys.stdin.readline

N, M = map(int, input().split())

unheard = set(input().strip() for _ in range(N))
unseen = set(input().strip() for _ in range(M))

result = sorted(list(unheard & unseen))

print(len(result))

for name in result:
    print(name)