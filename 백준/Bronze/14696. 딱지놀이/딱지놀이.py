N = int(input())

for _ in range(N):
    winner = 'D'
    a_card = list(map(int, input().split()))
    b_card = list(map(int, input().split()))

    if a_card.count(4) > b_card.count(4):
        winner = 'A'
    elif a_card.count(4) < b_card.count(4):
        winner = 'B'
    
    if a_card.count(4) == b_card.count(4) and a_card.count(3) > b_card.count(3):
        winner = 'A'
    elif a_card.count(4) == b_card.count(4) and a_card.count(3) < b_card.count(3):
        winner = 'B'

    if a_card.count(4) == b_card.count(4) and a_card.count(3) == b_card.count(3) and a_card.count(2) > b_card.count(2):
        winner = 'A'
    elif a_card.count(4) == b_card.count(4) and a_card.count(3) == b_card.count(3) and a_card.count(2) < b_card.count(2):
        winner = 'B'

    if a_card.count(4) == b_card.count(4) and a_card.count(3) == b_card.count(3) and a_card.count(2) == b_card.count(2) and a_card.count(1) > b_card.count(1):
        winner = 'A'
    elif a_card.count(4) == b_card.count(4) and a_card.count(3) == b_card.count(3) and a_card.count(2) == b_card.count(2) and a_card.count(1) < b_card.count(1):
        winner = 'B'

    print(winner)