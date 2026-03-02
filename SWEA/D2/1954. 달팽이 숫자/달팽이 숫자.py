T = int(input())
for t in range(1, T + 1):
    N = int(input())
    grid = [[0] * N for _ in range(N)]
    
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    r, c, dist = 0, 0, 0
    
    for i in range(1, N * N + 1):
        grid[r][c] = i
        
        nr = r + dr[dist]
        nc = c + dc[dist]
        
        if not (0 <= nr < N and 0 <= nc < N) or grid[nr][nc] != 0:
            dist = (dist + 1) % 4
            nr = r + dr[dist]
            nc = c + dc[dist]
            
        r, c = nr, nc
        
    print(f"#{t}")
    for row in grid:
        print(*row)