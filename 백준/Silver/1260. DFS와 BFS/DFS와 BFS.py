# 백준 1260(DFS와 BFS, 실버 2): BFS, DFS 기초 개념

import sys
from collections import deque
input = sys.stdin.readline

## 함수
def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in adj[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in adj[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)

## 실행
n, m, v = map(int, input().split())

adj = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

for i in range(1, n + 1):
    adj[i].sort()

visited_dfs = [False] * (n + 1)
dfs(v)
print()

visited_bfs = [False] * (n + 1)
bfs(v)