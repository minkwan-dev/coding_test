import sys

N = int(input())
stack = []
for tc in range(N):
    arr = sys.stdin.readline().split()
    # push는 스택에 x를 정수x를 넣음
    if arr[0] == 'push':
        stack.append(int(arr[-1]))
    # pop은 스택 맨 위에 정수를 빼서 출력 // 스택이 비어 있으면 -1 출력
    if arr[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    # size 스택에 들어있는 정수의 갯수 출력
    if arr[0] == 'size':
        print(len(stack))
    #empty: 스택이 비어있으면 1, 아니면 0
    if arr[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    # top 스택 가장 위에 있는 정수를 출력 (빼지는 않음) // 비어있으면 -1
    if arr[0] == 'top':
        if stack:
            print(int(stack[-1]))
        else:
            print(-1)
