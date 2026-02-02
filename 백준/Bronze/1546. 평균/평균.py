n = int(input()) 
sub = list(map(int, input().split()))[:n]

max_num = max(sub)
result = 0
final_result = 0

for elem in sub:
    result += (elem/max_num)*100
    
final_result = result / len(sub)
    
print(final_result)