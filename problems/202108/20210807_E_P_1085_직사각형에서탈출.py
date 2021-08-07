# BJ_1085_직사각형에서 탈출
# https://www.acmicpc.net/problem/1085
# 시간 : 3분
# 리뷰 없음.

import sys
x,y,w,h=map(int,sys.stdin.readline().split())
result=min(list([x,y,w-x,h-y]))
print(result)
