N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]

    winner = 'D'

    for shape in range(4, 0, -1):  
        if A.count(shape) > B.count(shape):
            winner = 'A'
            break
        elif A.count(shape) < B.count(shape):
            winner = 'B'
            break

    print(winner)