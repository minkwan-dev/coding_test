n = int(input())

end = 1
step = 1

while(n > end):
    step += 1
    end += 6 * (step-1)
    
print(step)