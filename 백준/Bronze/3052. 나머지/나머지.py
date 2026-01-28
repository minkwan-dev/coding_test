a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

data = [a, b, c, d, e, f, g ,h, i , j]
remain_list = []
count = 0

for elem in data:
    remain_list.append(elem % 42)

remain_set = set(remain_list)
print(len(remain_set))