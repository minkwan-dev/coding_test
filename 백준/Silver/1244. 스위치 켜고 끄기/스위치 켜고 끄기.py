def change(num):
    if switch[num] == 0:
        switch[num] = 1
    else:
        switch[num] = 0
    return

N = int(input())
switch = [-1] + list(map(int, input().split()))
students = int(input())

for _ in range(students):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(num, N+1, num):
            change(i)
    
    else:
        change(num)

        for i in range(N//2):
            if num + i > N or num - i < 1:
                break

            if switch[num + i] == switch[num - i]:
                change(num+i)
                change(num-i)
            
            else:
                break

for i in range(1, N+1):
    
    print(switch[i], end = ' ')

    if i % 20 == 0:
        print()