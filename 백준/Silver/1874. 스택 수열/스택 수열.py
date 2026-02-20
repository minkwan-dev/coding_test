import sys

input = sys.stdin.readline

n = int(input())
data_list = [int(input()) for _ in range(n)]

temp_list = []      
operator_stack = [] 
current = 1         
possible = True     

for target in data_list:
   
    while current <= target:
        temp_list.append(current)
        operator_stack.append('+')
        current += 1
    
    if temp_list[-1] == target:
        temp_list.pop()
        operator_stack.append('-')
    
    else:
        possible = False
        break

if possible:
    for op in operator_stack:
        print(op)
        
else:
    print("NO")