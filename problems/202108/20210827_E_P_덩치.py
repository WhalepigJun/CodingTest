# BJ_7468_덩치 [구현, 브루트포스 알고리즘]
# https://www.acmicpc.net/problem/7568
# 시간 : 20분
# 리뷰 : 처음엔 정렬을 이용하고 dictionary를 이용해서 구현하려고 했는데,
# 계속 실패해서 찾아보니 시간복잡도 O^2 으로 구현하면 쉽게 가능해서 전부를 살펴보는 것으로 변경

import sys
input=sys.stdin.readline
N=int(input())
data = []
rank = []
for _ in range(N):
    x,y = map(int,input().split())
    data.append((x,y))
for i in data:
    rank=1
    for j in data:
        if i[0]<j[0] and i[1]<j[1]:
            rank+=1
    print(rank, end=" ")    
