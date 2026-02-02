l = int(input())
s = input()


r = 31
m = 1234567891

ascii_list = []
temp_sum = 0

for elem in s:
    ascii_list.append(ord(elem)-96)
    
for i in range(len(ascii_list)):
    cur_sum = ascii_list[i] * (r**i)
    temp_sum += cur_sum


print(temp_sum % m)