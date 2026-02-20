import sys

def my_round(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
else:
    grade_list = []
    for _ in range(N):
        grade_list.append(int(input()))
        
    grade_list.sort()
    
    cut_standard = my_round(N*0.15)
    
    if cut_standard > 0:
        cal_list = grade_list[cut_standard:-cut_standard]
    else:
        cal_list = grade_list
        
    result = my_round(sum(cal_list) / len(cal_list))
    print(result)