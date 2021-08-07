# BJ_2805_나무자르기 [이진탐색]
# https://www.acmicpc.net/problem/2805
# 시간 : 오래걸림
# 이진탐색으로 해야겠다는 아이디어는 잘 잡았는데 정확한 값을 못찾고
# 그것보다 작은 값을 선택하는 것에대한 어려운점
# 시간 초과 문제에 대해 해결하느라 오래걸림

import sys
n,m=map(int, sys.stdin.readline().split())
trees=list(map(int, sys.stdin.readline().split()))

start=0
end=max(trees)

while start<=end:
    mid=(start+end)//2
    li= [tree-mid if tree>mid else 0 for tree in trees]
    sumli = sum(li)
    if sumli>=m:
        result=mid
        start=mid+1
    else:
        end=mid-1
print(result)
