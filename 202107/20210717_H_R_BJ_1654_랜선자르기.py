# BJ_1654_랜선 자르기_이진검색
# https://www.acmicpc.net/problem/1654
# 시간 : 30분
# 구현했는데, 시간초과-> 이진검색알고리즘을 이용해야했음

import sys

kn=sys.stdin.readline()
k=int(kn.split()[0])
n=int(kn.split()[1])

data=[]
for i in range(k):
   data.append(int(sys.stdin.readline()))
max=int(sum(data)/n) # 필요한 개수만큼 딱 맞춰서 만들 때 최대 길이

start = 0
end = max
mid = max
# 이진 검색 알고리즘
while True:
    pos_cnt=0 # 만들수 있는 최대 개수
    for i in data:
        pos_cnt+=int(i/mid) # 각 랜선으로 최대 길이로 만들 수 있는 개수
    if pos_cnt<n: # 적게 만들어지면 안됨
        end = mid
    elif start==mid: # 길이가 더 이상 커질 수 없음
        break
    elif pos_cnt>=n: # 많이는 만들어져도 되지만 최대 길이를 찾아야함
        start = mid
    mid = int((start+end)/2)
    
print(mid)
