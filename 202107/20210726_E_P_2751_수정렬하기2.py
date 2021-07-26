# BJ_2751_수 정렬하기2 [정렬]
# https://www.acmicpc.net/problem/2751
# 시간 : 3분
# 리뷰할게없음.

import sys
n = int(sys.stdin.readline())
li=[]
for i in range(n):
    li.append(int(sys.stdin.readline()))

li=sorted(li)
for i in li:
    print(i)
