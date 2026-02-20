import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()


print(round(sum(data) / n))
print(data[n//2])

dic = {}

for elem in data:
    if elem in dic:
        dic[elem] += 1
    else:
        dic[elem] = 1
        
max_cnt = max(dic.values())
modes = []

for key, value in dic.items():
    if value == max_cnt:
        modes.append(key)
        
modes.sort()

if len(modes) >= 2:
    print(modes[1])
else:
    print(modes[0])
    
print(data[-1]-data[0])