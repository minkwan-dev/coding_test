# 백준 1012(유기농배추, 실버 2): 델타연산 연습

import sys
from collections import deque
input = sys.stdin.readline

## 함수 
def bfs(x, y, m, n, field):
    queue = deque([(x, y)])
    field[y][x] = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if field[ny][nx] == 1:
                    field[ny][nx] = 0
                    queue.append((nx, ny))

## 실행
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    for _ in range(k):
        px, py = map(int, input().split())
        field[py][px] = 1
    
    warm_count = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(j, i, m, n, field)
                warm_count += 1
    print(warm_count)