# BJ_2839_설탕 배달 [수학, 다이나믹 프로그래밍, 그리디 알고리즘, 브루트포스 알고리즘]
# https://www.acmicpc.net/problem/2839
# 시간 : 10분
# 리뷰 처음에는 5kg을 최대한으로 넣고 남는 무게를 3kg으로 채우고 안되면 -1이었는데
# 생각해보니까 6kg 같은 경우는 3kg 두개로 할 수 있음.
# 반복문을 통해 해결

import sys
n=int(sys.stdin.readline())
flag=0
for i in range(n//5,-1,-1):
  num_5=i
  num_3=(n-i*5)//3
  if n==num_5*5+num_3*3:
    flag=1
    break
if flag==1:
  print(num_5+num_3)
else:
  print(-1)
