N, K = map(int, input().split())

# -------------------------------------------
students = [[0] * 7 for _ in range(2)]

for _ in range(N):
    S, Y = map(int, input().split())
    students[S][Y] += 1

required_room_cnt = 0

# -------------------------------------------
for i in range(2):
    for j in range(1, 7):
        
        num = students[i][j]
        
        if num > 0:
            required_room_cnt += (num // K)

            if num % K > 0:
                required_room_cnt += 1

print(required_room_cnt)