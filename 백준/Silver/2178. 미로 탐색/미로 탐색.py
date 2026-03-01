import sys

def bfs(n, m, maze):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = [(0, 0)]
    
    while queue:
       
        x, y = queue.pop(0)
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))
                    
    return maze[n-1][m-1]


input = sys.stdin.readline
n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

print(bfs(n, m, maze))