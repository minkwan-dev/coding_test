n = int(input())

new_list = list(map(int, input().split()))
   
num_1 = min(new_list)
num_2 = max(new_list)
print(num_1, end=' ')
print(num_2)