# BJ_2798_블랙잭 [브루트포스 알고리즘]
# https://www.acmicpc.net/problem/2798
# 시간 : 10분
# 리뷰 없음. 
# 단순하게 처음부터 끝까지 반복문을 돌면서 조건에 맞는 값을 찾는 문제

import sys
n,m=map(int,sys.stdin.readline().split())
cards=list(map(int,sys.stdin.readline().split()))
cards=sorted(cards)

def blackjack(n,m,cards):
    max=0
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                tmp_sum=cards[i]+cards[j]+cards[k]
                if tmp_sum>m:
                    continue
                if tmp_sum>max:
                    max=tmp_sum
    return max

print(blackjack(n,m,cards))
