# BJ_1920_수찾기_[정렬,이진탐색]
# https://www.acmicpc.net/problem/1920
# 시간 : 2시간
# 아이디어는 매우 빠르게 찾았다. O(N^2)으로 하면 시간초과가 날 것이 분명하니까
# 정렬을 한 후에 이진탐색을 하면 좀 더 시간복잡도를 줄일 수 있을 것이라고 생각했다.
# 아이디어는 맞았는데, 이진탐색과 sort 함수에서 오래 걸렸다. a.sort(), sort(a) 실행이 안되는것을 찾지 못하고 계속 헤맸다.
# sorted(a) 로 진행해서 a 에 다시 할당시켰다.
# 또한, 이진 탐색 알고리즘을 확실하게 알고 하자!

import sys
n=int(sys.stdin.readline())
a=map(int, sys.stdin.readline().split())
m=int(sys.stdin.readline())
b=map(int, sys.stdin.readline().split())

# a를 정렬하고 k를 이진 탐색을 이용하여 존재여부를 판단한다.
a=sorted(a)

for i in b:
    flag=0
    start=0
    end=n-1
    while start<=end:
        mid=int((start+end)/2)
        if i==a[mid]:
            flag=1
            print("1")
            break
        elif i<a[mid]:
            end=mid-1
        elif i>a[mid]:
            start=mid+1
    if flag==0:
        print("0")     
