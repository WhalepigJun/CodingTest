# BJ_2609_최대공약수와 최소공배수 [수학, 정수론, 유클리드 호제법]
# https://www.acmicpc.net/problem/2609
# 시간 : 10분
# 리뷰 : gcd 알고리즘만 알고있으면 간단한 문제 였다.

def gcd(num1, num2):
    if num1%num2==0:
        return num2
    else:
        return gcd(num2,num1%num2)
    
import sys
nums = list(map(int, sys.stdin.readline().split()))
n1 = nums[0]
n2 = nums[1]

result1=gcd(n1,n2)
result2=int(result1*(n1/result1)*(n2/result1))

print(result1)
print(result2)

