h, m = map(int, input().split())


 
data = 60*h + m
result = data - 45
h = result // 60
m = result % 60

if h == -1:
    h = 23

print(f'{h} {m}')
