# BJ_2108_통계학 [구현, 정렬]
# https://www.acmicpc.net/problem/2108
# 시간 : 15분
# 산술평균, 중앙값, 범위 출력은 간단했지만 최빈값에서 시간이 소요되었다.
# 결국에는 statistics 라이브러리를 사용해서 최빈값 리스트를 생성해서 해결하였다.
# 내가 만든 로직은 시간초과로 안되던데....

import sys
from statistics import multimode
inputs=sys.stdin.readline
n = int(inputs())
li=[]
for i in range(n):
    li.append(int(inputs()))
    
li = sorted(li)


print(round(sum(li)/n))
print(li[int(len(li)/2)])

modesList = multimode(li)
mode = modesList[1] if len(modesList)>1 else modesList[0]
print(mode)
print(li[-1]-li[0])
