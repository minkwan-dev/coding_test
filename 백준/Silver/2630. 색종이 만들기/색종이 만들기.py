N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

white_cnt = 0
blue_cnt = 0
    
def recur(row, col, N):
    global white_cnt, blue_cnt

    color = data[row][col]

    for row_idx in range(row, row + N):
        for col_idx in range(col, col + N):
            if data[row_idx][col_idx] != color:
                mid = N // 2
                recur(row, col, mid)
                recur(row, col + mid, mid)
                recur(row + mid, col, mid)
                recur(row + mid, col + mid, mid)

                return
            
    if color == 0:
        white_cnt += 1
    else:
        blue_cnt += 1
            
recur(0, 0, N)

print(white_cnt)
print(blue_cnt)