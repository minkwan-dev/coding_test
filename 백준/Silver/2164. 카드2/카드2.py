import sys
from collections import deque

N = int(input())

dq = deque(range(1, N + 1))

while len(dq) > 1:
    dq.popleft()

    if len(dq) == 1:
        break

    dq.append(dq.popleft())

print(dq[0])