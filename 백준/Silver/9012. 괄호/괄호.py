T = int(input())

for _ in range(T):
    ps = input()
    
    stack_count = 0
    is_vps = True
    
    for char in ps:
        if char == '(':
            stack_count += 1
        elif char == ')':
            stack_count -= 1
            
        if stack_count < 0:
            is_vps = False
            break
            
    if is_vps and stack_count == 0:
        print("YES")
    else:
        print("NO")
