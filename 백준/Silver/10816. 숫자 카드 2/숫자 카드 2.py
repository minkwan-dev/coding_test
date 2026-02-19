import sys
input = sys.stdin.readline

n = int(input())
my_list = map(int, input().split())

m = int(input())
card_list = map(int, input().split())

dic = {}

for data in my_list:
    if data in dic:
        dic[data] += 1
    else:
        dic[data] = 1
        
for data in card_list:
    if data in dic:
        print(dic[data], end=' ')
    else:
        print(0, end=' ')
