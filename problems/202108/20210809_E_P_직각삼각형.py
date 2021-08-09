# BJ_4153_직각삼각형 [수학,기하학]
# https://www.acmicpc.net/problem/4153
# 시간 : 5분
# 리뷰 없음.

import sys
input=sys.stdin.readline
while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else:
        if a>b:
            if a>c:
                if a**2==b**2+c**2:
                    print("right")
                else:
                    print("wrong")
            else:
                if c**2==a**2+b**2:
                    print("right")
                else:
                    print("wrong")
                    
        else:
            if c>b:
                if c**2==a**2+b**2:
                    print("right")
                else:
                    print("wrong")
            else:
                if b**2==a**2+c**2:
                    print("right")
                else:
                    print("wrong")
