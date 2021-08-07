# BJ_2231_분해합 [브루트포스 알고리즘]
# https://www.acmicpc.net/problem/2231
# 시간 : 5분
# 리뷰없음.

import sys
n = int(sys.stdin.readline())

for i in range(1,n+1):
    li = list(map(int,str(i)))
    if i+sum(li)==n:
        print(i)
        break
    if i==n:
        print(0)
