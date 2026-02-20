T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    
    data = list(map(int, (input().split())))
    
    queue = []
    
    for idx in range(len(data)):
        queue.append((idx, data[idx]))
        
    count = 0
    
    while True:
        current = queue.pop(0)
        
        is_max = True
        
        for doc in queue:
            if current[1] < doc[1]:
                is_max = False
                break
            
        if not is_max:
            queue.append(current)
            
        else:
            count += 1
            
            if current[0] == M:
                print(count)
                break