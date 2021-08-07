# BJ_2869_달팽이는 올라가고 싶다 [수학]
# https://www.acmicpc.net/problem/2869
# 시간 : 10분
# 리뷰 : 처음에는 while문을 통해서 반복문으로 찾았는데 시간초과 문제로
# 규칙을 찾아서 식으로 해결

import sys, math
a,b,v=map(int,sys.stdin.readline().split())
print(math.ceil((v-a)/(a-b)+1))
