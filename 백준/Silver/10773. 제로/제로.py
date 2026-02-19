K = int(input())

data_list = []

for tc in range(1, K + 1):
    data = int(input())
    
    if data == 0:
        data_list.pop()
    else: 
        data_list.append(data)
        

print(sum(data_list))