# BJ_1978_소수 찾기 [소수 검사]
# https://www.acmicpc.net/problem/1978
# 시간 10분
# isPrime() 함수 정의하는 문제. 기억하고 있자.

import sys
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

def isPrime(num):
    if num==1:
        return False
    else:
        sq = int(num**(1/2))
        for i in range(2,sq+1):
            if num%i==0:
                return False
        return True

cnt=0
for nu in li:
    if isPrime(nu):
        cnt+=1
print(cnt)
