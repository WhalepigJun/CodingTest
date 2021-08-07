# BJ_1436_영화감독 숌_구현
# https://www.acmicpc.net/problem/1436
# 시간 : 10분
# 

# 666, 1666, 2666, 3666, 4666, 5666,
# 6660, 6661, 6662, 6663, ....

from sys import stdin
n = int(stdin.readline())

i = 666 # 666부터 시작
cnt = 0
while n!=cnt: # 입력값과 카운트가 같아지면 반복문 멈춤
    if str(i).find("666")!=-1 : # 666이 포함되어 있으면
        cnt+=1
    i+=1
print(i-1)
 
