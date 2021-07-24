# BJ_2292_벌집
# https://www.acmicpc.net/problem/2292
# 시간 : 10분
# n이 1일때를 0이 출력하는 것을 체크하지 못함.

import sys
n=int(sys.stdin.readline())

start=1
cnt=0
while start<n:
    start+=6*cnt
    cnt+=1
if n==1:
    cnt=1
print(cnt)
