# BJ_1929_소수구하기_[소수검사]
# https://www.acmicpc.net/problem/1929
# 시간 : 20분
# 찾아보니까 좀 더 빠르게 할 수 있는 방법은 검사하고 싶은 수의 제곱근을 구해서
# 2부터 그 수가 아닌 제곱근까지 검사하는 것이 좀 더 빠르게 소수 검사를 할 수 있다.

import sys
import math

m,n=map(int,sys.stdin.readline().split())

def isprime(num):
    if num<=1:
        return False
    num_sqrt = int(num**(1/2))
    # 시간을 줄이기 위해 제곱근까지만 확인해도 된다.
    for j in range(2,num_sqrt+1):
        if num % j ==0:
            return False
    return True

for i in range(m,n+1):
    if isprime(i):
        print(i)

