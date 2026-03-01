# 백준 9934(완전 이진 트리, 실버 1): 이진트리 연습

import sys
input = sys.stdin.readline

## 함수
def build_tree(arr, level):
    mid = len(arr) // 2
    tree[level].append(arr[mid])
    
    if len(arr) == 1:
        return
    
    build_tree(arr[:mid], level + 1)
    build_tree(arr[mid+1:], level + 1)

## 실행
k = int(input())
inorder = list(map(int, input().split()))
tree = [[] for _ in range(k)]

build_tree(inorder, 0)

for nodes in tree:
    print(*nodes)