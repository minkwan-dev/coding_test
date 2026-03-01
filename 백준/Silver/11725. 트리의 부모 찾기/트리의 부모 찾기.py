# 백준 11725(트리의 부모 찾기, 실버 2): 부모-자식 관계 설정 연습 

import sys
from collections import deque
input = sys.stdin.readline

## 함수 
def bfs(start, adj, parent):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in adj[v]:
            if parent[i] == 0:
                parent[i] = v
                queue.append(i)

## 실행
n = int(input())
adj = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
parent[1] = 1 

for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

bfs(1, adj, parent)

for i in range(2, n + 1):
    print(parent[i])