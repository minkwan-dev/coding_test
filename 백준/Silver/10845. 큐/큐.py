import sys 
from collections import deque

input = sys.stdin.readline
queue = deque()
N = int(input())

for _ in range(N):
    command  = input().split()
    
    # push
    if command[0] == 'push':
        queue.append(command[1])
        
    # pop    
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
            
    # size
    elif command[0] == 'size':
        print(len(queue))
        
    # empty    
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
            
    # front
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            
    # back
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])