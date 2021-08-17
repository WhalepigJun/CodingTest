# BJ_11866_요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
# 시간 : 30분
# 리뷰 : 큐를 이용할 생각을 하지 않아서 굉장히 오래 걸린 문제
# 문제 유형에 큐가 적혀있는 것을 확인하고나서 빠르게 해결할 수 있었다. 

import sys
n,k = map(int,sys.stdin.readline().split())
queue=[i+1 for i in range(n)]
result=[]
while True:
    for _ in range(k-1):
        queue.append(queue[0])
        queue.remove(queue[0])
    result.append(queue.pop(0))
    if len(queue)==0:
        break
        
print("<",end="")
for i in range(len(result)):
    print("{0}".format(result[i]), end="")
    if not i==len(result)-1:
        print(", ", end="")
print(">")
