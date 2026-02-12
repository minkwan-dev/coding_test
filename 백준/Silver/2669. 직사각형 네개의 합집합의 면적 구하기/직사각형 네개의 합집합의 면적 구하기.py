board = [[0]*100 for _ in range(100)]

# 인풋을 받으면서
# 첫번째 포인트에서 마지막 포인트까지 돌면서
# 하나씩 해당하는 코디넷에 보드를 1로 채움

# 만약 이미 그 코디넷이 1로 채워있다면 넘어가기
count = 0
for i in range(4):

    rec = list(map(int,input().split()))
    for y in range(rec[1], rec[3]):
        for x in range(rec[0], rec[2]):
            if board[y][x] == 1:
                pass
            else:
                board[y][x] = 1
                count+=1

print(count)