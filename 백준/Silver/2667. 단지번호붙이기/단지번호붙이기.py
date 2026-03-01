# 백준 2667(단지번호붙이기, 실버 1): 델타연산 연습, BFS/DFS 연습

import sys
input = sys.stdin.readline

## 함수 
def dfs(x, y):
    global count
    visited[x][y] = True
    count += 1
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)

## 실행
n = int(input())
grid = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

result = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            count = 0
            dfs(i, j)
            result.append(count)

print(len(result))
for out in sorted(result):
    print(out)