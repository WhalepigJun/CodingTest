# BJ_2164_카드2 [자료구조, 큐]
# https://www.acmicpc.net/problem/2164
# 시간 : 20분
# 리스트로 구현했을때는 시간초과
# deque를 활용하면 시간초과 해결할 수 있다해서 리스트에서 deque로만 바꿈
# 규칙을 이용해서 다른 알고리즘 적용도 가능

import sys
from collections import deque 

n = int(sys.stdin.readline()) 
deque = deque()
for i in range(1,n+1):
    deque.append(i)

while len(deque)>1:
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num) 
print(deque[0])
