# BJ_2275_부녀회장이 될테야 [수학]
# https://www.acmicpc.net/problem/2775
# 시간 : 20분
# 리뷰 : 규칙을 찾아내서 해결.

import sys
input=sys.stdin.readline
c=int(input())
for i in range(c):
    k=int(input())
    n=int(input())
    pre_list=[r for r in range(0,15)]
    next_list=list(map(int,"0"*15))
    for j in range(k):
        for h in range(n):
            next_list[h+1]=pre_list[h+1]+next_list[h]
        pre_list=next_list
    print(next_list[n])
