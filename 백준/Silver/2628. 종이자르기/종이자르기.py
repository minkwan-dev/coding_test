width, height = map(int, input().split())

row_cuts = [0, height]
col_cuts = [0, width]

n = int(input())

for _ in range(n):
    direction, cut_point = map(int, input().split())

    if direction == 0:
        row_cuts.append(cut_point)
    
    else:
        col_cuts.append(cut_point)

row_cuts.sort()
col_cuts.sort()

max_row = 0
for i in range(len(row_cuts) - 1):
    diff = row_cuts[i+1] - row_cuts[i]
    if diff > max_row:
        max_row = diff

max_col = 0
for i in range(len(col_cuts) - 1):
    diff = col_cuts[i+1] - col_cuts[i]
    if diff > max_col:
        max_col = diff

print(max_row * max_col)