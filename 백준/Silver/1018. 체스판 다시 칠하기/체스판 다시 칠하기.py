row, col = map(int, input().split())
matrix = [input() for _ in range(row)]

min_wrong = 64 

for i in range(row - 8 + 1):
    
    for j in range(col - 8 + 1):
        wrong_start_w = 0 
  
        for x in range(i, i + 8):
            
            for y in range(j, j + 8):
                
                if (x + y) % 2 == 0:
                    if matrix[x][y] != 'W': 
                        wrong_start_w += 1
                
                if (x + y) % 2 == 1:
                    if matrix[x][y] != 'B':
                        wrong_start_w += 1
        
        current_min = min(wrong_start_w, 64 - wrong_start_w)
        
        if current_min < min_wrong:
            min_wrong = current_min

print(min_wrong)